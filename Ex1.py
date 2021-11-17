import csv
import sys
from my_Bilding import B
from my_call import Call
from my_Elevator import E
class IDError:
    pass

def set_state_by_call(elev: E,call:Call):
    if(call.src < call.dest):
        elev.status = 1  #up
    if (call.src > call.dest):
        elev.status = -1  # up

def on_root(elev: E,call:Call):
    id = -2
    if (elev.calls_dest.empty()):
        return elev.id

    if ((int(call.src) < int(call.dest)) and (int(elev.state) == 1)):
        for i in elev.calls_dest:
            if(i < call.dest):
                if (elev.last_call_time + elev.cost_location(call.src) > call.call_time):
                    id= elev.id

    if ((call.src > call.dest) and (elev.state == -1)):
        for i in elev.calls_dest:
            if(i > call.dest):
                if(elev.last_call_time+elev.cost_location(call.src)>call.call_time):
                    id= elev.id
    return id

def locate(time,Bilding:B):
    for e in Bilding.elevators:
        if(e.state == 1 and e.startTime <= time):
            e.cur_locatiion += e.speed
            if(e.cur_locatiion >= e.dest):
                e.cur_locatiion = e.updet_location()
                e.startTime =time+e.stopTime

        if(e.state == -1 and e.startTime<= time):
            e.cur_locatiion -= e.speed
            if(e.cur_locatiion <= e.dest):
                e.cur_locatiion = e.updet_location()
                e.startTime = time+e.stopTime
        if(e.calls.empty()):
            e.dest=0

def difference(last_call_time,last_call_src,call,elev:E):
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
            if ((int(row[2]) < building.min_flor) and (int(row[2]) > building.max_flor)) or ((int(int(row[3]) < building.min_flor) and (int(int(row[3]) > building.max_flor)))):
                raise Exception("call out of bound")

            call.append(Call(row))
        return call

def write(output,call):
    with open(output, "w",newline="") as ansfile:
        writef = csv.writer(ansfile)
        for i in call:
            writef.writerow(i)

def Ex1(bilding,calls,output):
    b = B(bilding)
    call = read(calls,b)
    all_calls = []
    last_call_time=0
    last_call_src=0
    for i in call: # here i get a call and can start working on it
        min_lode = sys.float_info.max
        id_lode = 0
        min_time = sys.float_info.max
        min_id = -1
        for e in b.elevators:
            # if(difference(last_call_time,last_call_src,i,e) != -1):
            #     min_id=difference(last_call_time,last_call_src,i,e)

            if(e.sum_lode() < min_lode):
                id_lode = e.get_id()

            if(float(e.endTime) <= float(i.call_time)):
                if(e.cost_call(i) < min_time):
                    min_time=e.cost_call(i)
                    min_id=e.get_id()
        if(min_id == -1):
            min_id = id_lode

        # last_call_src=i.src
        # last_call_time=i.call_time
        # set_state_by_call(b.elevators[min_id],i)
        b.elevators[min_id].last_call_time=i.call_time
        b.elevators[min_id].update_for_call(i)
        i.allocate(min_id)
        all_calls.append(i.get_row())
    write(output,all_calls)

if __name__ == '__main__':
    # a=input(str)
    # b=input(str)
    # Ex1("B"+a+".json","Calls_"+b+".csv","out.csv")
    Ex1("B1.json", "Calls_d.csv", "out.csv")
    # Ex1("B2.json", "Calls_a.csv", "out.csv")
    #
    # Ex1("B3.json", "Calls_a.csv", "out.csv")
    # Ex1("B3.json", "Calls_b.csv", "out.csv")
    # Ex1("B3.json", "Calls_c.csv", "out.csv")
    # Ex1("B3.json", "Calls_d.csv", "out.csv")

    # Ex1("B4.json", "Calls_a.csv", "out.csv")
    # Ex1("B4.json", "Calls_b.csv", "out.csv")
    # Ex1("B4.json", "Calls_c.csv", "out.csv")
    # Ex1("B4.json", "Calls_d.csv", "out.csv")

    # Ex1("B5.json", "Calls_a.csv", "out.csv")
    # Ex1("B5.json", "Calls_b.csv", "out.csv")
    # Ex1("B5.json", "Calls_c.csv", "out.csv")
    Ex1("B5.json", "Calls_d.csv", "out.csv")





