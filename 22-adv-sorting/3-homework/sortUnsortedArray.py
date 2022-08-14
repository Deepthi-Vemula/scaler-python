# Q1. Maximum Unsorted Subarray
# Problem Description
# Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.
#
#
#
# Problem Constraints
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000000
#
#
#
# Input Format
# First and only argument is an array of non-negative integers of size N.
#
#
#
# Output Format
# Return an array of length two where the first element denotes the starting index(0-based) and the second element denotes the ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 2, 4, 5]
# Input 2:
#
# A = [1, 2, 3, 4, 5]
#
#
# Example Output
# Output 1:
#
# [1, 2]
# Output 2:
#
# [-1]
#
#
# Example Explanation
# Explanation 1:
#
# If we sort the sub-array A1, A2, then the whole array A gets sorted.
# Explanation 2:
#
# A is already sorted.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        leftMax, rightMin, n = A[0], A[-1], len(A)
        leftSortedTillIndex, rightSortedTillIndex = 0, n - 1
        while leftSortedTillIndex + 1 < n and A[leftSortedTillIndex] <= A[leftSortedTillIndex + 1]:
            leftMax = max(leftMax, A[leftSortedTillIndex + 1])
            leftSortedTillIndex += 1
        if leftSortedTillIndex == n - 1:
            return [-1]
        while rightSortedTillIndex > 0 and A[rightSortedTillIndex] >= A[rightSortedTillIndex - 1]:
            rightMin = min(rightMin, A[rightSortedTillIndex])
            rightSortedTillIndex -= 1
        # print (leftSortedTillIndex, rightSortedTillIndex)
        lindex, rindex = leftSortedTillIndex, rightSortedTillIndex
        while lindex < rightSortedTillIndex:
            leftMax = max(leftMax, A[lindex])
            lindex += 1
        while rindex > leftSortedTillIndex:
            rightMin = min(rightMin, A[rindex])
            rindex -= 1
        # print("leftMax, rightMin", leftMax, rightMin)
        while leftSortedTillIndex >= 0 and A[leftSortedTillIndex] > rightMin:
            leftSortedTillIndex -= 1
        # print (leftSortedTillIndex, rightSortedTillIndex)
        while rightSortedTillIndex < n and A[rightSortedTillIndex] < leftMax:
            rightSortedTillIndex += 1
        # print (leftSortedTillIndex, rightSortedTillIndex)
        # print (leftSortedTillIndex, rightSortedTillIndex)
        return [leftSortedTillIndex+1, rightSortedTillIndex-1]


# A = [1, 2, 3]
A = [1, 3, 2, 4, 5]
sol = Solution()
print(sol.subUnsort(A))