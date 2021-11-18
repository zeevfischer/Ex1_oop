# Ex1 off line algorithm 

### **Explanation** 
---
Written by zeev fischer and liav levi this weeks assignment is optimizing an off-line algorithm to distribute a given list of calls to X amount of elevators in a building
Algorithm

1 first thing we need to do is create new classes that will hold the information we will read from the json fill and csv

2 then we can start reading files, creating a building with elevators, reading calls and locating the best elevator 

3 for each call we first check witch elevator is best for the call. to do so we first need to add our own parameters to the class we just made (a class description is shown below) 

* Lode, lode time -the time cost of all the calls the elevator needs to do
* Location – the location the elevator supposedly is 
* Last call time-saves the time of the call before the current one
* End time- is the time the elevator finishes all its calls  

  * Now first we Calculating the time it will cost each elevator to compleat the call
  * The we can check witch elevator is free or will be free the fastest and will be able to get to the call 
  * For each call we set the location to be the destination of the call and the time to be the call time + its lode
  * Then we check that adding the call will keep a balanced lode on all the elevators
  * Calls can be added on the way of a current call this is not always better but it can happen if needed
     
### My class
---
class Elevatorsv.  
class Building.  
class CallForElevator.  
class Ex1.  

### Link,Results,class description
---
**link to docs Ex1**  
* https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit

**links to articles from Ex0**  
* https://trace.tennessee.edu/cgi/viewcontent.cgi?article=3380&context=utk_chanhonoproj  
* https://www.researchgate.net/publication/220590321_Optimization_of_Group_Elevator_Scheduling_With_Advance_Information  
* https://www.researchgate.net/publication/31597314_Multiobjective_Optimization_in_Elevator_Group_Control  
![צילום מסך 2021-11-18 143459](https://user-images.githubusercontent.com/92921822/142422403-b07f7061-b4a2-484c-811c-d6c230e5a2ca.jpg)
![צילום מסך 2021-11-18 144700](https://user-images.githubusercontent.com/92921822/142422416-62cfaa55-6809-41b2-ad22-896c6d789a04.jpg)


