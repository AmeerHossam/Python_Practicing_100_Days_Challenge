def rotate(nums,k):
    j = -1
    new_list = []
    for _ in range(k):
        new_list.insert(0,nums[j])
        j-=1
    for i in range(len(nums)-len(new_list)):
        new_list.append(nums[i])
    nums = new_list
    print(nums)
    
k = int(input())
nums = list(map(int,input().rstrip().split()))

rotate(nums,k)