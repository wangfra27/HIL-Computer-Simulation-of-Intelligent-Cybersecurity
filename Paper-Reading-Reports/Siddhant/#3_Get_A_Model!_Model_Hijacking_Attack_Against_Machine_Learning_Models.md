[Link to Article](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/NDSS_2022/Get%20a%20Model!%20Model%20Hijacking%20Attack%20Against%20Machine%20Learning%20Models.pdf)

# Main Problem that is Being Tackled
Machine Learning is becoming increasingly widespread with a variety of critical applications. Because of this, multiple attack models have surfaced. One type of such attack is 'training time attack', whereby an adversary executes their attack before or during the machine learning model training. This article highlights these security concerns and introduces "Model Hijacking Attack," a new training time attack against computer vision based machine learning models. To this end, the article introduces two different Model Hijacking Attacks: Chameleon and Adverse Chameleon.

## Methodology
In order to perform a model hijacking attack, the adversary only needs to be able to poison the target model's training dataset. One problem, however, is that the original dataset and the hijacked datasets can be significantly different and thus easy to be detected. Thus, there are two requirements for a successful model hijacking attack. First, having good performance when predicting any sample from the original dataset with respect to the original task, and predicting any sample from the hijacking dataset with respect to the hijacking task. Second, the execution of the attack should be stealthy (e.g., camouflaged). 

### Camouflager
In order to implement the two attacks stated above, the Camouflager is proposed. The Camouflager is a encoder-decoder based model that camouflages samples in a hijacking dataset to be more stealthy. The model has two encoders, the first one encodes samples from the hijacking dataset and the other from the dataset that the adversary wants the hijacking dataset to be visually similar to. The outputs of the two encoders are then fed into a decoder which outputs the camouflaged sample.

### Chameleon
The Chameleon Attack utilizes two different losses to train the Camouflager: a Visual Loss which is responsible for making the hijacked dataset look visually similar to the target dataset and Semantic Loss which makes the camouflaged sample be semantically similar to the hijacking samples. In addition to training the Camouflager, the Chameleon attack also needs to establish a mapping between labels of the hijacking task and of the original task. To hijack a target model, the Chameleon attack poisons the original dataset using the camouflaged dataset. Finally, to execute the attack, the adversary camouflages a hijacking sample using the Camouflager, queries the camouflaged sample to the hijacked model, and maps the predicted label back to the corresponding on of the hijacking task.

### Adverse Chameleon
One problem with the Chameleon attack is that if the hijacked and the target datasets are relatively similar the Camouflager cannot achieve its expected properties. In response to this flaw, there is the Adverse Chameleon attack. It is a more complicated attack that utilizes an additional loss, named "adverse Semantic Loss", which is meant to distance the semantics/features of the output of the Camouflager from the target dataset.

## Evaluation
#### Datasets Description
In order to evaluate the different model hijacking attacks, three well-established computer vision benchmark datasets were used: MNIST, CIFAR-10, and CelebA. MNIST is a grey-scale handwritten digits classification dataset. It contains 70,000 images each containing a single digit and correspondingly split into 10 classes. CIFAR-10 is a 10 class colored dataset consisting of 60,000 images. CelebA is a dataset of face attributes with more than 200,000 colored images each containing the face of a celebrity in the middle.

### Attack Success Rate

#### Chameleon Attack
![image](https://user-images.githubusercontent.com/52840861/174518497-c8e7173c-3baa-4c2c-9a45-d1dc7bb2f326.png)

We use MNIST as out hijacking dataset and both CIFAR-10 and CelebA as the original datasets fr this attack. We followed the methodology stated for the Chameleon attack stated above. We sampled 1,000 for 8 random classes in the original dataset and sampled 10,000 randomly from the hijacking dataset. We then proceed to follow the methodology stated above to train the Camouflager. After training the Camouflager, we use it together with the same target dataset to camouflage 40,000 randomly sampled samples from the target dataset. We then train the target model with both the camouflage and the original samples.
#### Performance Evaluation
The Chameleon attack achieves 99% accuracy on the original dataset (when original task is CIFAR-10 Classification), 99.5% accuracy on the CelebA classification model. Take into note that this is with a significance difference between the hijacking and the target dataset. 

#### Adverse Chameleon Attack
![image](https://user-images.githubusercontent.com/52840861/174521653-feb38582-a41e-48b6-a1e4-45dea5894571.png)

As stated above, the Chameleon attack only when the hijacking and the target datasets are significantly different. For example, when performing the the Chameleon attack using CIFAR-10 as the original dataset and CelebA as the hijacking dataset it only achieves a success rate of 65.7%. Thus, when considering CelebA and Cifar-10 as the hijacking datasets we would use the Adverse Chameleon Attack.
#### Performance Evaluation
The Adverse Chameleon attack achieved 73.7% accuracy on the CIFAR-10 testing dataset when camouflaging CelebA to hijack CIFAR-10 classification model. For the opposite case, the attack has a 56.8% accuracy. Not great but it is better than guessing. 

## Conclusion
In short, this new type of attack we proposed can cause severe security and accountability risks. Moreover, the hijacked model's owner could be framed for the illegal and unethical task their model is capable of.



# Thoughts
This article has taught me a lot about security risks and ethical concerns related to the coming Machine Learning revolution.
* First experience with many of the mentioned datasets
* Deepened my understanding of Federated Learning

The Adverse Chameleon attack was not particularly great but the Chameleon attack did prove to be quite effective. However, the two attacks as a whole did not feel particularly radical. 

# Future Direction of this Research
There were multiple possible defenses against the model hijacking attack stated within the paper. Though they were quite effective at stopping the attacks, they also lowered the usability of the target model in and of itself. Researching different defense techniques to provide a better trade off would be a good direction to take. 

In the future, the principles behind the Chameleon attack could also be applied in some other case other than just vision based machine learning models. For example, [this paper](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/ACM_CCS_2021/Hidden%20Backdoors%20in%20Human-Centric%20Language%20Models.pdf) on Backdoors in Human-Centric Language Models. Instead of providing carefully crafted trigger sentences, we could use the principles behind the model haijack attack to instead stealthily provide poisoned data to a model while it is training to mess with the model itself.




