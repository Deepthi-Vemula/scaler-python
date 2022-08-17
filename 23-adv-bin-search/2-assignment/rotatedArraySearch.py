# Q2. Rotated Sorted Array Search
# Problem Description
# Given a sorted array of integers A of size N and an integer B.
#
# array A is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
# You are given a target value B to search. If found in the array, return its index otherwise, return -1.
#
# You may assume no duplicate exists in the array.
#
# NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= N <= 1000000
#
# 1 <= A[i] <= 10^9
#
# all elements in A are distinct.
#
#
#
# Input Format
# The first argument given is the integer array A.
#
# The second argument given is the integer B.
#
#
#
# Output Format
# Return index of B in array A, otherwise return -1
#
#
#
# Example Input
# Input 1:
#
# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4
# Input 2:
#
# A = [1]
# B = 1
#
#
# Example Output
# Output 1:
#
# 0
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
#
# Target 4 is found at index 0 in A.
# Explanation 2:
#
#
# Target 1 is found at index 0 in A.
def rotatedArraySearch(A, start, end, B):
    if start > end:
        # print("rotatedArraySearch ", start, end)
        return -1
    mid = int((start + end) / 2)
    print("rotatedArraySearch ", A[mid], start, end)
    if A[mid] == B:
        return mid
    if A[mid] < B:
        if A[end] >= B or (A[start] >= A[end] and ((mid==0) or (mid > 0 and A[mid] > A[mid-1]))):
            return rotatedArraySearch(A, mid + 1, end, B)
        return rotatedArraySearch(A, start, mid - 1, B)
    if A[mid] > B:
        if A[start] <= B or (A[start] >= A[end] and ((mid==0) or (mid > 0 and A[mid] > A[mid-1]))):
            return rotatedArraySearch(A, start, mid - 1, B)
        return rotatedArraySearch(A, mid + 1, end, B)


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        return rotatedArraySearch(A, 0, len(A) - 1, B)


A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202

# A = [180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10,
#      14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64,
#      67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109,
#      111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149,
#      152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177]
# B = 42
# A = [9, 10, 11, 12, 14, 15, 17, 19, 24, 25, 30, 39, 40, 44, 46, 48, 51, 53, 54, 56, 59, 60, 69, 70, 73, 75, 80, 87, 88,
#       89, 92, 93, 97, 99, 104, 107, 109, 110, 111, 117, 123, 124, 125, 126, 127, 128, 135, 136, 137, 141, 148, 153, 154,
#       161, 166, 167, 169, 175, 177, 180, 181, 182, 185, 186, 189, 193, 198, 202, 1, 2, 6, 7]
# B = 198

# A = [ 5, 1, 3 ]
# B = 5

sol = Solution()
print(sol.search(A, B))
