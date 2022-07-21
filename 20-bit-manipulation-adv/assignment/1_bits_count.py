# Q3. Number of 1 Bits
# Problem Description
# Write a function that takes an integer and returns the number of 1 bits it has.
#
#
# Problem Constraints
# 1 <= A <= 109
#
#
# Input Format
# First and only argument contains integer A
#
#
# Output Format
# Return an integer as the answer
#
#
# Example Input
# Input1:
# 11
#
#
# Example Output
# Output1:
# 3
#
#
# Example Explanation
# Explaination1:
# 11 is represented as 1011 in binary.
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        cnt, temp = 0, A
        while temp > 0:
            if temp & 1:
                cnt += 1
            temp = temp >> 1
        return cnt
