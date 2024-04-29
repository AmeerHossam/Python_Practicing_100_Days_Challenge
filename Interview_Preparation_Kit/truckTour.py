def truckTour(petrolPumps):
    fuel , position = 0,0
    length = len(petrolPumps)
    for i in range(length):
        fuel += petrolPumps[i][0] - petrolPumps[i][1]
        if fuel < 0:
            position = i + 1
            fuel = 0
    return position



petrolPumps=[]
n = int(input().strip())
for _ in range(n):
    petrolPumps.append(list(map(int,input().rstrip().split())))

print(truckTour(petrolPumps))