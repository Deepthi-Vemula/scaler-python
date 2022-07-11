# Q2. Very Large Power
# Problem Description
# Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).
#
# "^" means power,
#
# "%" means "mod", and
#
# "!" means factorial.
#
#
#
# Problem Constraints
# 1 <= A, B <= 5e5
#
#
#
# Input Format
# First argument is the integer A
#
# Second argument is the integer B
#
#
#
# Output Format
# Return one integer, the answer to the problem
#
#
#
# Example Input
# Input 1:
#
# A = 1
# B = 1
# Input 2:
#
# A = 2
# B = 2
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 4
#
#
# Example Explanation
# Explanation 1:
#
# 1! = 1. Hence 1^1 = 1.
# Explanation 2:
#
# 2! = 2. Hence 2^2 = 4.
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

def calcFact(B, val):
    fact = 1
    for i in range(1, B+1):
        fact = (fact*i)%val
    return fact
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        modVal = 1000000007
        bVal = calcFact(B, modVal-1)
        ans = calcPow(A, bVal , modVal)
        return ans


