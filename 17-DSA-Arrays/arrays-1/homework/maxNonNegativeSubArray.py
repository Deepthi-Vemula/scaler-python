# Q2. Max Non Negative SubArray
# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
#
# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
#
# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
#
# Find and return the required subarray.
#
# NOTE:
#
# 1. If there is a tie, then compare with segment's length and return segment which has maximum length.
# 2. If there is still a tie, then return the segment with minimum starting index.
#
#
# Input Format:
#
# The first and the only argument of input contains an integer array A, of length N.
# Output Format:
#
# Return an array of integers, that is a subarray of A that satisfies the given conditions.
# Constraints:
#
# 1 <= N <= 1e5
# -INT_MAX < A[i] <= INT_MAX
# Examples:
#
# Input 1:
# A = [1, 2, 5, -7, 2, 3]
#
# Output 1:
# [1, 2, 5]
#
# Explanation 1:
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3].
#
# Input 2:
# A = [10, -1, 2, 3, -4, 100]
#
# Output 2:
# [100]
#
# Explanation 2:
# The three sub-arrays are [10], [2, 3], [100].
# The answer is [100] as its sum is larger than the other two.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n, sumVal, maxSum = len(A), 0, -1
        maxSt, maxEnd, st, i = 0, 0, 0, 0
        while i < n:
            if A[i] < 0:
                if sumVal >= 0 and sumVal > maxSum:
                    maxSum = sumVal
                    maxSt, maxEnd = st, i - 1
                elif sumVal >= 0 and sumVal == maxSum:
                    if (maxEnd - maxSt) < (i - 1 - st):
                        maxSt, maxEnd = st, i - 1
                    elif (maxEnd - maxSt) == (i - 1 - st) and st < maxSt:
                        maxSt, maxEnd = st, i - 1
                st = i + 1
                sumVal = 0
            else:
                sumVal += A[i]
            print(A[i], sumVal, maxSum, maxSt, maxEnd)
            i += 1
        print(sumVal, maxSum, maxSt, maxEnd)
        if sumVal >= 0 and sumVal > maxSum:
            maxSt, maxEnd = st, i - 1
            maxSum = sumVal
        elif sumVal >= 0 and sumVal == maxSum:
            if (maxEnd - maxSt) < (i - 1 - st):
                maxSt, maxEnd = st, i - 1
            elif (maxEnd - maxSt) == (i - 1 - st) and st < maxSt:
                maxSt, maxEnd = st, i - 1
        print(sumVal, maxSum, maxSt, maxEnd, A[maxSt: maxEnd+1])
        if maxSum < 0:
            return []
        return A[maxSt: maxEnd+1]


# A = [1, 2, 5, -7, 2, 3]
# A = [10, -1, 2, 3, -4, 100]
# A = [ -1, -1, -1, -1, -1 ]
# A = [ 0, 0, -1, 0 ]
A = [ 1477171087 ]
sol = Solution()
print(sol.maxset(A))
