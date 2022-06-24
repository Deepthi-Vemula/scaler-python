# Q5. Sort the Unsorted Array
# Problem Description
#
# You are given an integer array A having N integers.
#
# You have to find the minimum length subarray A[l..r] such that sorting this subarray makes the whole array sorted.
#
#
#
# Problem Constraints
#
# 1 <= N <= 105
#
# -109 <= A[i] <= 109
#
#
#
# Input Format
#
# First and only argument is an integer array A.
#
#
#
# Output Format
#
# Return an integer denoting the minimum length.
#
#
#
# Example Input
#
# Input 1:
#
# A = [0, 1, 15, 25, 6, 7, 30, 40, 50]
# Input 2:
#
# A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
#
#
# Example Output
#
# Output 1:
#
# 4
# Output 2:
#
# 6
#
#
# Example Explanation
#
# Explanation 1:
#
# The smallest subarray to be sorted to make the whole array sorted =  A[3..6]
# i.e, subarray lying between positions 3 and 6.
# Explanation 2:
#
# The smallest subarray to be sorted to make the whole array sorted =  A[4..9]
# i.e, subarray lying between positions 4 and 9.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        leftMax, rightMin, n = A[0], A[-1], len(A)
        leftSortedTillIndex, rightSortedTillIndex = 0, n - 1
        while leftSortedTillIndex + 1 < n and A[leftSortedTillIndex] <= A[leftSortedTillIndex + 1]:
            leftMax = max(leftMax, A[leftSortedTillIndex + 1])
            leftSortedTillIndex += 1
        # print("leftSortedTillIndex", leftSortedTillIndex)
        if leftSortedTillIndex == n - 1:
            return 0
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
        return rightSortedTillIndex - leftSortedTillIndex - 1


A = [0, 1, 15, 25, 6, 7, 30, 40, 50]
A1 = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
A2 = [-1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000,
      -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000,
      -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000,
      -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000,
      -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -999999999, -999999999,
      -999999998, -999999997, -999999989, -999999989, -999999985, -999999983, -999999962, -999999641, -999999373,
      -999997846, -999983733, -999979539, -999810710, -999741073, -998223758, -997055435, -993590731, -993392766,
      -993254678, -991641947, -990253072, -985832338, -953642548, -905236133, -660391412, -272379836, 836858893,
      -983809782, 134265635, 829051775]
A3 = [-961864025, 837841427, 950691882, 952126598, 996055457]

sol = Solution()
print(sol.solve(A2))
