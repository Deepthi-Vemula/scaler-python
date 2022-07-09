# Q2. Rain Water Trapped
# Problem Description
# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
#
#
# Input Format
# First and only argument is the vector A
#
#
#
# Output Format
# Return one integer, the answer to the question
#
#
#
# Example Input
# Input 1:
#
# A = [0, 1, 0, 2]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# 1 unit is trapped on top of the 3rd element.
# Explanation 2:
#
# No water is trapped.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        leftMax, rightMax = [0 for i in range(n)], [0 for i in range(n)]
        lm, rm = 0, 0
        for i in range(n):
            leftMax[i] = lm
            lm = max(lm, A[i])
        for i in range(n - 1, -1, -1):
            rightMax[i] = rm
            rm = max(rm, A[i])
        water = 0
        print(leftMax)
        print(rightMax)
        for i in range(n):
            w = min(leftMax[i], rightMax[i]) - A[i]
            print(i, w)
            if w > 0:
                water += w
        return water


A1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
A2 = [56, 6, 52, 43, 23, 47, 48, 38, 96, 46, 30, 66, 80, 15, 62, 71, 61, 12, 98, 9, 28, 81, 70, 59, 95, 34, 9, 60, 70, 81, 71, 67, 58, 20, 22, 3, 95, 85, 20, 24, 74, 5, 23, 33, 75, 50, 38, 75, 68, 26, 46, 30, 75, 18, 4, 42, 51, 59, 8, 77 ]
A3 = [5, 4, 3, 2, 1, 2, 3, 4, 5]
sol = Solution()
print(sol.trap(A3))
