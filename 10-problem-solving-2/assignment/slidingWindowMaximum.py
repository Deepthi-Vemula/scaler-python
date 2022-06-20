# Q2. Sliding Window Maximum
# Problem Description
# Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.
#
# Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].
#
# Refer to the given example for clarity.
#
# NOTE: If B > length of the array, return 1 element with the max of the array.
#
#
#
# Problem Constraints
# 1 <= |A|, B <= 106
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
# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, -1, -3, 5, 3, 6, 7]
# B = 3
# Input 2:
#
# A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
# B = 6
#
#
# Example Output
# Output 1:
#
# [3, 3, 5, 5, 6, 7]
# Output 2:
#
# [7, 7, 7, 7]
#
#
# Example Explanation
# Explanation 1:
#
# Window position     | Max
# --------------------|-------
# [1 3 -1] -3 5 3 6 7 | 3
# 1 [3 -1 -3] 5 3 6 7 | 3
# 1 3 [-1 -3 5] 3 6 7 | 5
# 1 3 -1 [-3 5 3] 6 7 | 5
# 1 3 -1 -3 [5 3 6] 7 | 6
# 1 3 -1 -3 5 [3 6 7] | 7
# Explanation 2:
#
# Window position     | Max
# --------------------|-------
# [1 2 3 4 2 7] 1 3 6 | 7
# 1 [2 3 4 2 7 1] 3 6 | 7
# 1 2 [3 4 2 7 1 3] 6 | 7
# 1 2 3 [4 2 7 1 3 6] | 7
from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        n = len(A)
        maxArray = []
        window = deque([])
        for i in range(B):
            while (len(window)) and A[i] >= A[window[-1]]:
                window.pop()
            window.append(i)
        for i in range(B, n):
            maxArray.append(A[window[0]])
            print(window, maxArray)
            while len(window) and window[0] <= i - B:
                window.popleft()
            while len(window) and A[i] >= A[window[-1]]:
                window.pop()
            window.append(i)

        print(window, maxArray)
        maxArray.append(A[window[0]])
        return maxArray


sol = Solution()
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
A2 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
B2 = 3
A3 = [1]
B3 = 1
print(sol.slidingMaximum(A3, B3))
