# 23/10/28 author:WH  参考k神
# N字型变换后输出:核心就是将字符串s按照从左到右的顺序读成N字型的矩阵，然后从左到右从上到下输出矩阵中的所有字符
# 上述方法其实是把问题变复杂了，因为还需要经历将其转为N字型的过程，徒增计算复杂度和空间复杂度
# 核心点是要按照指定要求输出，那么确保输出的结果符合要求即可

class Solution:
    def convert(self, s, numRows):
        l = len(s)
        if numRows < 2:
            return s
        ans = [''] * numRows
        i, flag = 0, -1
        for c in s:
            ans[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(ans)
    

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 4
    result = Solution().convert(s, numRows)
    print(result)
