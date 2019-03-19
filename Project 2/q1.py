# Team ID: <TODO: fill up>

def schedule1(locations, start_location, number_of_trucks, orders):   
    # TODO: replace the code in this function with your algorithm
  
    #orders: Order ID, Weight, Delivery location
    
    #This simple model solution does not make use of locations
    #However, to optimize your longest traveling time, you should use the information in locations. 
    
    max_list = []
    
    for i in range(number_of_trucks):
        max_list.append([])
        
    for i in range(len(orders)):
        max_list[i%number_of_trucks].append(orders[i])
        
    return max_list