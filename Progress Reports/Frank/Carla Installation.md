# CARLA Installation
Note: This is for Ubuntu 18.04
## Prerequisites:
The Unreal engine build takes about 95 GB, and the Carla build takes about 20 GB. These values can fluxuate as Carla is run, as Carla generates a lot of temp files while running. Reserveing 130 GB total for the entire build should be sufficient. 
Installations through apt-get:
```
sudo apt-get install build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git clang
```
Install Distro from PyPI:
```
pip3 install distro
```
Install [Vulkan Drivers](https://linuxconfig.org/install-and-test-vulkan-on-linux):
```
sudo add-apt-repository ppa:oibaf/graphics-drivers
sudo apt update
sudo apt upgrade
apt install libvulkan1 mesa-vulkan-drivers vulkan-utils
```
## Install the modified version of Unreal Engine 
```
git clone --depth 1 -b carla https://github.com/CarlaUnreal/UnrealEngine.git ~/UnrealEngine_4.26
cd ~/UnrealEngine_4.26
./Setup.sh && ./GenerateProjectFiles.sh && make
```
If you need to verify that the installation is correct:
```
cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor
```

### Build Carla
This can be done concurrently with the Unreal Engine install
```
sudo apt-get install aria2
git clone https://github.com/carla-simulator/carla
cd carla
./Update.sh
```

### Running Carla
```
export UE4_ROOT=~/UnrealEngine_4.26
make PythonAPI
make launch
```
Carla will compile a lot of shaders the first time it is run. It is most optimal to leave the launched CARLA for a bit to compile all of these. This process should take about half an hour. 

After terminating a python script in Python, sometimes the process is not killed automatically, returning an error message about the rbc server being busy. Run the following command: 
```
pkill -9 python
```

Installing Tensorflow: 
The currently installed version of Pytorch is 1.9.0+cu111 and Tensorflow is 20.8. These are the specific versions that are compatible with Cuda on the computer and any other versions of Pytorch or Tensorflow will probably not work. 
