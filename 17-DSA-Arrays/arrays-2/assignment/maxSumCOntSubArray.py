# Q2. Max Sum Contiguous Subarray
# Problem Description
# Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
#
#
#
# Problem Constraints
# 1 <= N <= 1e6
# -1000 <= A[i] <= 1000
#
#
#
# Input Format
# The first and the only argument contains an integer array, A.
#
#
#
# Output Format
# Return an integer representing the maximum possible sum of the contiguous subarray.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, -10]
# Input 2:
#
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
#
# Example Output
# Output 1:
#
# 10
# Output 2:
#
# 6
#
#
# Example Explanation
# Explanation 1:
#
# The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
# Explanation 2:
#
# The subarray [4,-1,2,1] has the maximum possible sum of 6.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        sumTillHere = A[0]
        maxSum = A[0]
        maxSoFar = A[0]
        for i in range(1, n):
            maxSoFar = max(maxSoFar, A[i])
            sumTillHere += A[i]
            maxSum = max(maxSum, sumTillHere)
            # print(maxSum, sumTillHere)
            if sumTillHere < 0:
                sumTillHere = 0
        if maxSum < 0:
            return maxSoFar
        return maxSum
