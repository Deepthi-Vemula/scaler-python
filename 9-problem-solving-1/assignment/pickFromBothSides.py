# Q3. Pick from both sides!
# Problem Description
# You are given an integer array A of size N.
#
# You have to pick B elements in total. Some (possibly 0) elements from left end of array A
# and some (possibly 0) from the right end of array A to get the maximum sum.
#
# Find and return this maximum possible sum.
#
# NOTE: Suppose B = 4, and array A contains 10 elements, then
#
# You can pick the first four elements or can pick the last four elements,
# or can pick 1 from front and 3 from the back, etc.
# You need to return the maximum possible sum of elements you can pick.
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= B <= N
#
# -103 <= A[i] <= 103
#
#
#
# Input Format
# First argument is an integer array A.
#
# Second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the maximum possible sum of elements you picked.
#
#
#
# Example Input
# Input 1:
#
# A = [5, -2, 3 , 1, 2]
# B = 3
# Input 2:
#
# A = [1, 2]
# B = 1
#
#
# Example Output
# Output 1:
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
# Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
# Explanation 2:
#
# Pick element 2 from end as this is the maximum we can get
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n, sumVal = len(A), 0
        start, end = n - B, B - 1
        for i in range(start, n):
            sumVal += A[i]
        maxVal = sumVal
        for i in range(end+1):
            # print("before", sumVal, maxVal, start, i-1)
            sumVal += A[i] - A[start]
            start = (start+1)%n
            maxVal = max(sumVal, maxVal)
            # print("after", sumVal, maxVal)
        return maxVal

sol = Solution()
A = [5, -2, 3 , 1, 2]
B = 3

A1 = [2, 3, 4, 3, 4, 4, 1]
B1 = 6
print (sol.solve(A1,B1))
