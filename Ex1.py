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
    id = -1
    if ((call.src < call.dest)):
        if (elev.calls.empty()):
            id = elev.id

        for i in elev.calls:
            if(i < call.dest):
                if (elev.last_call_time + elev.cost_location(call.src) > call.call_time):
                    id= elev.id

    elif ((call.src > call.dest)):
        if (elev.calls.empty()):
            id = elev.id

        for i in elev.calls:
            if(i > call.dest):
                if(elev.last_call_time+elev.cost_location(call.src)>call.call_time):
                    id= elev.id
    return id

def locate(time,Bilding:B):
    for e in Bilding.elevators:
        if(e.state == 1 and e.startTime <= time):
            e.cur_locatiion += e.speed
            if(e.cur_locatiion >= e.dest):
                e.cur_locatiion = e.cur_locatiion
                e.startTime =time+e.stopTime

        if(e.state == -1 and e.startTime<= time):
            e.cur_locatiion -= e.speed
            if(e.cur_locatiion <= e.dest):
                e.cur_locatiion=e.cur_locatiion
                e.startTime = time+e.stopTime
        if(e.calls.empty()):
            e.dest=0

def Ex1(bilding,calls,output):
    b = B(bilding)
    # calls reading
    call = []
    with open(calls, "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            call.append(Call(row))

    # calls rewriting and shold be aftee alocat
    with open(output, "w",newline="") as ansfile:
        writef = csv.writer(ansfile)
        for i in call: # here i get a call and can start working on it
            elevs=[]
            min_lode = sys.float_info.max
            id_lode = 0
            min_time = sys.float_info.max
            min_id = -1
            if ((int(i.src) >= b.min_flor) and (int(i.dest) <= b.max_flor)) or ((int(i.src) >= b.min_flor) and (int(i.dest) <= b.max_flor)):
                for e2 in b.elevators:
                    if(on_root(e2,i) != -1):
                        elevs.append(e2)

                for e in elevs:
                    if(e.sum_lode() < min_lode):
                        id_lode = e.get_id()
                    if(float(e.endTime) <= float(i.call_time)):
                        # temp=e.cost_call(i)
                        if(e.cost_call(i) < min_time):
                            min_time=e.cost_call(i)
                            min_id=e.get_id()
                if(min_id == -1):
                    min_id = id_lode


                b.elevators[min_id].calls.append(i.src)
                b.elevators[min_id].calls.append(i.dest)
                set_state_by_call(b.elevators[min_id],i)
                b.elevators[min_id].last_call_time=i.call_time
                b.elevators[min_id].update_for_call(i)
                i.allocate(min_id)
                writef.writerow(i.get_row())

if __name__ == '__main__':
    Ex1("B3.json","my_c.csv","out.csv")

