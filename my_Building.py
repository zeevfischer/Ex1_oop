import json
from my_Elevator import Elevator
class IDError:
    pass
class B:
    def __init__(self,file_name):
        with open(file_name,"r") as f:
            self.elevators = []
            my_B = json.load(f)
            self.min_flor = my_B["_minFloor"]
            self.max_flor = my_B["_maxFloor"]
            for data in my_B["_elevators"]:
                Elev = Elevator(data)
                self.elevators.append(Elev)

    def minF(self):
        return self.min_flor

    def maxF(self):
        return self.max_flor

