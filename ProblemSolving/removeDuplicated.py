def removeDuplicates(nums):
    nums.sort()
    k = 0
    for i in range(0,len(nums)):
        if i < len(nums)-1:
            # if nums[i] in nums:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                print(i)
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                print(i)
    return len(nums)
    # p = 0
    # q = 1
    # while q < len(nums):
    #     if nums[q] != nums[p]:
    #         nums[p+1] = nums[q]
    #         p+=1
    #     q+=1
    # return p+1
    # unique_nums = []

    # for num in nums:
    #     if num not in unique_nums:
    #         unique_nums.append(num)

                
    # return unique_nums




n = int(input("Enter the length of the list >> "))
nums =[]
for _ in range(n):
    nums += list(map(int,input().split()))

print(removeDuplicates(nums))