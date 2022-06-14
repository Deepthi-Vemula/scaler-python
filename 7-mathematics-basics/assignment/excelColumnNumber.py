# Q1. Excel Column Number
# Problem Description
# Given a column title as appears in an Excel sheet, return its corresponding column number.
#
#
#
# Problem Constraints
# 1 <= length of the column title <= 5
#
#
#
# Input Format
# The only argument is a string that represents the column title in the excel sheet.
#
#
#
# Output Format
# Return a single integer that represents the corresponding column number.
#
#
#
# Example Input
# Input 1:
#
# AB
# Input 2:
#
# ABCD
#
#
# Example Output
# Output 1:
#
# 28
# Output 2:
#
# 19010
#
#
# Example Explanation
# Explanation 1:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        pass

    def titleToNumber(self, A):
        n = len(A)
        number = 0
        for i in range(n):
            val = int(ord(A[i]) - ord('A')) + 1
            number += val*pow(26, n-i-1)
        return number

