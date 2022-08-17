# Q2. Food Packets Distribution
# Problem Description
# The government wants to set up B distribution offices across N cities for the distribution of food
# packets. The population of the ith city is A[i]. Each city must have at least 1 office, and people can go to an office of their own city. We want to maximize the minimum number of people who can get food in any single office.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= A[i] <= 106
#
# 1 <= B <= 5 x 105
#
#
#
# Input Format
# The first line of input contains an integer array A.
#
# The second line of input contains an integer B.
#
#
#
# Output Format
# Return one integer representing the maximum number of people who can get food in any single office.
#
#
#
# Example Input
# Input 1:
#
# A = [10000, 20000, 30000]
# B = 6
# Input 2:
#
# A = [1, 1, 1]
# B = 4
#
#
# Example Output
# Output 1:
#
# 10000
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
# 1 office can be opened in the first city,
# 2 offices in the second city and
# 3 in the third. This way ,
# 10,000 people can get food in the office in the first city, and
# 10,000 people can get food in each office in the second city and
# 10,000 people can get food in third city.
# We will allot 10000 people in each office in the third city.
# Had we alloted more in some office, we had to allot lesser in some other office which will reduce the answer.
# Explanation 2:
#
# We will have to allot 2 offices to one city. And one of these offices would give food to 0 people.
def check(A, minVal, B):
    nCentres = 0
    for val in A:
        if (val // minVal) == 0:
            return False
        nCentres += val // minVal
    return nCentres >= B


def minAllocation(A, start, end, B):
    if start > end:
        return -1
    mid = (start + end) // 2
    ans = check(A, mid, B)
    # print("minAllocation ", start, end, mid, ans)
    if not ans:
        return minAllocation(A, start, mid - 1, B)
    val = minAllocation(A, mid + 1, end, B)
    if val == -1:
        return mid
    return val


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if sum(A) < B:
            return 0
        return minAllocation(A, 1, max(A), B)


# A = [8, 7, 1, 5, 5, 10, 10, 1, 5, 3]
# B = 17

# A = [10000, 20000, 30000]
# B = 7

sol = Solution()
print(sol.solve(A, B))
