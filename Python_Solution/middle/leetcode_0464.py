"""
    1、没想法。。。
"""

# 力扣加加解法
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False
        # picked用于保存当前已经选择过的数
        # acc表示当前累计的数字和
        def backtrack(picked, acc):
            if acc >= desiredTotal:
                return False
            if len(picked) == maxChoosableInteger:
                return False
            for n in range(1, maxChoosableInteger+1):
                if n not in picked:
                    picked.add(n)
                    if not backtrack(picked, acc + n):
                        picked.remove(n)
                        return True
                    picked.remove(n)
            return False
        return backtrack(set(), 0)
