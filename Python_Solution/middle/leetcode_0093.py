"""
    1、复原IP地址
    2、属于回溯中分割字符串这一系列的问题
"""
# 成为IP地址的条件
# 数字之间使用.进行分隔
# 每一个.分隔开的数字的范围为0~255
# .分隔开的数字不能是01这种前面是0后面是非0数字的情况

# 代码随想录的方法
class Solution:
    def __init__(self) -> None:
        self.ans = []

    def restoreIPAddress(self, s):
        self.ans.clear()
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.ans

    def backtracking(self, s, start_index, pointNum):
        # 递归终止的条件是在原序列中加入了3个.，因此终止递归时current的长度应该正好是字符串s长度+3
        if pointNum == 3:
            # 判断加入.之后对应的self.current是否满足上述的几个要求
            if (self.isValid(s, start_index, len(s)-1)):
                self.ans.append(s[:])
            return
        
        # 定义单层递归逻辑
        for i in range(start_index, len(s)):
            if self.isValid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, pointNum+1)
                # 加入.之后再回溯的话，起始位置就需要重新考虑了
                s = s[:i+1] + s[i+2:]
            else:
                break
    # 这种写法是比较明智的，多传几个参数就可以使判断的过程清晰明了  
    def isValid(self, s, start, end):
        if start > end: return False
        # 如果数字是0开头不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True


if __name__ == "__main__":
    s = "25525511135"
    result = Solution().restoreIPAddress(s)
    print(result)