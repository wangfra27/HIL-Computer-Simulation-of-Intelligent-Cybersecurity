# Progress Report 7
## Accomplishments
My research this week centered on LAV, a self-driving algorithm developed for CARLA. Using their algorithms and datasets, I was able to train and run a self-driving algorithm on the server. The training consisted of 5 parts: 
  * Privileged Motion Planning: A motion planner with privileged information, using ground truth labeling as an input to predict high-level commands and trajectories of the surrounding vehicles. 
  * Semantic Segmentation: The program takes in data from LiDAR and 3 RGB Cameras to produce a 2D map of the surrounding area. This map seperates the pixels on the map into five classes: “background”, “vehicles”, “roads”, “lane markings” and “pedestrians”. 
  * RGB Braking Prediction: The braking is overwritten by the program for traffic lights and hazzard stops. These are identified through the RGB cameras and trained using recorded brake actions. This classifier does have access to the motion planner's output, making decisions based off of predicted movement from the surrounding vehicles. 
  * Point Painting: [LiDAR Point Painting](https://arxiv.org/pdf/1911.10150.pdf) is used to fuse the data from the LiDAR and the RGB Cameras. 
  * Full Model Training: The Full model training is divided into two parts: a pretrained perception model and an end-to-end model. 
    - Perception Pre-training: While this step is not completely necessary, Pretrained models produce driving scores that are almost 6 times better than models without pre-training. This step takes in fully labeled data and uses rotation augmentations to create a robust model for further training. 
    - The final model combines everything into a three stage modular pipeline: a perception module, a motion planner, and a low-level controller that ultimately takes in LiDAR and RGB and outputs commands for steering and acceleration. 

The examplery trained weights provided by the creators of LAV also work nicely. 

## Problems/Future steps
  * continue to look into the exact methods used in the code on the training steps to examine how the trainers are created
  * train a more powerful agent using more of the provided datasets
  * understand the inputs and outputs of each module, look for ways to disrupt/improve the flow of information
