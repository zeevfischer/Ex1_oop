from my_call import Call
from queue import PriorityQueue

class Elevator:
    def __init__(self, data) -> None:
        self.id = data["_id"]
        self.speed = data["_speed"]
        self.minFloor = data["_minFloor"]
        self.maxFloor = data["_maxFloor"]
        self.closeTime = data["_closeTime"]
        self.openTime = data["_openTime"]
        self.startTime = data["_startTime"]
        self.stopTime = data["_stopTime"]

        self.location = 0
        self.last_call_time=0
        self.endTime = float(0)
        self.lode = []
        self.time_lode = []
    def updet_location(self):
        if not self.calls.empty():
            if self.state == -1:
                self.dest = -1 * self.calls.get()
            else:
                self.dest = self.calls.get()
        else:
            self.state = 0
        return self.dest

    def update_for_call(self,call: Call):
        self.location=call.get_dst()
        self.endTime = float(call.call_time) + float(self.cost_call(call))
        self.lode.append(self.cost_call(call))
        self.time_lode.append(self.endTime)
        self.de_lode(call)

    def update_for_location(self,location:int):
        self.location = location
        self.endTime += self.cost_location(location)

    def sum_lode(self):
        sum = 0
        for i in self.lode:
            sum += i
        return sum

    def de_lode(self,call: Call):
        if (float(call.call_time) > self.time_lode[0]):
            self.lode.pop(0)
            self.time_lode.pop(0)

    def get_id(self):
        return self.id

    # the cost off a call from a to b in time
    def cost_call(self,call: Call):
        location_a=abs(int(self.location)-(int(call.src)))
        a_b=abs(int(call.src) - int(call.dest))
        temp=self.closeTime + self.startTime + self.stopTime + self.openTime
        return (a_b/self.speed) + (location_a/self.speed) +temp

    def cost_location(self,location: int):
        a_b=abs(self.location - location)
        return self.closeTime + self.startTime + (a_b/self.speed) + self.stopTime + self.openTime
