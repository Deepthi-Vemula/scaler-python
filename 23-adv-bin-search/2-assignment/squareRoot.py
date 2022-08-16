# Q1. Square Root of Integer
# Problem Description
# Given an integer A.
#
# Compute and return the square root of A.
#
# If A is not a perfect square, return floor(sqrt(A)).
#
# DO NOT USE SQRT FUNCTION FROM THE STANDARD LIBRARY.
#
# NOTE: Do not use the sqrt function from the standard library. Users are expected to solve this in O(log(A)) time.
#
#
#
# Problem Constraints
# 0 <= A <= 1010
#
#
#
# Input Format
# The first and only argument given is the integer A.
#
#
#
# Output Format
# Return floor(sqrt(A))
#
#
#
# Example Input
# Input 1:
#
# 11
# Input 2:
#
# 9
#
#
# Example Output
# Output 1:
#
# 3
# Output 2:
#
# 3
#
#
# Example Explanation
# Explanation:
#
# When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
# When A = 9 which is a perfect square of 3, so we return 3.
def recSqrt(A, start, end):
    if start>end:
        return start
    mid = int((start+end)/2)
    sq = mid*mid
    if sq == A or (sq<A and (mid+1)*(mid+1)>A):
        return mid
    if sq > A:
        return recSqrt(A, start, mid-1)
    return recSqrt(A, mid+1, end)
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        return recSqrt(A, 0, int(A/2))
