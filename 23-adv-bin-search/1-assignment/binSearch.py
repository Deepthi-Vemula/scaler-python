# Q1. Sorted Insert Position
# Problem Description
# Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= N <= 106
#
#
#
# Input Format
# The first argument is an integer array A of size N.
# The second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the index of target value.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 5, 6]
# B = 5
# Input 2:
#
# A = [1]
# B = 1
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# The target value is present at index 2.
# Explanation 2:
#
# The target value is present at index 0.
def binSearch(A, start, end, B):
    if start > end:
        return -1
    if start == end:
        return start
    mid = int((start + end)/2)
    if A[mid] == B:
        return mid
    if A[mid] > B :
        return binSearch(A, start, mid-1, B)
    return binSearch(A, mid+1, end, B)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        val = binSearch(A, 0, n-1, B)
        print(A[val])
        if not (0 <= val < n):
            return val
        if A[val] < B:
            return val + 1
        return val



# expected return val = 149
A = [ 3, 4, 18, 19, 20, 27, 28, 31, 36, 42, 44, 71, 72, 75, 82, 86, 88, 97, 100, 103, 105, 107, 110, 116, 118, 119, 121,
      122, 140, 141, 142, 155, 157, 166, 176, 184, 190, 199, 201, 210, 212, 220, 225, 234, 235, 236, 238, 244, 259, 265,
      266, 280, 283, 285, 293, 299, 309, 312, 317, 335, 341, 352, 354, 360, 365, 368, 370, 379, 386, 391, 400, 405, 410,
      414, 416, 428, 433, 437, 438, 445, 453, 457, 458, 472, 476, 480, 485, 489, 491, 493, 501, 502, 505, 510, 511, 520,
      526, 535, 557, 574, 593, 595, 604, 605, 612, 629, 632, 633, 634, 642, 647, 653, 654, 656, 658, 686, 689, 690, 691,
      709, 716, 717, 737, 738, 746, 759, 765, 775, 778, 783, 786, 787, 791, 797, 801, 806, 815, 820, 822, 823, 832, 839,
      841, 847, 859, 873, 877, 880, 886, 904, 909, 911, 917, 919, 937, 946, 948, 951, 961, 971, 979, 980, 986, 993 ]
B = 902
#
#expected return val = 4
# A = [ 1, 3, 5, 6 ]
# B = 7


# A = [ 17, 30, 32, 69, 94, 96, 106, 118, 127, 159, 169, 170, 178, 183, 209, 238, 242, 247, 253, 261, 265, 279, 288, 302,
#       305, 316, 352, 357, 374, 376, 392, 402, 410, 421, 439, 442, 444, 446, 454, 458, 464, 467, 468, 498, 500, 513, 523,
#       541, 545, 556, 575, 608, 616, 629, 631, 635, 669, 674, 682, 686, 693, 695, 719, 733, 754, 755, 756, 778, 802, 822,
#       824, 828, 835, 847, 848, 862, 864, 878, 883, 885, 904, 908, 928, 934 ]
# B = 104

sol = Solution()
print(sol.searchInsert(A, B))