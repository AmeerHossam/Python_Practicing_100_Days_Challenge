def countingSort(arr,n):

    max_value = max(arr)
    print(max_value)
    new_array = [0]*(max_value+1)
    sorted_array = [0]*n


    for i in range(0,n):
        new_array[arr[i]]+=1
    
    # for y in range(1,max_value+1):
    #     new_array[y] += new_array[y-1]
    # m = n - 1

    # while m >= 0:
    #     sorted_array[new_array[arr[m]] -1] = arr[m]
    #     new_array[arr[m]] -=1
    #     m -= 1
    print(new_array)
n = int(input().strip())

arr = list(map(int,input().rstrip().split()))

countingSort(arr,n)

