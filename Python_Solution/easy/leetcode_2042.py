# 2023/1/3  author:WH
# class Solution:
#     def areNumbersAscending(self, s):
#         pre = 0
#         for t in s.split():
#             if t[0].isdigit():
#                 if (cur := int(t)) <= pre:
#                     return False
#                 pre = cur
#         return True

class Solution:
    def areNumbersAscending(self, s):
        pre = i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                cur = 0
                while i < n and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                if pre >= cur:
                    return False
                pre = cur
            else:
                i += 1
        return True

if __name__ == "__main__":
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    result = Solution().areNumbersAscending(s)
    print(result)