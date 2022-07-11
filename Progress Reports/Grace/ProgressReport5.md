# Progress Report 5
## Accomplishments
  * I was succesfully able to produce a hyperrealistic demo of Vista using car sensors. 
  * I was able to spawn multiple cars in a hyperrealistic simulation.
  * I found documentation of deep learning in Vista and its relation to Carla, although I have yet to carefully read it through. 
## Complications/Questions
  * Spawning multiple cars places them on top of each other, which trivializes the simulation
  * In attempt to fix this issue, I used code from the Vista github but I ran into another issue: I need to have a directory to a "mesh", which I cannot find information on. It seems to be an .obj file that will be converted via Vista, however, I have not found such a file with the given documentation. 
  * The simulator, although promising, still seems to have some missing info, or unavailable to the public. 
  
## Next Goals
  * Start to try to integrate OpenAI baselines with Vista, see if it is compatible with Carla
