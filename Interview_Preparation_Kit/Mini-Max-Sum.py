def miniMaxSum(arr):
    length = len(arr)
    sorted_list = sorted(arr)
    print((sorted_list[:length-1]))
    print(sorted_list[-(length-1):])
    min_value = sum(sorted_list[:length-1])
    max_value = sum(sorted_list[-(length-1):])

    print(min_value, max_value)
arr = list(map(int,input().rstrip().split()))

miniMaxSum(arr)