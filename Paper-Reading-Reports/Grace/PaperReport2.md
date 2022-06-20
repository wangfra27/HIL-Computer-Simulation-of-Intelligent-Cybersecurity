# Paper Report #2: Detecting In-vehicle Intrusion via Semi-supervised Learning-based Convolutional Adversarial Autoencoders
## Primary Issue:
In autonomous vehicles, the main method of the in-vehicle communication system is via the controller area network (CAN) bus. 
Although simple and efficient, it leaves room for adverserial attacks due to a lack of encryption/authentication methods. This means an attacker can 
have direct control over the information that a car obtains from the environment by altering its communication. For example, they can control brakes, 
lock doors, or even steer the car, which can lead to dangerous situations. The aim of this study is to use machine learning to train a model to 
differentiate between normal and attack patterns. 

## Methodology
The study uses a semi-supervised deep learning. In other words, the model will be trained on both unlabeled(unsupervised) and labeled data(supervised),
which gives its "semi-supervised" quality. This is so that the model will be able to better trained recognize new threats that may not be known, rather 
than only being able to recognize specific threats. However, there is a higher false-positive rate with this methodology, so the model will also be able 
trained on labeled data to better differentiate between specific normal and attack patterns. Thus, we will have a more optimal threshold to achieve the
best result. 

## Results
The model that the study is compared to other previous models, and it is clear that this model is very competitive with others in identifying known attacks. 

<img width="491" alt="image" src="https://user-images.githubusercontent.com/73855373/174667698-cb06a217-1b17-4d79-a40a-ef162939864b.png">

The F1 score is an indicator of how well the model can accurately make prediction by combining the metrics "precision" and "recall".
Precision: True positives / selected elements
Recall: True positives / relevant elements
In this context, the model's precision is the ratio of correctly labeled adversarial attacks out of total identified advresarial attacks, which includes false positives.
The model's recall is the ratio of correctly labeled adverserial attacks out of all given adversarial attacks. However, what really separates this model from others
is its ability to recognize unknown attacks due to its primarily unsupervised learning. 

## Main Takeaways
  * Combining methods can be beneficial to achieve optimal results. 
  * While it is important to train models on known data, it is at least equally important to train your model so that it can recognize unfamiliar data. In our current project, the drone should have the ability to run successfully in any environment, not just the one that it has been given.
