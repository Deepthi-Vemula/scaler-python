# Q2. Minimize the absolute difference
# Given three sorted arrays A, B and Cof not necessarily same sizes.
#
# Calculate the minimum absolute difference between the maximum and minimum number
# from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
# i.e. minimize | max(a,b,c) - min(a,b,c) |.
#
# Example :
#
# Input:
#
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
# Output:
#
# 1
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def __init__(self):
        pass

    def solve(self, A, B, C):
        # declare pointers for all the three arrays
        a1, b1, c1 = 0, 0, 0
        na, nb, nc = len(A), len(B), len(C)
        minVal, maxVal, diff = sys.maxsize, -1*sys.maxsize + 1, sys.maxsize
        while a1<na and b1<nb and c1<nc:
            minVal = min(A[a1], B[b1], C[c1])
            maxVal = max(A[a1], B[b1], C[c1])
            diff = min(diff, maxVal-minVal)
            if minVal == A[a1]:
                a1 += 1
            if minVal == B[b1]:
                b1 += 1
            if minVal == C[c1]:
                c1 += 1
        return diff
