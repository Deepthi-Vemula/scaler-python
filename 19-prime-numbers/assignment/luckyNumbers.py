# Q3. Lucky Numbers
# Problem Description
# A lucky number is a number that has exactly 2 distinct prime divisors.
#
# You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).
#
#
#
# Problem Constraints
# 1 <= A <= 50000
#
#
#
# Input Format
# The first and only argument is an integer A.
#
#
#
# Output Format
# Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.
#
#
#
# Example Input
# Input 1:
#
# A = 8
# Input 2:
#
# A = 12
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 3
#
#
# Example Explanation
# Explanation 1:
#
# Between [1, 8] there is only 1 lucky number i.e 6.
# 6 has 2 distinct prime factors i.e 2 and 3.
# Explanation 2:
#
# Between [1, 12] there are 3 lucky number: 6, 10 and 12.
import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        spf = [i for i in range(A+1)]
        for i in range(2, int(math.sqrt(A))+1):
            if spf[i] == i:
                for j in range(i * i, A+1, i):
                    if spf[j] == j:
                        spf[j] = i
        print(spf)
        count = 0
        for i in range(2, A+1):
            divCount, temp = 0, i
            # print("for ", i)
            while temp>1 and divCount<=2:
                x1 = spf[temp]
                while temp%x1 == 0:
                    temp = temp/x1
                # print("-------prime ", x1)
                divCount += 1
            # print("-------divcount ", i, divCount)
            if divCount == 2:
                count += 1

        return count

A = 12
sol = Solution()
print(sol.solve(A))