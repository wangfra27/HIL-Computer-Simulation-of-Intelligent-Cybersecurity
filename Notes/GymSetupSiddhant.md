# Setup Document for Gym
### Siddhant Patil - 8/16/2022
### The following document contains instructions to setup Gym for both Linux and Windows
---
# Windows
## Prerequisites:
* It is assumed you have Python installed. Python 3.9 is preferred.
### Visual Studio
If you do not have Visual C++ build tools:
* Go to [this link](https://visualstudio.microsoft.com/downloads/) and install the latest stable release for Windows.
* Open the installer
* Check the "Desktop Development with C++" box
* Click install

### Miniconda
We will be using Miniconda for this installation. Miniconda is a distribution of Conda similar to Anaconda.
* If you are using Python 3.9 you can use [this link](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86_64.exe) to download the corresponding Miniconda installer. If you are not using Python 3.9, go to [this link](https://docs.conda.io/en/latest/miniconda.html) and install the corresponding Miniconda installer for your Python version.
* Open the installer
* Run through all the prompts
* Once the installation is complete, search "Anaconda Prompt" in the Windows search box and open it. The following commands will be run in this terminal.

If the following command runs succesfully, you have succesfully installed Miniconda. 
```
conda list
```

## Installation:
We are going to create a conda virtual environment specifically for Gym named "gym"

Run the following commands within the Anaconda Prompt.
```
conda create --name gym
conda activate gym
```
Then run the following command to install Gym.
```
conda install -c conda-forge gym-all
```
If you want to work with Atari environments, run this command after the previous one.
```
pip install ale-py autorom[accept-rom-license]
```
In addition, run this command to install Stable Baselines 3.
```
conda install -c conda-forge stable-baselines3
```
## Quick Start
* Open an IDE of your choice
* Create a new project
* Make sure to import matplotlib.pyplot and gym modules
* Create a new script file and copy-paste the following code into it
```
import gym
import matplotlib.pyplot as plt
env = gym.make('MountainCar-v0')
import time

obs = env.reset()

for step in range(1500):
    # take random actions
    action = env.action_space.sample()
    
    # apply the action
    obs, reward, done, info = env.step(action)

    # Render the env
    env.render()

    # Wait a bit before the next frame
    time.sleep(0.001)

    # If the episode is up, then start another one
    if done:
        env.reset()

# Close the env
env.close()
```
The code above does not use any sort of algorithm to improve itself, instead it just samples a random action from all possible actions. The following code utilizes a reinforcement learning algorithm called PPO (Proximal Policy Optimization). The code uses [StableBaselines3](https://github.com/DLR-RM/stable-baselines3), so make sure to import it properly. We also need to install some more packages.

* Open Anaconda Prompt
* Run the following commands
```
activate gym
conda install swig
pip install box2d-py
```
Now that those packages are installed, make sure they are properly imported into any IDE you are using. 
Now create a new script file and copy-paste the following code into it.
```
import gym
from stable_baselines3 import PPO

# Parallel environments
#env = make_vec_env("LunarLander-v2", n_envs=8)

# Create environment
env = gym.make('LunarLander-v2')

# Instantiate the agent
model = PPO('MlpPolicy', env, verbose=1)
# Train the agent
model.learn(total_timesteps=int(2e6))
# Save the agent
model.save("ppo_lunar2")

# Load the trained agent
#model = PPO.load("ppo_lunar", env=env)

# Enjoy trained agent
obs = env.reset()
for i in range(10000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
    if dones:
        obs = env.reset()
```
# Linux
The following documentation is based around Debian.

## Prerequisites:
* Python 3.9 is the recommended version
### Miniconda
* Go to [this link](https://docs.conda.io/en/latest/miniconda.html) and install the latest Miniconda installer package for Linux that fits your system.
* Open a terminal
* Run the commands below
```
cd Downloads
//insert your specific installer file in below if it is different
chmod u+x ./Miniconda3-py39_4.12.0-Linux-x86_64
./Miniconda3-py39_4.12.0-Linux-x86_64
```
* Answer yes to any prompts that show up
* Close the terminal and then open a new one
* Run the following command
```
conda config --set auto_activate_base false
```
* Close the terminal and open a new one
* Run the following command
```
conda list
```
If it works, you have succesfully installed Miniconda.

## Installation:
We are going to create a conda virtual environment specifically for Gym named "gym"

Run the following commands.
```
conda create --name gym
conda activate gym
```
Then run the following command to install Gym.
```
conda install -c conda-forge gym-all
```
If you want to work with Atari environments, run this command after the previous one.
```
pip install ale-py autorom[accept-rom-license]
```
In addition, run this command to install Stable Baselines 3.
```
conda install -c conda-forge stable-baselines3
```
## Quick Start
We are going to be using Pycharm for these examples, but feel free to use another IDE if you wish.

Make sure to install snap as it will be used to install Pycharm. Run the following commands to install snap.
```
sudo apt update 
sudo apt install snapd 
sudo apt install core 
```
Next, run the following command to install Pycharm Community.
```
sudo snap install pycharm-community --classic
```
Now that you have installed Pycharm, open it up by searching it up in the search bar.

Create a new project for your scripts.

Once your project has been created, click "File" at the top left of your window and then click "Settings".

Find "Python Interpreter" and click it.

Click the plus button.

Search for the following packages and hit install on the bottom left for each of them:
* gym
* stable-baselines3
* matplotlib
* box2d-py
* Box2D

Now close out the window and hit "OK" on the settings window.

Create a new script and copy-paste the following code into it:

```
import gym
import matplotlib.pyplot as plt
env = gym.make('MountainCar-v0')
import time

# Number of steps you run the agent for
num_steps = 1500

obs = env.reset()

for step in range(1500):
    # take random action, but you can also do something more intelligent
    # action = my_intelligent_agent_fn(obs)
    action = env.action_space.sample()

    # apply the action
    obs, reward, done, info = env.step(action)

    # Render the env
    env.render()

    # Wait a bit before the next frame unless you want to see a crazy fast video
    time.sleep(0.001)

    # If the epsiode is up, then start another one
    if done:
        env.reset()

# Close the env
env.close()
```

The code above does not use any sort of algorithm to improve itself, instead it just samples a random action from all possible actions. The following code utilizes a reinforcement learning algorithm called PPO (Proximal Policy Optimization) from [StableBaselines3](https://github.com/DLR-RM/stable-baselines3).

```
import gym
from stable_baselines3 import PPO

# Parallel environments
#env = make_vec_env("LunarLander-v2", n_envs=8)

# Create environment
env = gym.make('LunarLander-v2')

# Instantiate the agent
model = PPO('MlpPolicy', env, verbose=1)
# Train the agent
model.learn(total_timesteps=int(2e6))
# Save the agent
model.save("ppo_lunar2")

# Load the trained agent
#model = PPO.load("ppo_lunar", env=env)

# Enjoy trained agent
obs = env.reset()
for i in range(10000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
    if dones:
        obs = env.reset()
```





