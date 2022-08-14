# Q2. Search for a Range
#     Problem Description
# Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].
#
#
#
# Problem Constraints
# 1 <= N <= 106
#
# 1 <= A[i], B <= 109
#
#
#
# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.
#
#
#
# Output Format
# Return an array of size 2, such that the first element = starting position of B in A
# and the second element = the ending position of B in A if B is not found in A return [-1, -1].
#
#
#
# Example Input
# Input 1:
#
# A = [5, 7, 7, 8, 8, 10]
# B = 8
# Input 2:
#
# A = [5, 17, 100, 111]
# B = 3
#
#
# Example Output
# Output 1:
#
# [3, 4]
# Output 2:
#
# [-1, -1]
#
#
# Example Explanation
# Explanation 1:
#
# The first occurence of 8 in A is at index 3.
# The second occurence of 8 in A is at index 4.
# ans = [3, 4]
# Explanation 2:
#
# There is no occurence of 3 in the array.
def findFirstPos(A, start, end, B):
    if start > end:
        return -1
    mid = int((start + end)/2)
    # print("findFirstPos : ", A[mid], start, end)
    if A[mid] == B and ((mid>0 and A[mid-1] != B) or mid == 0):
        return mid
    if A[mid] < B:
        return findFirstPos(A, mid+1, end, B)
    return findFirstPos(A, start, mid-1, B)


def findLastPos(A, start, end, B):
    if start > end:
        return -1
    mid = int((start + end)/2)
    # print("findLastPos : ", A[mid], start, end)
    n = len(A)
    if A[mid] == B and (((mid+1)<n and A[mid+1] != B) or mid == n-1):
        return mid
    if A[mid] > B:
        return findLastPos(A, start, mid-1, B)
    return findLastPos(A, mid+1, end, B)





class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)
        # finding first position using binSearch
        a = findFirstPos(A, 0, n-1 ,B)
        b = findLastPos(A, 0, n-1, B)
        return [a, b]


A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
      3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
      6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9,
      9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10
# expected ans = [118 133]
sol = Solution()
print(sol.searchRange(A, B))