# Q3. Different Bits Sum Pairwise
# Problem Description
# We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
# For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.
#
# You are given an array of N positive integers, A1, A2,..., AN.
# Find sum of f(Ai, Aj) for all pairs (i, j) such that 1<= i, j<= N. Return the answer modulo 109+7.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= A[i] <= 231 - 1
#
#
#
# Input Format
# The first and only argument of input contains a single integer array A.
#
#
#
# Output Format
# Return a single integer denoting the sum.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 5]
# Input 2:
#
# A = [2, 3]
#
#
# Example Output
# Ouptut 1:
#
# 8
# Output 2:
#
# 2
#
#
# Example Explanation
# Explanation 1:
#
# f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5)
# = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
# Explanation 2:
#
# f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        maxVal = max(A)
        if maxVal == 0:
            return 0
        bitCount = [[0]*2 for i in range(int(math.log(maxVal, 2) + 1))]
        modVal = 1000000007
        print (bitCount)
        for i in range(len(A)):
            temp = A[i]
            index = 0
            while index < len(bitCount):
                if temp & 1:
                    bitCount[index][1] += 1
                else:
                    bitCount[index][0] += 1
                temp = temp >> 1
                index += 1
        cnt = 0
        for i in range(len(bitCount)):
            cnt = (cnt + (bitCount[i][0] * bitCount[i][1])%modVal)%modVal
        return (2*cnt)%modVal

# A = [0, 4, 7, 9]
A = [ 0, 0, 0 ]
sol = Solution()
print(sol.cntBits(A))

