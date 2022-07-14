# Q1. Add One To Number
# Problem Description
# Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :
#
# Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
# A: For the purpose of this question, YES
# Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
# A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
#
#
# Problem Constraints
# 1 <= size of the array <= 1000000
#
#
#
# Input Format
# First argument is an array of digits.
#
#
#
# Output Format
# Return the array of digits after adding one.
#
#
#
# Example Input
# Input 1:
#
# [1, 2, 3]
#
#
# Example Output
# Output 1:
#
# [1, 2, 4]
#
#
# Example Explanation
# Explanation 1:
#
# Given vector is [1, 2, 3].
# The returned vector should be [1, 2, 4] as 123 + 1 = 124.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n, carry, k = len(A), False, 0
        # remove preceding extra zeroes
        while k < n and A[k] == 0:
            k += 1
        if k == n:
            A[0] = 1
            if n == 1:
                return A
            return A[1:]
        else:
            A = A[k:]
        n = len(A)
        i = n - 1
        # add 1 to number
        while i >= 0:
            if 0 <= A[i] < 9:
                A[i] += 1
                carry = False
                break
            A[i] = 0
            carry = True
            i -= 1
        if carry:
            A.insert(0, 1)
        return A


# A = [0]
A = [0, 3, 7, 6, 4, 0, 5, 5, 5]
sol = Solution()
print(sol.plusOne(A))
