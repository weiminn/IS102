# do NOT submit this file
import numpy as np
import copy
import utilities as util
import q2

# change these values to vary the test case
START = 'GUA'  # ensure that the START location is not found in ORDER_FILE                              
LOCATIONS_FILE = "data\locations_1.csv" 
ORDER_FILE = "data\order_1.csv"
LOAD_FILE = "data\load_1.csv"


orders = util.read_order(ORDER_FILE)
orders_copy = copy.deepcopy(orders)
#print("Orders :" + str(orders))
capacities = util.read_load(LOAD_FILE)
capacities_copy = copy.deepcopy(capacities)
#print("Loads :" + str(capacities))
locations = util.read_location(LOCATIONS_FILE)

# call your function
result = q2.schedule2(locations, START, capacities_copy, orders_copy)

print("START : " + START + ", NUM_TRUCKS : " + str(len(capacities)))
print("Your algorithm returned the following schedules:")
for schedule in result:
    print(schedule)
print()
    
# check if result returned by schedule2() is valid 
err_msg = util.check_validity_q2(capacities, orders, result)
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
total_travel_distance = 0

for i in range(len(result)):
    path = result[i]
    travel_distance = 0
    src = START
    for k in range(len(path)):
        dst = path[k][2]
        travel_distance += fulldest[src][dst]
        src = dst
    travel_distance += fulldest[src][START]
    print("distance for truck " + str(i+1) + " : " + str(travel_distance))
    total_travel_distance += travel_distance
    
print("Total travel distance (lower is better): " + str(total_travel_distance))