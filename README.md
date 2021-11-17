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
class mian.  

### Link,Results,class description
