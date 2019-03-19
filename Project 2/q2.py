# Team ID: <TODO: fill up>

def schedule2(locations, start_location, capacities, orders):     
    # TODO: replace the code in this function with your algorithm

    #This dumb model solution does not make use of locations
    #However, to optimize your total traveling distance, you must use locations' information
    
    max_list = []
    
    for i in range(len(capacities)):
        max_list.append([])
        
    for i in range(len(orders)):
        weight = orders[i][1]
        for k in range(len(capacities)):
            if capacities[k] >= weight:
                max_list[k].append(orders[i])
                capacities[k] -= weight
                weight = 0
                break
        if weight > 0:
            #print("Wrong input. Cannot deliver this item: ")
            #print(orders[i])
            return []
            
    return max_list

  
