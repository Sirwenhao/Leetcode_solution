'''
    1、算是第一个完整完成的easy题目了
    2、
'''

# 解法一：时间复杂度O(n)
# def nextGreatestLetter(letters, target):
#     for i in range(len(letters)):
#         if letters[i] > target:
#             return letters[i]

#     return letters[0]

# 解法2：时间复杂度O(n),空间复杂度O(1)
def nextGreatestLetters(letters, target):
    return next((i for i in letters if i > target), letters[0])

letters = ['c','f','j']
target = 'c'
result = nextGreatestLetters(letters, target)
print(result)