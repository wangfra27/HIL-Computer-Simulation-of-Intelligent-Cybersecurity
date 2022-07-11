# Progress Report 5
## Accomplishments
  * I was succesfully able to produce a hyperrealistic demo of Vista using car sensors.
  <img width="966" alt="Screen Shot 2022-07-11 at 12 19 33 PM" src="https://user-images.githubusercontent.com/73855373/178317718-5bd647c3-86a6-4d1e-934e-40e751e02c0d.png">

  * I was able to spawn multiple cars in a hyperrealistic simulation.
 <img width="1438" alt="Screen Shot 2022-07-11 at 12 57 56 PM" src="https://user-images.githubusercontent.com/73855373/178317972-0aaa055a-5773-4f55-b6ab-17795d6322fd.png">
  * Tested my code on multiple "maps".
  * I found documentation of deep learning in Vista and its relation to Carla, although I have yet to carefully read it through: https://www.mit.edu/~amini/pubs/pdf/learning-in-simulation-vista.pdf
   
## Complications/Questions
  * Spawning multiple cars places them on top of each other, which trivializes the simulation
  * In attempt to fix this issue, I used code from the Vista github but I ran into another issue: I need to have a directory to a "mesh", which I cannot find information on. It seems to be an .obj file that will be converted via Vista, however, I have not found such a file with the given documentation. 
  * I was successfully able to use RGB cameras, but when I attempt to use the Lidar and event cameras, it appears that I have missing files. 
  * The simulator, although promising, still seems to have some missing info, or unavailable to the public. When I looked at ongoing issues in the Vista github, there are others with the same problems that I am having. 
  
## Next Goals
  * Start to try to integrate OpenAI baselines with Vista, see if it is compatible with Carla
