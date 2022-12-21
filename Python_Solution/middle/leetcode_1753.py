# 2022/12/21  author:WH
# 配对的原则是每次配对都取最大的两个元素进行配对
# a+b < c时，a和b全部都参与配对
# a+b > c时，a,b中分别有一部分与c配对，c配完之后，a，b中剩余部分继续配对直至其中一个为0
class Solution:
    def maximumScore(self, a, b, c):
        v = [a, b, c]
        v.sort()
        if v[0] + v[1] < v[2]:
            return v[0] + v[1]
        return (sum(v) // 2)

if __name__ == "__main__":
    a = 2
    b = 4
    c = 6
    result = Solution().maximumScore(a, b, c)
    print(result)