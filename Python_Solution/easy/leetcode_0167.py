"""
    1、leetcode第一题的变形
"""

def twoSum(numbers, target):
    left = 1
    while left < len(numbers):
        # print(target-numbers[left-1])
        # print(numbers[left:])
        # print((target-numbers[left-1]) in (numbers[left:]))
        if (target-numbers[left-1]) in (numbers[left:]):
            return [left, numbers[left:].index(target-numbers[left-1])+1+left]
        left+=1
    return False
    

# numbers = [2,7,11,15]
# target = 9
numbers = [0,0,3,4]
target = 0
# print(2 in numbers)
result = twoSum(numbers, target)
print(result)