# Q3. Implement Power Function
# Problem Description
# Implement pow(A, B) % C.
# In other words, given A, B and C, Find (AB % C).
#
# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.
#
#
#
# Problem Constraints
# -109 <= A <= 109
# 0 <= B <= 109
# 1 <= C <= 109
#
#
# Input Format
# Given three integers A, B, C.
#
#
# Output Format
# Return an integer.
#
#
# Example Input
# A = 2, B = 3, C = 3
#
#
# Example Output
# 2
#
#
# Example Explanation
# 23 % 3 = 8 % 3 = 2
def calcPow(A, B, C):
    # Base Cases
    if (A == 0):
        return 0
    if (B == 0):
        return 1

    # If B is Even
    y = 0
    if (B % 2 == 0):
        y = calcPow(A, B / 2, C)
        y = (y * y) % C

    # If B is Odd
    else:
        y = A % C
        y = (y * calcPow(A, B - 1,
                         C) % C) % C
    return ((y + C) % C)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        A = A%C
        if A == 0 or A == 1:
            return A
        ans = calcPow(A, B, C)
        return ans