# Q1. Count of divisors
# Problem Description
# Given an array of integers A, find and return the count of divisors of each element of the array.
#
# NOTE: The order of the resultant array should be the same as the input array.
#
#
#
# Problem Constraints
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 106
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the count of divisors of each element of the array in the form of an array.
#
#
#
# Example Input
# Input 1:
#
# A = [2, 3, 4, 5]
# Input 2:
#
# A = [8, 9, 10]
#
#
# Example Output
# Output 1:
#
# [2, 2, 3, 2]
# Output 1:
#
# [4, 3, 4]
#
#
# Example Explanation
# Explanation 1:
#
# The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
# So the count will be [2, 2, 3, 2].
# Explanation 2:
#
# The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
# So the count will be [4, 3, 4].
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        maxVal, n  = max(A) + 1, len(A)
        sol = [0 for i in range(n)]
        spf = [0 for i in range(maxVal)]
        for i in range(1, maxVal):
            spf[i] = i
        for i in range(4, maxVal, 2):
            spf[i] = 2
        for i in range(3, maxVal):
            if spf[i] == i:
                for j in range(int(i * i), maxVal, i):
                    if spf[j] == j:
                        spf[j] = i
        for i in range(n):
            temp, ans = A[i], 1
            while temp != 1:
                cnt, d = 1, spf[temp]
                while temp != 1 and temp%d == 0:
                    cnt += 1
                    temp = temp/d
                ans *= cnt
            sol[i] = ans
        return sol
