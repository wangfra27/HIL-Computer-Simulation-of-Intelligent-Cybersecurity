# What I have done:
* I managed to figure out how to get custom weather to work. It is very configurable. Use the example script environments.py within the util folder. 
* Generating traffic is also very configurable. Use generate_traffic.py.
* Found some very useful documentation: I highly recommend going through [this](https://carla.readthedocs.io/en/latest/tuto_G_retrieve_data/) article thoroughly
* Cloned the Openpilot repository
* Added a new folder called 'Custom Scripts' to PythonAPI folder in carla
* Added two custom scripts: ego.py and replay_recording.py
* ego.py does work but as of now replay_recording.py does not
* In order to run the script open the carla simulator and press play, then in a separate terminal run the python file (e.g., python3 ego.py)
* I managed to get a recording (as in a log file) of me manually driving the car. I used the start_recording.py file from the examples in order to do this. I have gotten a log file (named "test1.log" that is in carla\Unreal\CarlaUE4\Saved) but it is not able to be properly parsed by normal means. I have not yet tried replaying the recording using start_replaying.py.
* Using ego.py it seems to run a car using a predetermined ai model and then prints out a plethora of information in the terminal (e.g., collisions, lane crossings, etc.)

# Problems/Ongoing
* Currently I am trying to get the Openpilot bridge to work. I start by pressing play in carla and then run the bridge.py script in a separate terminal. It seems the script cannot properly import the carla module although the scripts I listed above can. I believe I have found the fix in [this](https://www.pythontutorial.net/python-basics/python-module-search-path/) article but I did not have enough time to verify. 
