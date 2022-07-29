# Flightmare Installation
Note: This is for Ubuntu 18.04
## Prerequisites
* Make sure git is set up properly
* Flightmare requires CMake and GCC compiler. You will also need system packages python3, OpenMPI, and OpenCV. Run this:

```
apt-get update && apt-get install -y --no-install-recommends \
   build-essential \
   cmake \
   libzmqpp-dev \
   libopencv-dev
```
## Install Flightmare

```
cd ~
git clone https://github.com/uzh-rpg/flightmare.git
```

### Add Environment Variable

```
echo "export FLIGHTMARE_PATH=~/flightmare" >> ~/.bashrc
source ~/.bashrc
```

### Install Dependencies
You will notice that there is no requirements.txt file within the flightmare file, you have to create one using pipreq. If you do not have it installed run

```
pip3 install pipreqs
```
then create the actual requirements.txt file

```
cd flightmare
pipreqs
```
now you need to install these dependencies

```
pip3 install -r requirements.txt
```
now that you have the dependencies installed you want to install Flightmare (flightlib)

```
cd flightmare/flightlib
# it first compiles the flightlib and then installs it as a python package.
pip3 install .
```
## ROS

### Install ROS

we are going to use a ros installer script.

```
cd ~
git clone https://github.com/jetsonhacks/installROS.git
cd installROS
./installROS.sh -p ros-melodic-desktop-full -p ros-melodic-rgbd-launch
```

### Install Gazebo

```
sudo apt-get install gazebo9 *
```

### ROS Dependencies

```
sudo apt-get install libgoogle-glog-dev protobuf-compiler ros-$ROS_DISTRO-octomap-msgs ros-$ROS_DISTRO-octomap-ros ros-$ROS_DISTRO-joy python-vcstool
```
before you proceed run

```
protoc --version
```
to make sure that protoc is version 3.0.0. If not, follow [this guide](https://github.com/linux-on-ibm-z/docs/wiki/Building-ProtoBuf-3.0.0).

## Catkin
Get catkin tools with these commands

```
sudo apt-get install python-pip
sudo pip install catkin-tools
```

then create a catkin workspace with the following commands

```
cd
mkdir -p catkin_ws/src
cd catkin_ws
catkin config --init --mkdirs --extend /opt/ros/$ROS_DISTRO --merge-devel --cmake-args -DCMAKE_BUILD_TYPE=Release
```

now we are going to clone the flightmare repository (yes, we are doing this again). **NOTE: YOU HAVE TO USE SSH, YOU CANNOT USE HTTPS FOR CLONING.** Make sure your SSH key is set up properly to authenticate. Then run the following commands

```
cd ~/catkin_ws/src
git clone git@github.com:uzh-rpg/flightmare.git
```

now clone dependencies

```
vcs-import < flightmare/flightros/dependencies.yaml
```

and build

```
catkin_make
```
now add sourcing of your catkin workspace and FLIGHTMARE_PATH environment variable to your .bashrc file

```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export FLIGHTMARE_PATH=~/catkin_ws/src/flightmare" >> ~/.bashrc
source ~/.bashrc
```

## Download Flightmare Unity Binary

There are a couple concepts you need to understand. Flightmare is based on a server-client model. This unity binary works as the server from which we run scripts (the client) that connect to unity using a bridge. What we are going to install now is the "server" part.

You can download this Unity Binary [here.](https://github.com/uzh-rpg/flightmare/releases/latest/download/RPG_Flightmare.tar.xz)

Extract this to /flightmare/flightrender

### Running an Example

Make sure that unity is not currently running when you run the following command. If it works correctly, you should get a simulation where a drone is flying between some moving gates in the WAREHOUSE environment.

Run the simulation with this command

```
roslaunch flightros racing.launch
```
if you are curious about the different examples you can use the command

```
roscd flightros
```
and explore. There will be a "racing" directory that contains all the examples that you can run.

## Related Links

* [ros commands](http://wiki.ros.org/ROS/CommandLineTools)
* [core concepts of flightmare](https://flightmare.readthedocs.io/en/latest/first_steps/core_concepts.html)
* [flightmare github](https://github.com/uzh-rpg/flightmare)
* [installROS github](https://github.com/jetsonhacks/installROS)
* [pipreqs](https://github.com/bndr/pipreqs)

