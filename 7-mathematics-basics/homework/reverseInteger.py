# Q4. Reverse integer
# Problem Description
#
# You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer
#
# Look at the example for clarification.
#
#
#
# Problem Constraints
#
# N belongs to the Integer limits.
#
#
#
# Input Format
#
# Input an Integer.
#
#
#
# Output Format
#
# Return a single integer denoting the reverse of the given integer.
#
#
#
# Example Input
#
# Input 1:
#
# x = 123
#
# Input 2:
#
# x = -123
#
#
# Example Output
#
# Output 1:
#
# 321
#
# Ouput 2:
#
# -321
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        n = 0
        negativeFlag = False
        if A < 0:
            A *= -1
            negativeFlag = True
        while A>0:
            n = n*10 + (A%10)
            A = int(A/10)
            # print("n, A", n, A)
        if(abs(n) > (2 ** 31 - 1)):
            return 0
        if negativeFlag:
            n *= -1
        return n

sol = Solution()
val1 = -1987654321
val2 = -1234567891
val3 = -1153072433
val4 = 1563847412
print(sol.reverse(val2))