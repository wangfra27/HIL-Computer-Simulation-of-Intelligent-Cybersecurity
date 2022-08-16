# Setup Document for Gym
### Siddhant Patil - 8/16/2022
### The following document contains instructions to setup Gym for both Linux and Windows
---
# Windows
## Prerequisites:
* It is assumed you have Python installed. Python 3.9 is preferred.
### Visual Studio
If you do not have Visual C++ build tools:
* go to [this link](https://visualstudio.microsoft.com/downloads/) and install the latest stable release for Windows.
* open the installer
* check the "Desktop Development with C++" box
* click install

### Miniconda
We will be using Miniconda for this installation. Miniconda is a distribution of Conda similar to Anaconda.
* If you are using Python 3.9 you can use [this link](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86_64.exe) to download the corresponding Miniconda installer. If you are not using Python 3.9, go to [this link](https://docs.conda.io/en/latest/miniconda.html) and install the corresponding Miniconda installer for your Python version.
* open the installer
* run through all the prompts
* once the installation is complete, search "Anaconda Prompt" in the Windows search box and open it

if the command 
```
conda list
```
runs succesfully, you have succesfully installed Miniconda!

## Installation:
We are going to create a conda virtual environment specifically for Gym named "gym"

run the following commands
```
conda create --name gym
conda activate gym
```
then
```
conda install -c conda-forge gym-all
```
if you want to work with atari environments, run this command after
```
pip install ale-py autorom[accept-rom-license]
```
# Linux
## Prerequisites:
* Python 3.9 is the recommended version
### Miniconda
* go to [this link](https://docs.conda.io/en/latest/miniconda.html) and install the latest Miniconda installer package for Linux that fits your system.
* open a terminal
* run the commands below
```
cd Downloads
//insert your specific installer file in below if it is different
chmod u+x ./Miniconda3-py39_4.12.0-Linux-x86_64
./Miniconda3-py39_4.12.0-Linux-x86_64
```
* answer yes to any prompts that show up
* close the terminal and then open a new one
* run the following command
```
conda config --set auto_activate_base false
```
* close the terminal and open a new one
* run the following command
```
conda list
```
If it works then you have succesfully installed Miniconda.

## Installation:
We are going to create a conda virtual environment specifically for Gym named "gym"

run the following commands
```
conda create --name gym
conda activate gym
```
then
```
conda install -c conda-forge gym-all
```
if you want to work with atari environments, run this command after
```
pip install ale-py autorom[accept-rom-license]
```
