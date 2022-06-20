# Progress Report 3
## Accomplishments
  * Learned to use a yaml file
  * Became familiar with Jupyter Notebooks
  * Successfully integrated Mario environment with PPO from Stable-Baselines3

Import Mario gym environment by installing gym_super_mario_bros. Nes_py is used to emulate the environment by imitating controls from a NES joypad, essentially giving the model a range of actions.
```
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
```
The next step is to vectorize the environment, meaning we can train the the agent on multiple environments per step. For more information, look [here](https://stable-baselines.readthedocs.io/en/master/guide/vec_envs.html). We will also be using Stable-Baselines3 PPO implementation to train the model.

```
from gym.wrappers import GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from stable_baselines3 import PPO
```
We set up the environment:
```
# 1. Create the base environment
env = gym_super_mario_bros.make('SuperMarioBros-v0')
# 2. Simplify the controls
env = JoypadSpace(env, SIMPLE_MOVEMENT)
# 3. Grayscale
env = GrayScaleObservation(env, keep_dim=True)
# 4. Wrap inside the Dummy Environment
env = DummyVecEnv([lambda: env])
# 5. Stack the frames
env = VecFrameStack(env, 4, channels_order='last')
```
We can then start training the model:
```
model = PPO('CnnPolicy', env, verbose=1, learning_rate=0.000001, n_steps=512)
model.learn(total_timesteps=500000)
model.save('Mario_model1')
model.load('Mario_model1')
```
The hyperparameters can be adjusted according to the desired speed and timeframe of the model. For example, the total_timesteps can be reduced to adjust the amount of time the model will be trained. Note that the training may take several hours depending on the timesteps.

Finally, we can run this trained model on the environment and visualize how it performs.
```
state = env.reset()
while True:
    action = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()
```
When comparing this to the raw environment where the model does random actions, the model does not know where to go and jumps randomly from left to right or stays in place. However, after training we clearly see that the model is driven by a reward, that is to go as far right as fast as possible. 

## Complications/Issues
  * Could not install all dependencies from environment.yml file. This was due to some packages not being compatible with Macbook.
  * Ran into issue where gym_super_mario_bros command could not compile. I ended up deleting the assertions from the source file and it seemed to at least result in a temporary fix.
  
## Future Goals
  * Become more familiar with AirSim and Carla
