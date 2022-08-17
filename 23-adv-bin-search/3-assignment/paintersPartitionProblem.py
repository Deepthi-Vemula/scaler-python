# Q1. Painter's Partition Problem
# Problem Description
# Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
# You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.
#
# Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
# NOTE:
# 1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
# 2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.
#
# Return the ans % 10000003.
#
#
#
# Problem Constraints
# 1 <= A <= 1000
# 1 <= B <= 106
# 1 <= N <= 105
# 1 <= C[i] <= 106
#
#
#
# Input Format
# The first argument given is the integer A.
# The second argument given is the integer B.
# The third argument given is the integer array C.
#
#
#
# Output Format
# Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board % 10000003.
#
#
#
# Example Input
# Input 1:
#
# A = 2
# B = 5
# C = [1, 10]
# Input 2:
#
# A = 10
# B = 1
# C = [1, 8, 11, 3]
#
#
# Example Output
# Output 1:
#
# 50
# Output 2:
#
# 11
#
#
# Example Explanation
# Explanation 1:
#
# Possibility 1:- One painter paints both blocks, time taken = 55 units.
# Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
# There are no other distinct ways to paint boards.
# ans = 50 % 10000003
# Explanation 2:
#
# Each block is painted by a painter so, Painter 1 paints block 1, painter 2 paints block 2, painter 3 paints block 3
# and painter 4 paints block 4, time taken = max(1, 8, 11, 3) = 11
# ans = 11 % 10000003
modVal = 10000003
def placePainters(A, nPainters, val, q):
    print("placePainters ", nPainters, val, q)
    # print(A)
    sumVal, n, i = A[0]*q, len(A), 1
    while i < n:
        print("\t values ", sumVal, i, nPainters, val)
        if (sumVal + A[i]*q) > val:
            sumVal = 0
            nPainters -= 1
            if nPainters <= 0:
                return False
        sumVal += A[i]*q
        i += 1
    print("\t values ", sumVal, i, nPainters, val)
    if nPainters > 0:
        return True
    return False

def minPaintersPartition(A, start, end, B, q):
    if start > end:
        return -1
    mid = (start + end) // 2
    ans = placePainters(A, B, mid, q)
    print("minPaintersPartition ", start, end, mid, ans)
    if not ans:
        return minPaintersPartition(A, mid+1, end, B, q)
    val = minPaintersPartition(A, start, mid-1, B, q)
    if val == -1:
        return mid
    return val

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        if A >= len(C):
            return max(C)*B
        maxVal = max(C)
        sumVal = sum(C)
        print(maxVal, sumVal*B)
        return (minPaintersPartition(C, maxVal*B, sumVal*B, A, B))%modVal



# A = 4
# B = 10
# C = [ 884, 228, 442, 889 ]



# A = 10
# B = 1
# C = [1, 8, 11, 3]


# A = 3
# B = 10
# C = [ 185, 186, 938, 558, 655, 461, 441, 234, 902, 681 ]
# ans = 18670

# A = 5
# B = 10
# C = [ 658, 786, 531, 47, 169, 397, 914 ]
# ans = 9140

A = 1
B = 1000000
C = [ 1000000, 1000000 ]


# A = 3
# B = 1
# C = [3, 5, 1, 7, 8, 2, 5, 3, 10, 1, 4, 7, 5, 4, 6]
# ans = 25

sol = Solution()
print(sol.paint(A, B, C))