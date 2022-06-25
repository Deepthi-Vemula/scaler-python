# Q3. Find subsequence
# Given two strings A and B, find if A is a subsequence of B.
#
# Return "YES" if A is a subsequence of B, else return "NO".
#
#
# Input Format
#
# The first argument given is the string A.
# The second argument given is the string B.
# Output Format
#
# Return "YES" if A is a subsequence of B, else return "NO".
# Constraints
#
# 1 <= lenght(A), length(B) <= 100000
# 'a' <= A[i], B[i] <= 'z'
# For Example
#
# Input 1:
# A = "bit"
# B = "dfbkjijgbbiihbmmt"
# Output 1:
# YES
#
# Input 2:
# A = "apple"
# B = "appel"
# Output 2:
# "NO"
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        n1, n2, ai, bi, cnt = len(A), len(B), 0, 0, 0
        # print(A, B, n1, n2)
        while bi < n2 and ai < n1:
            # print(ai, bi, A, B, n1, n2)
            while bi < n2 and A[ai] != B[bi]:
                bi += 1
            print(ai, bi, A, B)
            if bi < n2 and A[ai] == B[bi]:
                cnt += 1
                bi += 1
            ai += 1
        if cnt == n1:
            return "YES"
        return "NO"


A = "bit"
B = "dfbkjijgbbiihbmmt"
sol = Solution()
print(sol.solve(A, B))
