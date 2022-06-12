# Q3. Sorted Permutation Rank
# Problem Description
# Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.
#
# Note: The answer might not fit in an integer, so return your answer % 1000003
#
#
#
# Problem Constraints
# 1 <= |A| <= 1000
#
#
#
# Input Format
# First argument is a string A.
#
#
#
# Output Format
# Return an integer denoting the rank of the given string.
#
#
#
# Example Input
# Input 1:
#
# A = "acb"
# Input 2:
#
# A = "a"
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 1
#
#
# Example Explanation
# Explanation 1:
#
# Given A = "acb".
# The order permutations with letters 'a', 'c', and 'b' :
#     abc
# acb
# bac
# bca
# cab
# cba
# So, the rank of A is 2.
# Explanation 2:
#
# Given A = "a".
# Rank is clearly 1.

def factorial(A):
    if A == 0 or A == 1:
        return 1
    return A*factorial(A-1)

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        Acopy = ''.join(sorted(A))
        count = 0
        for i in range(len(A)):
            print("index : ", Acopy.index(A[i]))
            count += (factorial(len(Acopy)-1)*Acopy.index(A[i]))% 1000003
            Acopy = Acopy.replace(A[i], '')
            print("count: ", count, Acopy)
        return (count+1)% 1000003

sol = Solution()
str1 = "acb"
str2 = "badc"
str3 = "DTNGJPURFHYEW"
print(sol.findRank(str3))