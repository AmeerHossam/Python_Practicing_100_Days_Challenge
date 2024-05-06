def majorityElement(arr):
    nums = len(arr)
    maxCount , index = 0,0
    for i in range(nums):
        count = 1

        for j in range(i+1,nums):
            if arr[i] == arr[j]:
                count += 1
        if count > maxCount:
            maxCount = count
            index = i
    if maxCount > nums // 2:
        return arr[index]
    else:
        return "No Majority Element"
arr = list(map(int,input().rstrip().split()))
print(majorityElement(arr))