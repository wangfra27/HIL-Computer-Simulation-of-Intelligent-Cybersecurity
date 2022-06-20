[Link to Article](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/NDSS_2022/Get%20a%20Model!%20Model%20Hijacking%20Attack%20Against%20Machine%20Learning%20Models.pdf)

# Main Problem that is Being Tackled
Machine Learning is becoming increasingly widespread with a variety of critical applications. Because of this, multiple attack models have surfaced. One type of such attack is 'training time attack', whereby an adversary executes their attack before or during the machine learning model training. This article highlights these security concerns and introduces "Model Hijacking Attack," a new training time attack against computer vision based machine learning models. To this end, the article introduces two different Model Hijacking Attacks: Chameleon and Adverse Chameleon.

## Methodology
In order to perform a model hijacking attack, the adversary only needs to be able to poison the target model's training dataset. One problem, however, is that the original dataset and the hijacked datasets can be significantly different and thus easy to be detected. Thus, there are two requirements for a successful model hijacking attack. First, having good performance when predicting any sample from the original dataset with respect to the original task, and predicting any sample from the hijacking dataset with respect to the hijacking task. Second, the execution of the attack should be stealthy (e.g., camouflaged). 

### Camouflager
In order to implement the two attacks stated above, the Camouflager is proposed. The Camouflager is a encoder-decoder based model that camouflages samples in a hijacking dataset to be more stealthy. The model has two encoders, the first one encodes samples from the hijacking dataset and the other from the dataset that the adversary wants the hijacking dataset to be visually similar to. The outputs of the two encoders are then fed into a decoder which outputs the camouflaged sample.

## Chameleon
The Chameleon Attack utilizes two different losses to train the Camouflager: a Visual Loss which is responsible for making the hijacked dataset look visually similar to the target dataset and Semantic Loss which makes the camouflaged sample be semantically similar to the hijacking samples. To hijack a target model, the Chameleon Attack camouflages a hijacking sample using the Camouflager, queries the camouflaged dataset to the hijacked model,

## Adverse Chameleon


