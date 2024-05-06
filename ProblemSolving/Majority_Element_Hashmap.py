def majorityElement(arr):
    n = len(arr)
    m = {}

    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    for key in m:
        print(key)
        if m[key] > n // 2 :
             return key ,m 
        

arr = list(map(int,input().rstrip().split()))
print(majorityElement(arr))