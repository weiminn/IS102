# do NOT submit this file
import numpy as np
import copy
import utilities as util
import q1

# change these values to vary the test case
START = "GUA"  # ensure that the START location is not found in ORDER_FILE          
NUM_TRUCKS = 3
LOCATIONS_FILE = "data\locations_1.csv" 
ORDER_FILE = "data\order_1.csv"

orders = util.read_order(ORDER_FILE)
orders_copy = copy.deepcopy(orders)
#print("Orders :" + str(orders))
locations = util.read_location(LOCATIONS_FILE)

# call your function
result = q1.schedule1(locations, START, NUM_TRUCKS, orders_copy)

print("START : " + START + ", NUM_TRUCKS : " + str(NUM_TRUCKS))
print("Your algorithm returned the following schedules:")
for schedule in result:
    print(schedule)
print()

# check if result returned by schedule1() is valid 
err_msg = util.check_validity_q1(orders, result, NUM_TRUCKS)
if err_msg != "":
    print("Result is not valid")
    print(err_msg) 
    exit()
    
locmap = util.read_map(LOCATIONS_FILE)

#Compute shortest distance between START and any delivery location, between any 2 delivery location
fulldest = {}
compact = [START]

for order in orders:
    compact.append(order[2])
    
for node in compact:
    distance = util.dijkstra(node, locmap)
    fulldest[node] = {}
    for tem in compact:
        fulldest[node][tem] = distance[tem][1]
max_travel_time = 0

for i in range(len(result)):
    path = result[i]
    travel_time = 0
    src = START
    for k in range(len(path)):
        dst = path[k][2]
        travel_time += fulldest[src][dst]
        src = dst
    travel_time += fulldest[src][START]
    print("travel time for truck " + str(i+1) + ": " + str(travel_time))
    if travel_time > max_travel_time:
        max_travel_time = travel_time
        
print("Max travel time (lower is better): " + str(max_travel_time))