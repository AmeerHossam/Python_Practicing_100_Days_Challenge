def alternativeSort(arr):
    length = len(arr)
    sorted_arr = sorted(arr)
    counter = 0
    reversed_counter = length - 1
    new_list = []
    for _ in sorted_arr:
        if counter < reversed_counter:
            new_list.append(sorted_arr[reversed_counter])
            reversed_counter -= 1

            new_list.append(sorted_arr[counter])
            counter += 1
    
    print(new_list)


n = int(input().strip())

arr = list(map(int,input().rstrip().split()))
alternativeSort(arr)