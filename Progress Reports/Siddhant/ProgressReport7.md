# Problems with Openpilot
After upgrading the second desktop from Ubuntu 18.04 to Ubuntu 20.04 the setup script did work thankfully. Now the one problem left is that I installed scons using pip3 but it is not being recognized as a command. If I try reinstalling it with pip3 it says that it has already been installed. If I try installing it using apt instead it installs an older version of scons that is recognized as a command but does not work. There is a specific feature in the newer scons that is not in that older version which openpilot requires. I ended up moving on to Flightmare.
# Accomplishments
 * Successfully set up Openpilot
 * Succesfully set up a server for running Flightmare simulations, it runs perfectly on the main desktop

# Ongoing
* Working on setting up a client for the Flightmare simulator

# Next Steps
* Get a client running and start running simulations. 
* Flightmare comes with an OpenAI Gym Python Wrapper so work on implementing Stable Baselines

