# 2023/5/2  author:WH

# 枚举：但是提交答案超时了
class Solution:
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        i = j = 0
        while x ** i <= bound:
            i += 1
        iMax = i
        while y ** j <= bound:
            j += 1
        jMax = j
        for m in range(iMax):
            for n in range(jMax):
                res = x ** m + y ** n
                if res <= bound:
                    ans.add(res)
                else:
                    break
        return list(ans)
    
if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    result = Solution().powerfulIntegers(x, y, bound)
    print(result)