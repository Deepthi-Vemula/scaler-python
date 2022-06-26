# Q4. Is Dictionary?
# Problem Description
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
#
#
#
# Problem Constraints
# 1 <= N, length of each word <= 105
#
# Sum of the length of all words <= 2 * 106
#
#
#
# Input Format
# The first argument is a string array A of size N.
#
# The second argument is a string B of size 26, denoting the order.
#
#
#
# Output Format
# Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
#
#
#
# Example Input
# Input 1:
#
# A = ["hello", "scaler", "interviewbit"]
# B = "adhbcfegskjlponmirqtxwuvzy"
# Input 2:
#
# A = ["fine", "none", "no"]
# B = "qwertyuiopasdfghjklzxcvbnm"
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
# The order shown in string B is: h < s < i for the given words. So return 1.
# Explanation 2:
#
# "none" should be present after "no". Return 0.
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        hashMap = {}
        for i in range(len(B)):
            hashMap[B[i]] = i
        # print(hashMap)
        for i in range(1, len(A)):
            j = 0
            while j < min(len(A[i]), len(A[i-1])):
                # print("comparing ", A[i-1], A[i], hashMap[A[i-1][j]], hashMap[A[i][j]])
                if hashMap[A[i][j]] < hashMap[A[i-1][j]]:
                    return 0
                if hashMap[A[i][j]] > hashMap[A[i-1][j]]:
                    break
                j += 1
            if j == min(len(A[i]), len(A[i-1])) and len(A[i]) < len(A[i-1]):
                return 0

        return 1

A = [ "fine", "none", "no" ]
B = "qwertyuiopasdfghjklzxcvbnm"


# A = ["hello", "scaler", "interviewbit" ]
# B = "adhbcfegskjlponmirqtxwuvzy"
sol = Solution()
print (sol.solve(A, B))