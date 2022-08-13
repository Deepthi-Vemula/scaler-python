# Q3. B Closest Points to Origin
# Problem Description
# We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).
#
# Here, the distance between two points on a plane is the Euclidean distance.
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)
#
# NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).
#
#
#
# Problem Constraints
# 1 <= B <= length of the list A <= 105
#                              -105 <= A[i][0] <= 105
#                              -105 <= A[i][1] <= 105
#
#
#
# Input Format
# The argument given is list A and an integer B.
#
#
#
#     Output Format
# Return the B closest points to the origin (0, 0) in any order.
#
#
#
#     Example Input
# Input 1:
#
# A = [
# [1, 3],
# [-2, 2]
# ]
# B = 1
# Input 2:
#
# A = [
# [1, -1],
# [2, -1]
# ]
# B = 1
#
#
# Example Output
# Output 1:
#
# [ [-2, 2] ]
# Output 2:
#
# [ [1, -1] ]
#
#
# Example Explanation
# Explanation 1:
#
# The Euclidean distance will be sqrt(10) for point [1,3] and sqrt(8) for point [-2,2].
# So one closest point will be [-2,2].
# Explanation 2:
#
#     The Euclidean distance will be sqrt(2) for point [1,-1] and sqrt(5) for point [2,-1].
# So one closest point will be [1,-1].
from functools import cmp_to_key
import math
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        ans = [[0, 0] for i in range(B)]
        A = sorted(A, key=cmp_to_key(lambda x, y : 1 if (math.sqrt(x[0]*x[0] + x[1]*x[1])) > (math.sqrt(y[0]*y[0] + y[1]*y[1])) else -1))
        # sortedA = sorted(A, cmp=lambda  x, y: (x[0]*x[0] + x[1]*x[1]) - (y[0]*y[0] + y[1]*x[1]))
        # print(A)
        for i in range(0, B):
            ans[i] = A[i]
        return ans

# A = [
#     [1, -1],
#     [2, -1]
# ]
# B = 1

# A = [
#     [1, 3],
#     [-2, 2]
# ]
# B = 1
# A =[
#     [26, 41],
#     [40, 47],
#     [47, 7],
#     [50, 34],
#     [18, 28]]
# B = 5

A = [[-762, 643],[693, -1004],[-1026, 680],[722, -1092],[-875, 630],[787, -860],[-807, 999],[1015, -788],[-760, 889],
     [990, -642],[-1098, 1044],[863, -614],[-744, 651],[959, -898],[-905, 926],[808, -725],[-730, 809],[871, -908],
     [-993, 957],[658, -924],[-927, 872],[735, -821],[-1069, 1018],[839, -777],[-957, 786],[853, -942],[-865, 955],
     [705, -1072],[-717, 940],[922, -618],[-1013, 802],[1065, -884],[-638, 1063],[654, -882],[-722, 718],[703, -870],
     [-837, 1059],[723, -747],[-869, 620],[951, -625],[-890, 693],[1043, -927],[-745, 636],[976, -951],[-1055, 711],
     [658, -867],[-1011, 1049],[867, -624],[-685, 1018],[1018, -962],[-1070, 885],[954, -798],[-1005, 1095],[-370, 81],
     [156, -484],[-286, 228],[476, -87],[-450, 114],[86, -315],[-89, 466],[383, -447]]
B = 8
sol = Solution()
print(sol.solve(A, B))