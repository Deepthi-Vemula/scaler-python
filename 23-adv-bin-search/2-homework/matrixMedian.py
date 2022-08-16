# Q2. Matrix Median
# Problem Description
# Given a matrix of integers A of size N x M in which each row is sorted.
#
# Find and return the overall median of matrix A.
#
# NOTE: No extra memory is allowed.
#
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
#
#
#
# Problem Constraints
# 1 <= N, M <= 10^5
#
# 1 <= N*M <= 10^6
#
# 1 <= A[i] <= 10^9
#
# N*M is odd
#
#
#
# Input Format
# The first and only argument given is the integer matrix A.
#
#
#
# Output Format
# Return the overall median of matrix A.
#
#
#
# Example Input
# Input 1:
#
# A = [   [1, 3, 5],
#         [2, 6, 9],
#         [3, 6, 9]   ]
# Input 2:
#
# A = [   [5, 17, 100]    ]
#
#
# Example Output
# Output 1:
#
# 5
# Output 2:
#
# 17
#
#
# Example Explanation
# Explanation 1:
#
# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
# Median is 5. So, we return 5.
# Explanation 2:
#
# Median is 17.
def getCount(A, start, end, x):
    if start > end:
        return -1
    mid = (start + end) // 2
    if A[mid] <= x:
        return getCount(A, mid + 1, end, x)
    ans = getCount(A, start, mid - 1, x)
    if ans == -1:
        return mid


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        l, r = 0, 0
        n, m = len(A), len(A[0])
        mid, req, ans = -1, (n * m) // 2 + 1, -1

        for i in range(n):
            r = max(r, A[i][m - 1])

        while l <= r:
            mid = (l+r) // 2
            cnt = 0

            for row in A:
                cnt += getCount(row, 0, m - 1, mid)

            print("getCount of ", mid, cnt, req)

            if cnt >= req:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


A = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
sol = Solution()
print(sol.findMedian(A))
