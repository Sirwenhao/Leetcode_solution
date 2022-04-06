'''
    1、树的题基本上看见就不知道怎么写
'''

# leetcode官解
# from matplotlib import collections

# def pathSum(root, targetSum):
#     prefix = collections.defaulrdict(int)
#     prefix[0] = 1

#     def dfs(root, curr):
#         if not root:
#             return 0

#         ret = 0
#         curr += root.val
#         ret += prefix[curr - targetSum]
#         prefix[curr] += 1
#         ret += dfs(root.left, curr)
#         ret += dfs(root.right, curr)
#         prefix[curr] -= 1
#         return ret
#     return dfs(root, 0)


# leetcode加加

import collections

def helper(root,acc,target,hashmap):
    if not root:
        return 0
    count = 0
    acc+=root.val
    if acc==target:
        count+=1
    if acc-target in hashmap:
        count+=hashmap[acc-target]
    hashmap[acc]+=1
    if root.left:
        count+=helper(root.left,acc,target,hashmap)
    if root.right:
        count+=helper(root.right,acc,target,hashmap)
    hashmap[acc]-=1
    return count

def pathSum(root, targetSum):
    hashmap=collections.defaultdict(lambda:0)
    return helper(root,0,targetSum,hashmap)