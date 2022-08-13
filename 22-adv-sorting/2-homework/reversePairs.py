# Q2. Reverse pairs
# Problem Description
# Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
# Return the number of important reverse pairs in the given array A.
#
#
#
# Problem Constraints
# 1 <= length of the array <= 105
#
# -2 * 109 <= A[i] <= 2 * 109
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return the number of important reverse pairs in the given array A.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 2, 3, 1]
# Input 2:
#
# A = [4, 1, 2]
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
# There are two pairs which are important reverse i.e (3, 1) and (3, 1).
# Explanation 2:
#
# There is only one pair i.e (4, 1).

modVal = 1000000007

def merge(A, start, end, mid):
    a1, b1 = start, mid+1
    index = 0
    ans = [0 for i in range(end-start+1)]
    while a1<=mid and b1<=end:
        if A[a1] <= A[b1]:
            ans[index] = A[a1]
            index += 1
            a1 += 1
        else:
            ans[index] = A[b1]
            index += 1
            b1 +=1
    while a1 <= mid:
        ans[index] = A[a1]
        index += 1
        a1 += 1
    while b1 <= end:
        ans[index] = A[b1]
        index += 1
        b1 +=1
    for i in range(len(ans)):
        A[start + i] = ans[i]
    return A

def calcMergeCount(A, start, end, mid):
    # print("calcMergeCount:", A, start, end)
    leftCount = mid-start+1
    a1, b1 = start, mid+1
    count = 0
    while a1<=mid and b1<=end:
        if A[a1] > 2*A[b1]:
            b1 += 1
            count += leftCount
        else:
            a1 +=1
            leftCount -= 1
    merge(A, start, end, mid)
    return count

def calcInvertedPairs(A, start, end):
    # print("calcInvertedPairs", start, end)
    if start >= end:
        return 0
    mid = int((start+end)/2)
    c1 = calcInvertedPairs(A, start, mid)
    c2 = calcInvertedPairs(A, mid+1, end)
    c3 = calcMergeCount(A, start, end, mid)
    return (c1+c2+c3)
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return calcInvertedPairs(A, 0, len(A)-1)


# A = [ 14046, 57239, 78362, 99387, 27609, 55100, 65536, 62099, 40820, 33056, 88380, 78549, 57512, 33137,
#       81212, 32365, 42276, 65368, 52459, 74924, 25355, 76044, 78056, 45190, 94365, 58869, 20611 ]

A = [1, 3, 2, 3, 1]

sol = Solution()
print(sol.solve(A))