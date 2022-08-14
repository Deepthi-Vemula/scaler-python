# Q1. Single Element in a Sorted Array
# Problem Description
# Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= A[i] <= 10^9
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the single element that appears only once.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 1, 7]
# Input 2:
#
# A = [2, 3, 3]
#
#
# Example Output
# Output 1:
#
# 7
# Output 2:
#
# 2
#
#
# Example Explanation
# Explanation 1:
#
# 7 appears once
# Explanation 2:
#
# 2 appears once
def getSingleElement(A, start, end):
    if start >= end:
        return A[start]
    n = len(A)
    mid = int((start+end)/2)
    # print("getSingleElement ", A[mid], start, end)
    # success scenario - single element
    if mid%2 == 0 and ((0<mid<(n-1) and A[mid-1] != A[mid] and A[mid+1] != A[mid]) or (mid == 0 and A[mid+1] != A[mid]) or (mid == n-1 and A[mid-1] != A[mid])):
        return A[mid]
    if (mid%2 == 0 and ((mid>0 and A[mid-1] != A[mid]) or (mid < (n-1) and A[mid] == A[mid+1]))) or (mid%2 == 1 and ((mid>0 and A[mid-1] == A[mid]) or (mid < (n-1) and A[mid] != A[mid+1]))) :
        return getSingleElement(A, mid+1, end)
    return getSingleElement(A, start, mid-1)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return getSingleElement(A, 0, len(A)-1)


A = [ 1, 1, 2, 2, 3 ]
sol = Solution()
print(sol.solve(A))