import random

def station_generate(n,station_lb,station_ub):
    station=[]
    for i in range(n):
        station.append(random.randint(station_lb,station_ub))
    return station

def distance_generate(n,distance_lb,distance_ub):
    distance=[]
    for i in range(n):
        distance.append([0]*n)
    for i in range(n-1):
        for j in range(i+1,n):
            distance[i][j] = distance[j][i] = random.randint(distance_lb,distance_ub)
    return distance

def fuel_generate(n,fuel_lb,fuel_ub):
    fuel=[]
    for i in range(n):
        fuel.append([0]*n)
    for i in range(n-1):
        for j in range(i+1,n):
            fuel[i][j] = fuel[j][i] = random.randint(fuel_lb,fuel_ub)
    return fuel