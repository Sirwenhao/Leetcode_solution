"""
    1、只修改一位的前提下，将数组变为递增数组
"""

# def checkPossibility(nums):
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             nums.remove(nums[i])
#             print("nums:", nums)
#             cnt = 0
#             for j in range(len(nums)-1):
#                 if nums[j] < nums[j+1]:
#                     cnt += 1
#                 else:
#                     return False
#             return cnt == (len(nums)-1)
    
# nums = [1] # 输出为None不满足

# 力扣加加解法：

def checkPossibility(nums):
    N = len(nums)
    count = 0
    for i in range(1, N):
        if nums[i] < nums[i-1]:
            count += 1
            if count > 1:
                return False
            if i >= 2 and nums[i] < nums[i-1]:
                nums[i] = nums[i-1]
    return True

nums = [4, -1, 2, 3]
result = checkPossibility(nums)
print(result) 
