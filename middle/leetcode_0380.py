"""
    1、常数时间复杂度完成插入、删除和获取随机元素操作
    2、考察对于基本数据结构的时间和空间复杂度的理解与应用
    3、重点题目，回顾基本数据结构的时间空间复杂度
    4、本题采用的是数组加哈希表
"""
from random import random

class RandomizedSet:

    def __init__(self):
        """
        Initialized Data Structure Here!
        """
        self.data = dict()
        self.arr = []
        self.n = 0

    def insert(self, val):
        """
        Inserts a value from the set.
        Returns true if the set did not already contains the specified element.
        """
        if val in self.data:
            return False
        self.data[val] = self.n
        self.arr.append(val)
        self.n += 1
        return True

    def remove(self, val):
        """
        Remove a value from the set.
        Returns true if the set contains the specified element.
        """
        if val not in self.data:
            return False
        i = self.data[val]
        # 更新data
        self.data[self.arr[-1]] = i
        self.data.pop(val)
        # 更新arr
        self.arr[i] = self.arr[-1]
        # 删除最后一项
        self.arr.pop()
        self.n -= 1
        return True

    def getRadnom(self):
        """
        Get a random element from the set.
        """
        return self.arr[int(random() * self.n)]