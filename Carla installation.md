# Carla Installation
When installing Carla, there are three more dependencies not mentioned to install.
Clang: 
```
sudo apt-get install clang
```
Distro from PyPI: 
```
pip3 install distro
```
[Vulkan Drivers](https://linuxconfig.org/install-and-test-vulkan-on-linux): 
```
sudo add-apt-repository ppa:oibaf/graphics-drivers
sudo apt update
sudo apt upgrade
apt install libvulkan1 mesa-vulkan-drivers vulkan-utils
```

## Running Carla
To run Carla run the following sequence of commands
Set the environment variable (I haven't set the environment variable to persist across sessions yet)
```
export UE4_ROOT=~/UnrealEngine_4.26
```
Launch Server in Carla folder: 
```
make launch
```
To run Python scripts on Carla, first start the simulation by hitting play, then open a new terminal to run the code.

## Running Px4 
Run QGroundControl.AppImage: 
```
./QGroundControl.AppImage
```

Run the desired simulator: 
```
make px4_sitl jmavsim
```
or
```
make px4_sitl gazebo
```
