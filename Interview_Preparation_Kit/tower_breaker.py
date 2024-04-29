def towerBreakers(n,m):

    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1
    

arr = list(map(int,input().rstrip().split()))

n = int(arr[0])
m = int(arr[1])

print(towerBreakers(n,m))