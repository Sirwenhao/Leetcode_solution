'''
    1、一开始理解的有点小问题，与顺序无关，就是单纯数学意义上的交集
'''

def intersection(nums1, nums2):
    a = len(nums1)
    b = len(nums2)
    list = []
    if a > b:
        for i in range(b):
            if nums2[i] in nums1 and nums2[i] not in list:
                list.append(nums2[i])
            else:
                continue
    else:
        for i in range(a):
            if nums1[i] in nums2 and nums1[i] not in list:
                list.append(nums1[i])
            else:
                continue

    return list

nums1 = [1,2,2,1]
nums2 = [2,2]

result = intersection(nums1, nums2)
print(result)