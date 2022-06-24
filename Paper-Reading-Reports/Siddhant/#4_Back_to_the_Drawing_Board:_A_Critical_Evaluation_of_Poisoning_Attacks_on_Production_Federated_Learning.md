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
The existing literature on poisoning attacks and defenses for FL makes __unrealistic assumptions__  that do not hold in real-world FL deployments. For example, assumptions about the percentages of compromised clients, total number of FL clients, and the [types of FL systems](https://arxiv.org/pdf/1912.04977.pdf) For instance, state-of-the-art attacks assume adversaries who can compromise up to 25% of FL clients. For an app like GBoard with ~1B downloads, 25% compromised would mean an attacker controls __250 million android devices!__ Thus, we argue that the assumption in recent FL robustness works do not represent common real-world adversarial scenarios that account for the difficulty and cost of at-scale compromises.
