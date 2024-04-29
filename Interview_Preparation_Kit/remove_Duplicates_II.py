def removeDuplicates(nums):

    nums.sort()
    i = 0
    for num in range(0,len(nums)):
        # if i < len(nums)-1:
            # if nums[i] in nums:
            # if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
            #     nums.remove(nums[i])
        if i < 2 or nums[num] != nums[i - 2]:
            
            nums[i] = nums[num]
            i+=1
    # k = len(nums)

    return i, nums



nums = list(map(int,input().rstrip().split()))

print(removeDuplicates(nums))