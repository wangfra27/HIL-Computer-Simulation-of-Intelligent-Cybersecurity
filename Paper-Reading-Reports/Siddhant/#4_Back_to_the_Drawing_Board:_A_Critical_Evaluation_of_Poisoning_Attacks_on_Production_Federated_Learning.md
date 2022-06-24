# Back to the Drawing Board: A Critical Evaluation of Poisoning Attacks on Production Federated Learning
### [Link to Article](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/IEEE%202022/Back%20to%20the%20Drawing%20Board%20A%20Critical%20Evaluation%20of%20Poisoning%20Attacks%20on%20Federated%20Learning%20.pdf)
---
## Summary
While recent works have indicated that Federated Learning may be vulnerable to poisoning attacks by compromised clients, their real impact on production FL systems is not truly understood. This paper aims to develop a comprehensive systemization for poisoning attacks on FL by enumerating all possible threat models, variations of poisoning, and adversary capabilities. The paper specifically focuses on Untargeted Poisoning Attacks as it argues they are significantly relevant to production FL deployment. The findings were rather surprising: contrary to the established belief, FL is highly robust in practice even when using simple, low-cost defenses. This paper goes further and proposes novel, state-of-the-art data and model poisoning attacks, and show via an extensive set of experiments across three benchmark datasets how ineffective poisoning attacks are in the presence of simple defense mechanisms. This paper aims to correct previous misconceptions and offer concrete guidelines to conduct more accurate (and more realistic) research on this topic. 

## The Three Major Approaches To Poisoning FL
![diagram showing differences between three major approaches to poisoning FL](https://user-images.githubusercontent.com/52840861/175426193-d307b31d-371e-41de-9f43-978b0db01551.png)

Backdoor Poisoning Attacks – These types of poisoning attacks aim to misclassify only input with a certain predetermined trigger (e.g., only images with cars in them) in order to create a backdoor. The model works perfectly fine for non-trigger data, which makes this attack hard to detect. However, if the input data has the specific trigger, then the attack is triggered and the malicious output is given.

Targeted Poisoning Attacks – These types of poisoning focus on misclassifying only a certain specific set/classes of input.

Untargeted Poisoning Attacks – aim to reduce model accuracy on arbitrary inputs. It does not discriminate input.  

#### Why Untargeted?
The paper focuses specifically on Untargeted Poisoning Attacks as it is significantly relevant to production deployments: it can be used to impact a large population of FL clients and it can remain undetected for long duration.

### The Gap Between Literature and Practice
The existing literature on poisoning attacks and defenses for FL makes __unrealistic assumptions__  that do not hold in real-world FL deployments. For example, assumptions about the percentages of compromised clients, total number of FL clients, and the types of FL systems. For instance, state-of-the-art attacks assume adversaries who can compromise up to 25% of FL clients. For an app like GBoard with ~1B downloads, 25% compromised would mean an attacker controls __250 million android devices!__ Thus, we argue that the assumption in recent FL robustness works do not represent common real-world adversarial scenarios that account for the difficulty and cost of at-scale compromises.

## Systemization of FL Poisoning Threat Models

![table of key dimensions of threat model](https://user-images.githubusercontent.com/52840861/175435451-4b8e923d-af0a-49a5-8bfc-e6c543c1798f.png)

We present three key dimensions for the threat model of FL poisoning, as shown above. Each combination of these dimensions constitutes a threat model. Note that some of these are impractical. 

Production FL can either be **cross-device** or **cross-silo**. In cross-device FL, the number of clients is large (from few thousand to billions) and only a small fraction of them is chosen in each FL training round. In this case, the amount of data that can be processed is quite limited. And there is also the possibility of a small fraction dropping out due to highly unreliable network connections. In cross-silo FL, the number of clients is moderate (up to 100) and all clients are selected in each round. Clients are large corporations (e.g., banks) and have devices with ample resources. Thus, they can process ample data and client drop-outs do not happen. In both FL types, the on-device model used for inference and the on-device model being trained are different. Hence, and adversary cannot gain any insight into the training-model by querying the inference-model. That leaves 8 threat models behind. 

![image](https://user-images.githubusercontent.com/52840861/175441335-a0efbc41-31f3-4bc0-a331-c12a04d514ad.png)

However, going off what is practical, only 2 models are left: T4 (nobox offline data poison), and T5 (whitebox online model poison). Since model poisoning capability means whitebox access by default, thus T1 and T2 are not valid. In cross-device FL, only a select few clients get the most recent global model in each round. Hence, to gain whitebox access to the model, the adversary needs to control (i.e., break into) a large number of devices, which is impractical in practice. With whitebox access, the adversary can mount the stronger online model poisoning attacks (MPAs) instead of data poisoning attacks (DPAs). Therefore, T3, T7, and T8 are also impractical. Under T6, the adversary mounts and online attack (i.e., they adaptively poison the local data of the compromised clients). But, since the adversary has no knowledge of the current global model due to nobox access, they cannot generate new poisoning data adaptively. Hence, T6 is impractical.

## Improved Poisoning Attack

Note:
An aggregation is a process in which numbers are gathered for statistical purposes and are expressed as one number. This could be in the form of a total or an average. Each measure has a regular aggregate. Aggregation rules can be used in addition to the regular aggregate. Aggregation rules define how a measure is aggregated in relation to one of more dimensions.

Aggregation rules can be
* Distributive (Count, Sum, Maximum, Minimum)
* Non-distributive (Average, Standard Deviation, Variance)
* Time state (First, Last, Current Period)
___

Our optimization problem for poisoning attacks is based on that of [this paper](https://people.cs.umass.edu/~amir/papers/NDSS21-model-poisoning.pdf). Specifically, we aim to craft poisoned updates (via data or model poisoning) which will increase the overall distance between the poisoned aggregate (computed using poisoned and benign update) and the benign aggregrate (computed using only benign updates). This can be formalized as follows:

![optimization problem formalization](https://user-images.githubusercontent.com/52840861/175459090-203d1a7d-39b1-4ae8-a524-b89faf1178e5.png)

**m** is the number of compromised clients selected in the given round. f_agr is the target AGR/ f_avg is the Average AGR. The del with the **n** are the benign updates available to the adversary (e.g., updates computed using the benign data of compromised clients). del **b** is a reference benign aggregrate. And del with the **m** are **m** replicas of the poisoned update of our attack. del **p** is the final poisoned aggregrate.

Although our optimization problem in (1) is the same as [the aformentioned paper](https://people.cs.umass.edu/~amir/papers/NDSS21-model-poisoning.pdf), there are two key differences from [the paper](https://people.cs.umass.edu/~amir/papers/NDSS21-model-poisoning.pdf). First, we are the first to use (1) to construct systematic data poisoning attacks on FL. Second, our model poisoning attacks not only tailor the optimization in (1) to the given AGR, but also to the given dataset and global model, by using [stochastic gradient ascent](https://pastebin.com/DPYaFADk) algorithm; this boosts the efficacy of our attack.  

## Analysis of FL Robustness

