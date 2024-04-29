def gridChallenge(grid):

    length = len(grid)
    # sorted_array = []
    for i in range(length):
        grid[i] = (sorted(grid[i]))

    # return len(grid)   
    for i in range(length-1):
        for j in range(len(grid[i])):
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                return "NO"
    return "YES"
    
n = int(input().strip())

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)
# s = list(map(str,input().rstrip().split()))

print(gridChallenge(grid))