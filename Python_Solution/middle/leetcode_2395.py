# 2023/3/26  author:WH

class Solution:
    def findSubarrays(self, nums):
        # start = 0
        # while start < len(nums)-3:
        #     for i in range(start, len(nums)-3):
        #         # print(i)
        #         # print(sum(nums[i:i+2]))
        #         if sum(nums[i:i+2]) == sum(nums[i+1:i+3]):
        #             return True
        #     start += 1
        # return False
        lst = set()
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] not in lst:
                lst.add(nums[i]+nums[i+1])
            else:
                return True
        return False



if __name__ == "__main__":
    nums = [4, 2, 4]
    result = Solution().findSubarrays(nums)
    print(result)
