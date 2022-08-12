# Q1. Kth Smallest Element
# Problem Description
# Find the Bth smallest element in given array A .
#
# NOTE: Users should try to solve it in less than equal to B swaps.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= B <= min(|A|, 500)
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
# The first argument is an integer array A.
#
# The second argument is integer B.
#
#
#
# Output Format
# Return the Bth smallest element in given array.
#
#
#
# Example Input
# Input 1:
#
# A = [2, 1, 4, 3, 2]
# B = 3
# Input 2:
#
# A = [1, 2]
# B = 2
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 2
#
#
# Example Explanation
# Explanation 1:
#
# 3rd element after sorting is 2.
# Explanation 2:
#
# 2nd element after sorting is 2.
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        # selection sort
        A = list(A)
        n = len(A)
        for ind in range(B):
            min_index = ind

            for j in range(ind + 1, n):
                # select the minimum element in every iteration
                if A[j] < A[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            temp = A[ind]
            A[ind] = A[min_index]
            A[min_index] = temp
        return A[B-1]


A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
B = 9
sol = Solution()
print(sol.kthsmallest(A, B))