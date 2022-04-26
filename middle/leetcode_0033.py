"""
1、查找目标值，指定了算法复杂度为O(logN)
"""
# 力扣加加解法
def search(nums, target):
    if not nums:
        return -1
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (right-left)//2 + left
        if nums[mid] == target:
            return mid

        if nums[mid] > nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        else:
            if nums[mid+1] <= target <= nums[right]:
                left = mid+1
            else:
                right = mid

    return left if nums[left] == target else -1



nums = [4,5,6,7,0,1,2]
target = 0   
result = search(nums, target)
print(result)