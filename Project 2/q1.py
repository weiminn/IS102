# Team ID: 3

def schedule1(locations, start_location, number_of_trucks, orders):   
    # TODO: replace the code in this function with your algorithm
    routes = []

    for i in range(number_of_trucks):
        routes.append([])

    for r in routes:
        r.append(orders[0])
        orders.pop(0)

    i = 0

    while len(orders) != 0:
        s_dist = 0
        shortest = None
    
        for j in range(len(orders)):
            f = None
            if(i >= len(routes)):
                f = routes[i%len(routes)][ len(routes[i%len(routes)])-1 ][2]
            else:
                f = routes[i][len(routes[i])-1][2]

            d = distance( f , orders[j][2], locations)

            if j == 0:
                shortest = orders[j]
                s_dist = d
            else:
                if d < s_dist:
                    shortest = orders[j]
                    s_dist = d

        if(i >= len(routes)):
            routes[i%len(routes)].append(shortest)
        else:
            routes[i].append(shortest)
        orders.remove(shortest)

        i += 1
        
    return routes

def distance(f, t, locations):
    for loca in locations:
        loca = loca.split(',')
        if loca[0] == f and loca[1] == t:
            return int(loca[2])
