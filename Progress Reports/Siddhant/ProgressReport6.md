# Problems with Openpilot
Doing some research online, I found two methods online to install Openpilot. One was a [youtube video](https://www.youtube.com/watch?v=cfDLKVRycRA) which used a ubuntu setup script that does not work for Ubuntu 18.04 (which we are currently using). The other computer does not have a Nvidia graphics card so using the other computer is not an option at the moment. As for the [other method](https://github.com/commaai/openpilot/blob/master/tools/sim/README.md), it used a [bridge](https://github.com/commaai/openpilot/blob/master/tools/sim/bridge.py) script that did not work. I would continue working on this but another issue is that Openpilot is not photorealistic. Additionally, I could not find any way to implement outside deep learning algorithms (e.g., stable baselines) through OpenPilot.
# Research on Other Simulators

There were two main simulators I researched into.

### Sim4CV
A Photo-Realistic Simulator for Computer Vision Applications.
Built on top of the Unreal Engine, the simulator integrates full featured physics based cars, unmanned aerial vehicles (UAVs), and animated human actors in diverse urban and suburban 3D environments. Some pros are that it is photorealistic and we can use drones and cars. The environment is also said to be highly customizable.However, there are some cons. First of all, there is no documentation of the software online. Also, in order to get a copy of the simulator we need to email the creators as there is no download link on the website.

![SIM4CV features](https://user-images.githubusercontent.com/52840861/178172233-10fbf2b6-7175-4aab-b25a-a26557c112a8.png)

### Flightmare
[Flightmare](https://www.youtube.com/watch?v=m9Mx1BCNGFU&ab_channel=UZHRoboticsandPerceptionGroup) is a flexible modular quadrotor simulator. Flightmare is composed of two main components: a configurable rendering engine built on Unity and a flexible physics engine for dynamics simulation. Those two components are totally decoupled and can run independently from each other. Flightmare comes with several desirable features: (i) a large multi-modal sensor suite, including an interface to extract the 3D point-cloud of the scene; (ii) an API for reinforcement learning which can simulate hundreds of quadrotors in parallel; and (iii) an integration with a virtual-reality headset for interaction with the simulated environment. Flightmare can be used for various applications, including path-planning, reinforcement learning, visual-inertial odometry, deep learning, human-robot interaction, etc.

![Flightmare](https://user-images.githubusercontent.com/52840861/178174087-10ed05cb-0e28-4120-bd2e-df13a5e50717.png)

##### Pros:
* photorealistic
* opensource and easily downloadable
* [extensive documentation](https://flightmare.readthedocs.io/en/latest/documentation.html)
* very customizable
* compatible with ROS & Gazebo
* compatible with OpenAI Gym (so implementing stablebaselines 3 should be relatively easy)
* realtime data acquisition with a multitude of sensors (e.g., RGB Images, Depth Maps, etc)
* configurable sensor suite (user-defined camera poses and parameters)
* can run multiple agents in parallel
* user-friendly

Some cons however is that it runs on Unity, not Unreal Engine. It also does not simulate things like cars, it only simulates quadroters. However, I believe that compared to Sim4CV this is a much better option. Another thing to take into note is that Unity is only about 4 GB.

![Flightmare 2](https://user-images.githubusercontent.com/52840861/178174201-8f5206d0-90ee-4674-9bce-6de3dc4f9768.png)


# Ongoing
* Researching more into Flightmare

# Next Steps
* Work on installing Flightmare and running simulations. 
