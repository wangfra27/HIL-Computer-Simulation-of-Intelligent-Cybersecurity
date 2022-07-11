# Progress Report 6
## Accomplishments
  * I was able to write and run python code that compiled data from each of the availiable sensors on the Carla ego vehicle, allowing us to examine what kind of data can be drawn and used, and the rates that they are gathered at, while also verifying that everything works as intended. 
  * I also ran into a problem with disk space on the Linux system while installing dependencies for LAV. I experimented with migrating Carla to the Extra SSD. The files for Unreal Engine 4 should be able to be stored on the Extra SSD. If there are further problems with disk space, we should be able to use [GParted](https://gparted.org/) to partition more space for Linux at the expense of Windows. 

I examined various self driving algorithms to examine their viability on our installed Carla

### Deep Reinforcement Learning
A [deep reinforcement learning algorithm](https://github.com/Luca96/carla-driving-rl-agent) that trained an autonomous driving agent using the PPO algorithm. This code works on our computer, but runs at 3 frames per second, making it unlikely to be viable for experiementation. I spent time trying to increase the frames by making the code less intensive for the computer, but had no success. 

### LBC/LAV
Learning by Cheating and [Learning from All Vehicles](https://github.com/dotchen/LAV) are two self-driving algorithms developed by the same team, with Learning from All Vehicles being based off of Learning by Cheating. LAV is currently placed third on the Carla Leaderboards for best sensor based autonomous driving algorithms. (First and Second have not released their code to the public yet). LAV considers that the majority of driving algorithms fail on the plethora of edge cases that are impossible for researchers to code in manually or for researchers to simulate for algorithms to learn off of. As such, the algorithm examines and maps out trajectories for all vehicles near it, allowing it to learn from the experiences of other vehicles while also practicing movement prediction for the other cars on the road. 

This algorithm is very promising, and I am still in the process of getting a working model. 

## Problems
  * While installing LAV, I found that the current version of Cuda on the computer is 9.1, which wasn't compatible with PyTorch, which is used by LAV. Upgrading Cuda to a compatible version runs the risk of breaking existing Nvidia Drivers, which seem to rely on Cuda. 
