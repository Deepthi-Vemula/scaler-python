# Q4. N/3 Repeat Number
# Problem Description
# You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
# If so, return the integer. If not, return -1.
#
# If there are multiple solutions, return any one.
#
#
#
# Problem Constraints
# 1 <= N <= 7*105
# 1 <= A[i] <= 109
#
#
# Input Format
# The only argument is an integer array A.
#
#
# Output Format
# Return an integer.
#
#
# Example Input
# [1 2 3 1 1]
#
#
# Example Output
# 1
#
#
# Example Explanation
# 1 occurs 3 times which is more than 5/3 times.
def getCount(A, el):
    count = 0
    for val in A:
        if val == el:
            count += 1
    return count

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        if n == 1 or (n==2 and A[0] == A[1]):
            return A[0]
        if n == 2:
            return -1
        num1, num2, c1, c2 = A[0], A[1], 1, 1
        if A[0] == A[1]:
            c1 = 2
            c2 = 0
        for i in range(2, n):
            if c1 and c2 and A[i] != num1 and A[i] != num2:
                c1 -= 1
                c2 -= 1
            elif A[i] == num1:
                c1 += 1
            elif A[i] == num2:
                c2 += 1
            elif c1 == 0:
                num1 = A[i]
                c1 = 1
            elif c2 == 0:
                num2 = A[i]
                c2 = 1

        if c1 == 0 and c2 == 0:
            return -1
        if c1 != 0 and getCount(A, num1) > int(n/3):
            return num1
        if c2 != 0 and getCount(A, num2) > int(n/3):
            return num2
        return -1

sol = Solution()
A = [1, 2, 3, 1, 1]
A2 = [9, 3, 5, 6, 1, 1, 9, 9, 9, 1, 1]
A3 = [1000441, 1000441, 1000994]
print (sol.repeatedNumber(A3))
