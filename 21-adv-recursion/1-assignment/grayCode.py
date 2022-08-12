# Q2. Gray Code
# Problem Description
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.
#
# A gray code sequence must begin with 0.
#
#
#
# Problem Constraints
# 1 <= A <= 16
#
#
#
# Input Format
# The first argument is an integer A.
#
#
#
# Output Format
# Return an array of integers representing the gray code sequence.
#
#
#
# Example Input
# Input 1:
#
# A = 2
# Input 1:
#
# A = 1
#
#
# Example Output
# output 1:
#
# [0, 1, 3, 2]
# output 2:
#
# [0, 1]
#
#
# Example Explanation
# Explanation 1:
#
# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].
# Explanation 1:
#
# for A = 1 the gray code sequence is:
#     00 - 0
#     01 - 1
# So, return [0, 1].

def recGrayCode(A):
    if A == 1:
        return [0, 1]
    arr = recGrayCode(A-1)
    arr2 = [0 for i in range(len(arr))]
    num = 1<<(A-1)
    # print(arr, num)
    for i in range(len(arr)):
        arr2[i] = (arr[len(arr)-i-1] + num)
    return arr + arr2


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        return recGrayCode(A)



sol = Solution()
print(sol.grayCode(3))