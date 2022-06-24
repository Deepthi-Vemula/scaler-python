# Q3. Remove Duplicates from Sorted Array
# Problem Description
#
# Given a sorted array A consisting of duplicate elements.
#
# Your task is to remove all the duplicates and return a sorted array of distinct elements consisting of all distinct elements present in A.
#
# NOTE: The input format has been changed from previous versions.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 106
#
# 1 <= A[i] <= 2*109
#
#
#
# Input Format
#
# First and only argurment containing the integer array A.
#
#
#
# Output Format
#
# Return an array/vector from the function as per the question.
#
#
#
# Example Input
#
# Input 1:
#
# A = [1, 1, 2]
# Input 2:
#
# A = [1, 2, 2, 3, 3]
#
#
# Example Output
#
# Output 1:
#
# [1, 2]
# Output 2:
#
# [1, 2, 3]
#
#
# Example Explanation
#
# Explanation 1:
#
# Updated Array: [1, 2] after removing the 2nd element.
# Explanation 2:
#
# Updated Array: [1, 2, 3] after removing the 3rd and 5th element.
def findlastMatchingIndex(A, start, end, el):
    if start >= end:
        return -1
    print(start, end, el)
    if A[end] == el:
        return end
    mid = int((start + end)/2)
    if mid + 1 <= end and A[mid] == el and A[mid+1] != el:
        return mid
    if A[mid] > el:
        return findlastMatchingIndex(A, start, mid-1, el)
    return findlastMatchingIndex(A, mid+1, end, el)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        index = 1
        while index < len(A):
            if A[index] == A[index-1]:
                print("index val : ", index)
                i1 = findlastMatchingIndex(A, index, len(A) - 1, A[index])
                print("last index", i1)
                if i1 == -1:
                    del A[index]
                else:
                    del A[index-1:i1]
                print("deleted array : ", A)
            else:
                index += 1
        return A


A = [1, 2, 2, 2, 2, 3, 3]
A1 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
sol = Solution()
print (sol.solve(A1))