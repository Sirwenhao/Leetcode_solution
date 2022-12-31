# 2022/12/31  author:WH
class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))

if __name__ == "__main__":
    seats = [3, 1, 5]
    students = [2, 7, 4]
    result = Solution().minMovesToSeat(seats, students)
    print(result)