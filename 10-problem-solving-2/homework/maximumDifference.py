# Q3. Maximum Difference
# Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 |
#
# where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1
#
# Note |x| denotes the absolute value of x.
#
#
# Input Format
#
# The arguments given are the integer array A and integer B.
# Output Format
#
# Return the maximum value of | s1 - s2 |.
# Constraints
#
# 1 <= B < length of the array <= 100000
# 1 <= A[i] <= 10^5
# For Example
#
# Input 1:
# A = [1, 2, 3, 4, 5]
# B = 2
# Output 1:
# 9
#
# Input 2:
# A = [5, 17, 100, 11]
# B = 3
# Output 2:
# 123
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        left, right = 0, 0
        if B < n-B:
            left = B
            right = n-B
        else:
            right = B
            left = n-B
        leftSum, rightSum = 0, 0
        for i in range(left):
            leftSum += A[i]
        for i in range(left, n):
            rightSum += A[i]
        return abs(leftSum - rightSum)
