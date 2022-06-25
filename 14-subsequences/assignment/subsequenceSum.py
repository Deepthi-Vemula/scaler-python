# Q4. Subsequence-Sum Problem
# Problem Description
#
# You are given an array of integers of N size.
#
# You have to find that there is any subsequence exists or not whose sum is equal to B.
#
#
#
# Problem Constraints
#
# 1 <= N <= 20
# 1 <= A[i] <= 100000
# 0 <= B <= 1e9
#
#
# Input Format
#
# First Argument is array of integers A
# Second Argument is B
#
#
#
# Output Format
#
# Return 1 if any subsequence sum is equal to B otherwise return 0.
#
#
#
# Example Input
#
# Input 1:
#
# A=[1,20,13,4,5]
# B=18
# Input 2:
#
#
# A=[2,2,2,2]
# B=5
#
#
# Example Output
#
# 1
# Output 1:
#
#
# 1
# Output 2:
#
#
# 0
#
#
# Example Explanation
#
# Explanation 1:
# There is as subsequence present at indexes 1,3,4 whose sum is 18
# Explanation 2:
#
#
# There is no possible subsequence whose sum is 5
# NOTE: Array is considered 1 based indexing for the above explanation.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Base Case
        n = len(A)
        for i in range(1, pow(2, n)):
            sumVal, j = 0, 0
            while j < n:
                if i >> j & 1:
                    # print("included", i >> j, A[j])
                    sumVal += A[j]
                j += 1
            # print(sumVal)
            if sumVal == B:
                return 1
        return 0


A = [87538, 59509, 15940, 30570, 17686, 55831, 74461, 92198, 4872, 41884, 22828, 82415, 82829, 78818, 66225, 64102,
     92580, 24777, 41751, 92808]
B = 1036814


# A=[1, 20, 13, 4, 5]
# B=18
sol = Solution()
print (sol.solve(A, B))
