# 2023/5/17  author:WH

class Solution:
    def haveConflict(self, event1, event2):
        return (event2[1] >= event1[1] >= event2[0] or event1[1] >= event2[1] >= event1[0])
    
if __name__ == "__main__":
    event1 = ["01:15", "02:00"]
    event2 = ["02:00", "03:00"]
    result = Solution().haveConflict(event1, event2)
    print(result)