# Q3. Prime Addition
# You are given an even number N and you need to represent the given number as the sum of primes. The prime numbers do not necessarily have to be distinct. It is guaranteed that at least one possible solution exists.
#
# You need to determine the minimum number of prime numbers needed to represent the given number.
#
# Input
#
# The first argument contains an integer N,the number you need to represent (3<=N<=10^9).
# Output
#
# Return an integer which is the minimum number of prime numbers needed to represent the given number N.
# Examples
#
# Input
#
# 26
# Output
#
# 2
# Explanation
#
# Testcase 1-
#
# You can represent 26 as: 13+13
# So we require minimum of 2 prime numbers to represent the number 26.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 1:
            return 0
        if A == 2:
            return 1
        return 2

