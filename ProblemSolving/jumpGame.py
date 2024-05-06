nums = [0,1,2]

def canJump(nums):
    max_index = 0
    for i , num in enumerate(nums):
        if i > max_index:
            return False
        max_index = max(max_index, num+i)
    return True   
print(canJump(nums))