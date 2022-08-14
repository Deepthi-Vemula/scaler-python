# Q3. Find a peak element
# Problem Description
# Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.
#
# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the peak element.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# Input 2:
#
# A = [5, 17, 100, 11]
#
#
# Example Output
# Output 1:
#
# 5
# Output 2:
#
# 100
#
#
# Example Explanation
# Explanation 1:
#
# 5 is the peak.
# Explanation 2:
#
# 100 is the peak.
def getPeak(A, start, end):
    if start > end:
        return -1
    n = len(A)
    mid = int((start+end)/2)
    print("getPeak ", A[mid], start, end)
    if ((0 < mid < (n-1)) and (A[mid] > A[mid-1] and A[mid] > A[mid+1])) or (mid == 0 and A[mid] > A[mid+1]) or (mid == n-1 and A[mid] > A[mid]-1):
        return A[mid]

    if (mid<n-1 and A[mid] < A[mid+1]) or (mid>0 and A[mid] > A[mid-1]):
        return getPeak(A, mid+1, end)
    return getPeak(A, start, mid-1)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return A[0]
        return getPeak(A, 0, len(A)-1)




A = [ 18, 33, 100, 135, 203, 270, 292, 310, 356, 392, 400, 429, 436, 461, 427, 403, 399, 375, 251, 245, 173, 130, 43 ]
# ans = 461

A : [ 10 ]

sol = Solution()
print(sol.solve(A))
