# Q1. Tower of Hanoi
# Problem Description
# In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
# You have the following constraints:
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# You have to find the solution to the Tower of Hanoi problem.
# You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
# In each row, there should be 3 integers (disk, start, end), where:
#
# disk - number of disk being moved
# start - number of the tower from which the disk is being moved
# stop - number of the tower to which the disk is being moved
#
#
# Problem Constraints
# 1 <= A <= 18
#
#
# Input Format
# The first argument is the integer A.
#
#
# Output Format
# Return a 2D array with dimensions M x 3 as mentioned above in the description.
#
#
# Example Input
# Input 1:
# A = 2
# Input 2:
#
# A = 3
#
#
# Example Output
# Output 1:
# [1 1 2 ] [2 1 3 ] [1 2 3 ]
# Output 2:
#
# [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ]
#
#
# Example Explanation
# Explanation 1:
# We shift the first disk to the middle tower.
# We shift the second disk to the last tower.
# We, finally, shift the first disk from the middle tower to the last tower.
# Explanation 2:
#
# We can see that this the only unique path with minimal moves to move all disks from the first to the third tower.
# test cases
# 1 = [1 1 3 ]
# 2 = [1 1 2 ] [2 1 3 ] [1 2 3 ]
# 3 = [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ]
# 4 = [1 1 2 ] [2 1 3 ] [1 2 3 ] [3 1 2 ] [1 3 1 ] [2 3 2 ] [1 1 2 ] [4 1 3 ] [1 2 3 ] [2 2 1 ] [1 3 1 ] [3 2 3 ] [1 1 2 ] [2 1 3 ] [1 2 3 ]
# 5 = [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ] [4 1 2 ] [1 3 2 ] [2 3 1 ] [1 2 1 ] [3 3 2 ] [1 1 3 ] [2 1 2 ] [1 3 2 ] [5 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ] [3 2 1 ] [1 3 2 ] [2 3 1 ] [1 2 1 ] [4 2 3 ] [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ]
import copy
def printSeq(arr):
    # print("printSeq", len(arr))
    # replace all 2 with 3 and 3 with 2 for 2nd and third values
    for i in range (len(arr)):
        for j in range(1, len(arr[i])):
            if arr[i][j] == 2:
                arr[i][j] = 3
            elif arr[i][j] == 3:
                arr[i][j] = 2
    return arr

def toggleArr(arr2):
    arr = copy.deepcopy(arr2)
    for i in range (len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] = arr[i][j] + 1
            if arr[i][j] == 4:
                arr[i][j] = 1
    # print("toggleArr: after toggle orgininal array", arr2, "changed array : ", arr)
    return arr

def recTowerOfHanoi(A):
    # print("recTowerOfHanoi ", A)
    arrMid = [[A, 1, 3]]
    if A<=1:
        return arrMid
    arr1 = printSeq(recTowerOfHanoi(A-1))
    arr2 = toggleArr(arr1)
    return arr1 + arrMid + arr2

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        return recTowerOfHanoi(A)


sol = Solution()
print(sol.towerOfHanoi(5))


