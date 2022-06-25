# Q2. Little Ponny and 2-Subsequence
# Problem Description
#
# Little Ponny has been given a string A, and he wants to find out the lexicographically minimum subsequence from it of size >= 2. Can you help him?
#
# A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a. For example, "abc" is lexicographically smaller than "acc" because the first different letter is 'b' and 'c' which is smaller in "abc".
#
#
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 105
#
# A only contains lowercase alphabets.
#
#
#
# Input Format
#
# The first and the only argument of input contains the string, A.
#
#
#
# Output Format
#
# Return a string representing the answer.
#
#
#
# Example Input
#
# Input 1:
#
# A = "abcdsfhjagj"
# Input 2:
#
# A = "ksdjgha"
#
#
# Example Output
#
# Output 1:
#
# "aa"
# Output 2:
#
# "da"
#
#
# Example Explanation
#
# Explanation 1:
#
# "aa" is the lexicographically minimum subsequence from A.
# Explanation 2:
#
# "da" is the lexicographically minimum subsequence from A.
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        min1, min2, n, minIndex = 'z', 'z', len(A), -1
        for i in range(n-1):
            if A[i] < min1:
                min1, minIndex = A[i], i
        # print(min1, A)
        for i in range(minIndex + 1, len(A)):
            if A[i] < min2:
                min2 = A[i]
        return min1+min2


sol = Solution()
A = "djjhibvetj"
print (sol.solve(A))