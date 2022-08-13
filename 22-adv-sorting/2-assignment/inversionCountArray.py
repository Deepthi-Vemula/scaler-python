# Q1. Inversion count in an array
# Problem Description
# Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).
#
#
#
# Problem Constraints
# 1 <= length of the array <= 100000
#
# 1 <= A[i] <= 10^9
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the number of inversions of A modulo (109 + 7).
#
#
#
# Example Input
# Input 1:
#
# A = [3, 2, 1]
# Input 2:
#
# A = [1, 2, 3]
#
#
# Example Output
# Output 1:
#
# 3
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# All pairs are inversions.
# Explanation 2:
#
# No inversions.

def calcMergeCount(A, start, end, mid):
    ans = [0 for i in range(end-start+1)]
    leftCount = mid-start+1
    a1, b1 = start, mid+1
    index = 0
    count = 0
    while a1<=mid and b1<=end:
        if A[a1] <= A[b1]:
            ans[index] = A[a1]
            index += 1
            a1 += 1
            leftCount -= 1
        else:
            ans[index] = A[b1]
            index += 1
            b1 +=1
            count += leftCount
    while a1 <= mid:
        ans[index] = A[a1]
        index += 1
        a1 += 1
        leftCount -= 1
    while b1 <= end:
        ans[index] = A[b1]
        index += 1
        b1 +=1
        count += leftCount
    for i in range(len(ans)):
        A[start + i] = ans[i]
    return count

def calcInvertedPairs(A, start, end):
    if start >= end:
        return 0
    mid = int((start+end)/2)
    c1 = calcInvertedPairs(A, start, mid)
    c2 = calcInvertedPairs(A, mid+1, end)
    c3 = calcMergeCount(A, start, end, mid)
    return c1+c2+c3

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return calcInvertedPairs(A, 0, len(A)-1)

A = [3, 2, 1]
# A = [1, 2, 3]
# A = [ 45, 10, 15, 25, 50 ]
sol = Solution()
print(sol.solve(A))