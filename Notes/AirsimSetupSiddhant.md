# Setup Document for Airsim
### Siddhant Patil - 8/21/2022
### The following document contains instructions on how to setup Airsim for a Windows machine. 
---
## Prerequisites
* A Windows Machine. Windows 10 or 11 is recommended but not required.

## Unreal Engine Setup

1. Download the Epic Games Launcher from [this link](https://www.unrealengine.com/en-US/download).
2. Create an account
3. Once you are in, go to the "Unreal Engine" tab and install version 4.27 from the installation dropdown. **Make sure that you are installing version 4.27 and not another version or Airsim will not work.**

## Visual Studio
1. Install Visual Studio from [this link](https://visualstudio.microsoft.com/downloads/). Choose the latest version. 
> Note: At the time of this document being written the latest version is 2022 so that is the version that will be referenced from now on. Replace 2022 with whatever version you have installed.
2. Open the installer. Select the following options
*  Desktop Development with C++
*  Windows 10 SDK 10.0.19041
*  the latest .NET Framework SDK (this is under the **Individual Components** tab)
3. Start the installation.

## AirSim
1. Open `Developer Command Prompt for VS 2022`
2. Run the following commands:
> Note: It is not a good idea to install Airsim in C drive. This will cause errors. It is recommended to clone in a different drive. The first command that follows changes to a D drive but you can change that to a drive of your choosing.
```
D:
git clone https://github.com/Microsoft/AirSim.git
cd AirSim
build.cmd
```

## Associating Project File Extensions with Unreal Engine
1. Close the Epic Games Launcher window.
1. Open `Task Manager`
2. Scroll through and make sure that there is no task related to the launcher. If there is, click on it and hit "End Task"
3. Now open the launcher again. There should be a popup asking if project file extensions should be associated with Unreal Engine, click yes.

## Quick Start
We will be using a Blocks environment that comes with Airsim.
1. double click on the `Blocks.sln` file located at `AirSim\Unreal\Environments\Blocks`
2. Select your Unreal project as Start Up project (e.g., Blocks project) and make sure Build config is set to "Develop Editor" and x64.
3. After Unreal Editor loads, press the Play button.
4. Hit the Stop button once you are done

### Running a DQN algorithm
1. Press the Play button.
2. Open a new terminal
3. Navigate to the following folder: `AirSim\PythonClient\reinforcement_learning`

If you are currently running a car in your simulation, run the following command:
```
python3 dqn_car
```
If you are currently running a drone in your simulation, run the following command instead:
```
python3 dqn_drone
```
