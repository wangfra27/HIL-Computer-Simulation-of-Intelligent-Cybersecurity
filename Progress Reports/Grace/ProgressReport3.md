# Progress Report 3
## Accomplishments
  * Learned to use a yaml file
  * Became familiar with Jupyter Notebooks
  * Successfully integrated Mario environment with PPO from Stable-Baselines3
  ```
 # Import Mario Environment
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
# Import Frame Stacker Wrapper and GrayScaling Wrapper
from gym.wrappers import GrayScaleObservation
# Import Vectorization Wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
# Import PPO from Stable-Baselines
from stable_baselines3 import PPO
```
  
## Complications/Issues
  * Could not install all dependencies from environment.yml file. This was due to some packages not being compatible with Macbook.
  * Ran into issue where gym_super_mario_bros command could not compile. I ended up deleting the assertions from the source file and it seemed to at least result in a temporary fix.
  
## Future Goals
  * Become more familiar with AirSim and Carla
