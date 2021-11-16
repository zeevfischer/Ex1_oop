import csv
import json
import random
import sys

from my_Elevator import E
from my_Bilding import B
from my_call import Call
from random import randint,seed
class IDError:
    pass

# def location(bilding,elev)

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
            # frist = bool(True)
            # # this is not the firt call
            # if(frist != True):
            #     print()
            min_time = sys.float_info.max
            min_id = 0
            if ((int(i.src) >= b.min_flor) and (int(i.dest) <= b.max_flor)) or ((int(i.src) >= b.min_flor) and (int(i.dest) <= b.max_flor)):
                for e in b.elevators: # run on elevators to see witch one is better
                #     # if (e.calltime(i) < temp_time):
                #     #     temp_time = e.calltime(i)
                #     #     temp_id = e.get_id()
                # temp_id=random.randrange(0,len(b.elevators),1)


                    # temp_location=e.location
                    temp_time=e.cost_call(i)
                    if(temp_time < min_time):
                        min_time=e.cost_call(i)
                        min_id=e.get_id()


                e.update_for_call(i)
                i.allocate(min_id)
                writef.writerow(i.get_row())

if __name__ == '__main__':
    Ex1("B3.json","Calls_b.csv","out.csv")

