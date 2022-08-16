# Q4. Ath Magical Number
# Problem Description
# You are given three positive integers, A, B, and C.
#
# Any positive integer is magical if divisible by either B or C.
#
# Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.
#
#
#
# Problem Constraints
# 1 <= A <= 109
#
# 2 <= B, C <= 40000
#
#
#
# Input Format
# The first argument given is an integer A.
#
# The second argument given is an integer B.
#
# The third argument given is an integer C.
#
#
#
# Output Format
# Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.
#
#
#
# Example Input
# Input 1:
#
# A = 1
# B = 2
# C = 3
# Input 2:
#
# A = 4
# B = 2
# C = 3
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 6
#
#
# Example Explanation
# Explanation 1:
#
# 1st magical number is 2.
# Explanation 2:
#
# First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.
modVal = 1000000007


# This function computes GCD
def compute_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


# This function computes LCM
def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x, y)
    return lcm


def magicalNumber(start, end, A, B, n, lcm):
    if start > end:
        return -1
    mid = int((start + end) / 2)
    val = int(mid / A) + int(mid / B) - int(mid / lcm)
    # print("magicalNumber", start, end, mid, val, n)
    if val == n and (mid % A == 0 or mid % B == 0):
        return mid%modVal
    if val >= n:
        return magicalNumber(start, mid - 1, A, B, n, lcm)
    return magicalNumber(mid + 1, end, A, B, n, lcm)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        lcm = compute_lcm(B, C)
        end = min(B, C) * A
        # print("lcm of ", B, C, lcm, " end ", end)
        return magicalNumber(min(B, C), end, B, C, A, lcm)


# A = 19
# B = 11
# C = 13
# ans = 117

# A = 1
# B = 2
# C = 3
# ans = 2

# A = 4
# B = 2
# C = 3
# ans = 6


A = 807414236
B = 3788
C = 38141
# ans = 238134151


sol = Solution()
print(sol.solve(A, B, C))
