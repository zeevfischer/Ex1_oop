from my_call import Call
class E:
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
        self.endTime = float(0)
        # self.total_cost=float(0)
        # self.E_log = []

    def update_for_call(self,call: Call):
        self.location=call.get_dst()
        self.endTime = float(call.call_time) + float(self.cost_call(call))
        self.total_time += float(self.cost_call(call))

    # def update_for_location(self,location:int):
    #     self.location = location
    #     self.endTime += self.cost_location(location)

    def get_id(self):
        return self.id

    # def time_for_call(self, call:Call)-> float:
    #     dist = abs(int(self.finalFloor) - int(call.src)) + abs(int(call.src) - int(call.dest))
    #     time = 2 * self.stopTime + self.startTime + 2 * self.openTime + 2 * self.closeTime
    #     if self.finalFloor != call.src:
    #         time += self.startTime
    #     return dist / self.speed + time

    # the cost off a call from a to b in time
    def cost_call(self,call: Call):
        location_a=abs(int(self.location)-(int(call.src)))
        a_b=abs(int(call.src) - int(call.dest))
        temp=self.closeTime + self.startTime + self.stopTime + self.openTime
        return (a_b/self.speed) + (location_a/self.speed) +temp

    def cost_location(self,location: int):
        a_b=abs(self.location - location)
        return self.closeTime + self.startTime + (a_b/self.speed) + self.stopTime + self.openTime


    # def isState(self, time) -> bool:
    #     if self.endTime == 0:
    #         return True
    #     return (float(time) >= self.endTime)
    #
    # def addCall(self, c):
    #     self.endTime = self.endTime + self.time_for_call(c)
    #     self.finalFloor = c.dest