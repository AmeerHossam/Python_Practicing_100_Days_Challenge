def diagonalDifference(arr):
    length = len(arr)
    counter = 0
    reverse_counter=length-1
    rhs=0
    lhs=0
    for i in arr:
        # print(i[counter])
        lhs=lhs+i[counter]
        counter += 1
    for y in arr:
        # print(y[reverse_counter])
        rhs = rhs + y[reverse_counter]
        reverse_counter -= 1
    absolute_value = abs(rhs-lhs)
    print(absolute_value)
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().rstrip().split())))

diagonalDifference(arr)