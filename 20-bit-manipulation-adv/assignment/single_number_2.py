# Q1. Single Number II
# Problem Description
# Given an array of integers, every element appears thrice except for one, which occurs once.
#
# Find that element that does not appear thrice.
#
# NOTE: Your algorithm should have a linear runtime complexity.
#
# Could you implement it without using extra memory?
#
#
#
#
# Problem Constraints
# 2 <= A <= 5*106
#
# 0 <= A <= INTMAX
#
#
#
# Input Format
# First and only argument of input contains an integer array A.
#
#
#
# Output Format
# Return a single integer.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Input 2:
#
# A = [0, 0, 0, 1]
#
#
# Example Output
# Output 1:
#
# 4
# Output 2:
#
# 1
#
#
# Example Explanation
# Explanation 1:
#
# 4 occurs exactly once in Input 1.
# 1 occurs exactly once in Input 2.
import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        maxVal = max(A)
        n = int(math.log(maxVal, 2) + 1)
        cnt = [0 for i in range(n)]
        for i in range(len(A)):
            j = 0
            temp = A[i]
            while temp > 0:
                # print("j", j, temp)
                if temp & 1:
                    cnt[j] += 1
                temp = temp >> 1
                j += 1
        num = 0
        for i in range(len(cnt)):
            if cnt[i] % 3 != 0:
                num = num | (1 << i)
        return num


A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# A = [0, 0, 0, 1]
sol = Solution()
print (sol.singleNumber(A))