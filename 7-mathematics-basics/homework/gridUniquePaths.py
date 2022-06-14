# Q2. Grid Unique Paths
# Problem Description
#
# A robot is located at the top-left corner of an A x B grid (marked 'Start' in the diagram below).
#
#
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
#
# Problem Constraints
#
# A and B will be such that the resulting answer fits in a 32 bit signed integer.
#
#
#
# Input Format
#
# First argument of input will be single integer A.
# Second argument of input will be single integer B.
#
#
#
# Output Format
#
# Return a single integer denoting the number of unique paths.
#
#
#
# Example Input
#
# A = 2, B = 2
#
#
# Example Output
#
# 2
#
#
# Example Explanation
#
# 2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
# OR  : (0, 0) -> (1, 0) -> (1, 1)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 1 or B == 1:
            return 1
        if A == 2 or B == 2:
            return max(A,B)
        matrix = [[0 for i in range(B)] for j in range(2)]
        print(matrix)
        for i in range(2):
            matrix[i][0] = 1
        for j in range(B):
            matrix[0][j] = 1
        for i in range(1, A):
            for j in range(1, B):
                matrix[i%2][j] = matrix[(i-1)%2][j] + matrix[i%2][j-1]
        return matrix[(A-1)%2][B-1]

sol = Solution()
print(sol.uniquePaths(1, 1000000007))