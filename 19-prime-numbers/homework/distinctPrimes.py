# Q4. Distinct Primes
# You have given an array A having N integers. Let say G is the product of all elements of A.
#
# You have to find the number of distinct prime divisors of G.
#
#
#
# Input Format
#
# The first argument given is an Array A, having N integers.
# Output Format
#
# Return an Integer, i.e number of distinct prime divisors of G.
# Constraints
#
# 1 <= N <= 1e5
# 1 <= A[i] <= 1e5
# For Example
#
# Input:
# A = [1, 2, 3, 4]
# Output:
# 2
#
# Explanation:
# here G = 1 * 2 * 3 * 4 = 24
# and distinct prime divisors of G are [2, 3]
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pdt, maxVal = 1, max(A)
        spf = [i for i in range(maxVal + 1)]
        for i in range(2, int(math.sqrt(maxVal)) + 1):
            if spf[i] == i:
                for j in range(i * i, maxVal + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        primeNumbers, count = {}, 0
        for i in range(len(A)):
            temp = A[i]
            # print("for ", i)
            while temp > 1:
                x1 = spf[int(temp)]
                if x1 not in primeNumbers.keys():
                    primeNumbers[x1] = 1
                    count += 1
                while temp % x1 == 0:
                    temp = temp / x1
        return count


A = [96, 98, 5, 41, 80]
sol = Solution()
print (sol.solve(A))
