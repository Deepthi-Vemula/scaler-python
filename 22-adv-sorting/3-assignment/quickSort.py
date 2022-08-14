# Q2. QuickSort
# Problem Description
#
# Given an integer array A, sort the array using QuickSort.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 105
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
#
# First argument is an integer array A.
#
#
#
# Output Format
#
# Return the sorted array.
#
#
#
# Example Input
#
# Input 1:
#
# A = [1, 4, 10, 2, 1, 5]
# Input 2:
#
# A = [3, 7, 1]
#
#
# Example Output
#
# Output 1:
#
# [1, 1, 2, 4, 5, 10]
# Output 2:
#
# [1, 3, 7]
#
#
# Example Explanation
#
# Explanation 1:
#
# Return the sorted array.
def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, A):
    if len(A) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return A
    if l < r:
        pi = partition(l, r, A)
        quicksort(l, pi-1, A)  # Recursively sorting the left values
        quicksort(pi+1, r, A)  # Recursively sorting the right values
    return A


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A = quicksort(0, len(A)-1, A)
        return A

A = [ 1, 4, 10, 2, 1, 5 ]
sol = Solution()
print(sol.solve(A))

