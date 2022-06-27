# Progress Report 4
## Accomplishments
  * Succesfully installed a Linux VM through Parallels
  * Succesfully installed the prerequisites for Vista Simulator through PyPi
  * Read through the [Vista Docs](https://vista.csail.mit.edu/introduction/index.html) and ran simulation

### Vista Simulation
The simulator uses real-life data gathered from outside sources to construct objects called Traces. I constructed a virtual world object World that is built from these Traces. Then I created my agent, a car, and set the specific parameters around it. The display is a tool to create a visualization of this world. 
<img width="855" alt="image" src="https://user-images.githubusercontent.com/73855373/176010607-03c082e1-a83a-4b5e-918b-dc757eec0e3f.png">

I then create two state space controllers in which I could determine the agent's actions: 1) by following human trajectory 
or 2) a pure pursuit controller

Human Trajectory: Uses Traces to imitate how humans drive in the dataset
  
<img width="454" alt="image" src="https://user-images.githubusercontent.com/73855373/176011338-89e5f021-cb74-49eb-bda1-6a7a3bef641e.png">
  
Pure pursuit controller: Computes the angular velocity that moves the agent from its current position to a look-ahead point

<img width="556" alt="image" src="https://user-images.githubusercontent.com/73855373/176011769-476bcc05-9771-44e8-8e86-b16c18d068e5.png">

Afterwards, I can use one of these controllers as the agent's action, and then render the display to visualize what this may look like.

<img width="407" alt="image" src="https://user-images.githubusercontent.com/73855373/176012020-77ad6482-65c0-4f64-92bf-eb90cc9c8dbc.png">

Human Trajectory Visual:
![human](https://user-images.githubusercontent.com/73855373/176015256-1b50f30b-c0ac-4531-8d70-8c3fec0b9a62.gif)

Pure Pursuit Visual:
![pure](https://user-images.githubusercontent.com/73855373/176014753-cf5448fb-8bc7-453e-a126-7134ab95d370.gif)

## Critiques
  * Vista docs are not updated and there are some sections have no content
  * The visualization is very simple and I wish there were more data points so I can easily find the differences between controllers

## Issues
  * I had to constantly free up space beacause the VM was taking up an unanticipated amount of storage
  * After installing Vista, I was unable to import it due to some unknown error where I could not find a solution online
  * I was able to fix issues regarding runtime issues, but the resultimg image does not appear when I attempt to render it
