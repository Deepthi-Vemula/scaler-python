# Q2. Intersection Of Sorted Arrays
# Problem Description
#
# Find the intersection of two sorted arrays. OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.
#
# Example:
#
# Input:
# A: [1 2 3 3 4 5 6]
# B: [3 3 5]
#
# Output: [3 3 5]
#
# Input:
# A: [1 2 3 3 4 5 6]
# B: [3 5]
#
# Output: [3 5]
# NOTE : For the purpose of this problem ( as also conveyed by the sample case ),
# assume that elements that appear more than once in both arrays should be included multiple times in the final output.
def findNearestElement(A, start, end, el):
    if A[end] < el:
        return end + 1
    mid = int((start + end) / 2)
    if A[mid] == el:
        while mid and A[mid] == A[mid - 1]:
            mid -= 1
        return mid
    if (mid == 0 and A[mid] > el) or (mid > 0 and A[mid] > el and A[mid - 1] < el):
        return mid
    if el > A[mid]:
        return findNearestElement(A, mid + 1, end, el)
    if el < A[mid]:
        return findNearestElement(A, start, mid - 1, el)


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        ap, bp, an, bn = 0, 0, len(A), len(B)
        intersectionArray = []
        while ap < an and bp < bn:
            if A[ap] == B[bp]:
                # print("yes, it's a match!", A[ap])
                intersectionArray.append(A[ap])
                ap += 1
                bp += 1
            elif A[ap] < B[bp]:
                ap = findNearestElement(A, ap, an - 1, B[bp])
            else:
                bp = findNearestElement(B, bp, bn - 1, A[ap])
        return intersectionArray


sol = Solution()
# A = [1, 3, 8, 10, 13, 13, 16, 16, 16, 18, 21, 23, 24, 31, 31, 31, 33, 35, 35, 37, 37, 38, 40, 41, 43, 47, 47, 48, 48,
#      52, 52, 53, 53, 55, 56, 60, 60, 61, 61, 63, 63, 64, 66, 67, 67, 68, 69, 71, 80, 80, 80, 80, 80, 80, 81, 85, 87, 87,
#      88, 89, 90, 94, 95, 97, 98, 98, 100, 101]
# B = [5, 7, 14, 14, 25, 28, 28, 34, 35, 38, 38, 39, 46, 53, 65, 67, 69, 70, 78, 82, 94, 94, 98]
A = [ 2, 3, 3, 4, 4, 6, 8, 8, 9, 9, 10, 10, 11, 14, 14, 15, 16, 18, 20, 21, 23, 23, 24, 25, 28, 29, 33, 33, 35, 35, 37, 38, 38, 40, 41, 42, 42, 44, 44, 47, 47, 49, 49, 52, 53, 56, 58, 61, 62, 62, 63, 64, 65, 65, 66, 67, 67, 67, 68, 69, 72, 74, 76, 76, 79, 80, 82, 82, 83, 83, 83, 84, 85, 85, 85, 85, 87, 91, 93, 94, 94, 94, 95, 96, 101, 101 ]
B = [ 12, 12, 20, 39, 42, 44, 47, 73, 77 ]
print (sol.intersect(A, B))
