def removeElement(arr,il):
    length = len(arr)
    new_list = []
    for i in range(0,length):
        if arr[i] != il :
            new_list.append(arr[i])
    
    new_length = len(new_list)
    arr = new_list
    return f"{new_length}, {arr}"






il = int(input())
arr = list(map(int,input().strip().split()))

print(removeElement(arr,il))