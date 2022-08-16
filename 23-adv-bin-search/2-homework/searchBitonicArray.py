# Q3. Search in Bitonic Array!
# Problem Description
# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
#
# NOTE:
#
# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
#
#
# Problem Constraints
# 3 <= N <= 105
#
# 1 <= A[i], B <= 108
#
# Given array always contain a bitonic point.
#
# Array A always contain distinct elements.
#
#
#
# Input Format
# First argument is an integer array A denoting the bitonic sequence.
#
# Second argument is an integer B.
#
#
#
# Output Format
# Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.
#
#
#
# Example Input
# Input 1:
#
# A = [3, 9, 10, 20, 17, 5, 1]
# B = 20
# Input 2:
#
# A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
# B = 30
#
#
# Example Output
# Output 1:
#
# 3
# Output 2:
#
# -1
#
#
# Example Explanation
# Explanation 1:
#
# B = 20 present in A at index 3
# Explanation 2:
#
# B = 30 is not present in A
def checkBitonicIndex(A, start, end):
    if start > end:
        return -1
    mid = int((start + end) / 2)
    # print("checkBitonicIndex ", start, end, mid, A[mid])
    if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
        return mid
    if A[mid - 1] < A[mid] < A[mid + 1]:
        return checkBitonicIndex(A, mid + 1, end)
    return checkBitonicIndex(A, start, mid - 1)



def binSearchAsc(A, start, end, B):
    if start > end:
        return -1
    mid = (start + end) // 2
    if A[mid] == B:
        return mid
    if A[mid] > B:
        return binSearchAsc(A, start, mid - 1, B)
    return binSearchAsc(A, mid + 1, end, B)


def binSearchDesc(A, start, end, B):
    if start > end:
        return -1
    mid = (start + end) // 2
    if A[mid] == B:
        return mid
    if A[mid] > B:
        return binSearchDesc(A, mid + 1, end, B)
    return binSearchDesc(A, start, mid - 1, B)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        i1 = checkBitonicIndex(A, 0, n - 1)
        # print("bitonic index", i1)
        ans = binSearchAsc(A, 0, i1, B)
        if ans == -1:
            return binSearchDesc(A, i1 + 1, n - 1, B)
        return ans


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
B = 12
sol = Solution()
print(sol.solve(A, B))
