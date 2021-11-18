import csv
import sys
from my_Building import Building
from my_call import Call
from my_Elevator import Elevator
class IDError:
    pass

def difference(last_call_time, last_call_src, call, elev:Elevator):
    temp=-1
    time=float(call.call_time)-float(last_call_time)
    dist=abs(float(call.src)-float(last_call_src))
    if(dist/elev.speed > time):
        temp = elev.id
    return temp

def read(calls,building):
    call = []
    with open(calls, "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if ((int(row[2]) < building.min_flor) or (int(row[2]) > building.max_flor)) or ((int(int(row[3]) < building.min_flor) or (int(int(row[3]) > building.max_flor)))):
                raise Exception("call out of bound")

            call.append(Call(row))
        return call

def write(output,call):
    with open(output, "w",newline="") as ansfile:
        writef = csv.writer(ansfile)
        for i in call:
            writef.writerow(i)


def max_call(building: Building):
    max = 0
    max_id = 0
    for i in building.elevators:
        if (max < i.count_call):
            max_id = i.get_id()
            max = i.count_call

    return max_id

def min_call(building: Building):
    min=sys.float_info.max
    min_id=0

    for i in building.elevators:
        if (min > i.count_call):
            min_id = i.get_id()
            min = i.count_call
    return min_id

def Ex1(building, calls, output):
    b = Building(building)
    call = read(calls,b)
    all_calls = []
    for i in call: # here i get a call and can start working on it
        min_lode = sys.float_info.max
        id_lode = 0
        min_time = sys.float_info.max
        min_id = -1
        for e in b.elevators:

            if(e.sum_lode() < min_lode):
                id_lode = e.get_id()

            if(float(e.endTime) <= float(i.call_time)):
                if(e.cost_call(i) < min_time):
                    min_time=e.cost_call(i)
                    min_id=e.get_id()

        # if(b.elevators[min_id].sum_lode() > b.elevators[id_lode].sum_lode()):
        #     min_id = id_lode
        if(b.elevators[min_call(b)].count_call + (len(call)*0.1) < b.elevators[max_call(b)].count_call):
            min_id = min_call(b)
        if(min_id == -1):
            min_id = id_lode

        b.elevators[min_id].last_call_time=i.call_time
        b.elevators[min_id].update_for_call(i)
        i.allocate(min_id)
        all_calls.append(i.get_row())
    write(output,all_calls)

if __name__ == '__main__':
    # Ex1("B"+a+".json","Calls_"+b+".csv","out.csv")
    Ex1(sys.argv[1], sys.argv[2], sys.argv[3])
    # Ex1("B5.json", "Calls_b.csv", "out.csv")






