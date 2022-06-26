# Q1. Permutations of A in B
# Problem Description
# You are given two strings, A and B, of size N and M, respectively.
#
# You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.
#
#
#
# Problem Constraints
# 1 <= N < M <= 105
#
#
#
# Input Format
# Given two arguments, A and B of type String.
#
#
#
# Output Format
# Return a single integer, i.e., number of permutations of A present in B as a substring.
#
#
#
# Example Input
# Input 1:
#
# A = "abc"
# B = "abcbacabc"
# Input 2:
#
# A = "aca"
# B = "acaa"
#
#
# Example Output
# Output 1:
#
# 5
# Output 2:
#
# 2
#
#
# Example Explanation
# Explanation 1:
#
# Permutations of A that are present in B as substring are:
# 1. abc
# 2. cba
# 3. bac
# 4. cab
# 5. abc
# So ans is 5.
# Explanation 2:
#
# Permutations of A that are present in B as substring are:
# 1. aca
# 2. caa
def checkFrequencies(B, A):
    for i in range(len(B)):
        if B[i] != A[i]:
            return False
    return True
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        lenB = len(B)
        lenA = len(A)
        letterFreqA = [0 for i in range(26)]
        letterFreqB = [0 for i in range(26)]
        offsetVal = ord("a")
        if lenA > lenB or lenB == 0 or lenA == 0:
            return 0
        for i in range(lenA):
            letterFreqA[ord(A[i]) - offsetVal] += 1
            if i < lenA-1:
                letterFreqB[ord(B[i]) - offsetVal] += 1
        count = 0
        for i in range(lenA-1, lenB):
            letterFreqB[ord(B[i]) - offsetVal] += 1
            # check for frequencies match
            if checkFrequencies(letterFreqB, letterFreqA):
                count += 1
            # print ("val to be deleted : ", i-lenA+1, B[i-lenA+1])
            letterFreqB[ord(B[i-lenA+1]) - offsetVal] -= 1
        return count