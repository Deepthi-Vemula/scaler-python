# Q2. Matrix Search
# Problem Description
# Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.
#
# This matrix A has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.
#
# NOTE: Rows are numbered from top to bottom, and columns are from left to right.
#
#
#
# Problem Constraints
# 1 <= N, M <= 1000
# 1 <= A[i][j], B <= 106
#
#
#
# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer B.
#
#
#
# Output Format
# Return 1 if B is present in A else, return 0.
#
#
#
# Example Input
# Input 1:
#
# A = [
#     [1,   3,  5,  7]
#     [10, 11, 16, 20]
#     [23, 30, 34, 50]
# ]
# B = 3
# Input 2:
#
# A = [
#     [5, 17, 100, 111]
#     [119, 120, 127, 131]
# ]
# B = 3
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# 3 is present in the matrix at A[0][1] position so return 1.
# Explanation 2:
#
# 3 is not present in the matrix so return 0.
def recSearch(A, start, end, B):
    mid = [int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2)]
    if start[0] > end[0] or start[1] > end[1]:
        # print("recSearch", start, end)
        return False
    # print("recSearch", A[mid[0]][mid[1]], start, end)
    if A[mid[0]][mid[1]] == B:
        return True
    if A[mid[0]][mid[1]] > B:
        return recSearch(A, start, [mid[0] - 1, end[1]], B) or recSearch(A, [mid[0], start[1]], [mid[0], mid[1] - 1], B)
    return recSearch(A, [mid[0] + 1, start[1]], end, B) or recSearch(A, [mid[0], mid[1]+1], [mid[0], end[1]], B)


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        val = recSearch(A, [0, 0], [len(A) - 1, len(A[0]) - 1], B)
        if val:
            return 1
        return 0


A = [
    [3, 3, 11, 12, 14],
    [16, 17, 30, 34, 35],
    [45, 48, 49, 50, 52],
    [56, 59, 63, 63, 65],
    [67, 71, 72, 73, 79],
    [80, 84, 85, 85, 88],
    [88, 91, 92, 93, 94]]
B = 94


# A = [[1],
#     [11],
#     [49],
#     [74],
#     [77],
#     [78],
#     [93],
#     [94]]
# B = 49


# A =[
#     [4, 4, 21, 26, 33, 35, 44],
#     [46, 48, 51, 57, 58, 58, 59],
#     [67, 68, 73, 80, 86, 90, 93]]
# B = 44
sol = Solution()
print(sol.searchMatrix(A, B))
