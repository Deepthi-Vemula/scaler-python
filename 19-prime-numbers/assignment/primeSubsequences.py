# Q4. Prime Subsequences
# Given an array A having N positive numbers. You have to find the number of Prime subsequences of A.
#
# A Prime subsequence is one that has only prime numbers, for example [2, 3], [5] are the Prime subsequences where [2, 4] and [1, 2, 3, 4] are not.
#
#
#
# Input Format
#
# The first argument given is an Array A, having N integers.
# Output Format
#
# Return an integer X, i.e number of Prime subsequences.
# As X can be very large print X % (1000000007), here % is modulus operator.
# Constraints
#
# 1 <= N <= 1e3
# 1 <= A[i] <= 1e6
# For Example
#
# Input:
# A = [1, 2, 3]
# Output:
# 3
#
# Explanation:
# no. Subsequences      Prime subsequences
# 1.  [1]                     No
# 2.  [1, 2]                  No
# 3.  [1, 3]                  No
# 4.  [1, 2, 3]               No
# 5.  [2]                     Yes
# 6.  [2, 3]                  Yes
# 7.  [3]                     Yes
# 8.  []                      No
#
# here we have 3 subsequences(5, 6, 7) those have only prime number(s).
import math


def isPrime(val):
    if val == 0 or val == 1:
        return False
    for i in range(2, int(math.sqrt(val))+1):
        if val%i == 0:
            return False
    return True
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        modVal, count = 1000000007, 0
        for val in A:
            if isPrime(val):
                print(val)
                count += 1
        return ((1<<count)%modVal - 1)%modVal


A1 = [929419, 129720, 822680, 337758, 709964, 310471, 590339, 337103, 394409, 341947, 564720, 809888, 469243, 58727,
     411493, 838236, 749664, 691280, 111390, 358221, 825155, 674205, 631438, 580626, 754346, 279695, 131295, 177090,
     845088, 477452, 997671, 176057, 787856, 52861, 580365, 199963, 20235, 576514, 893202, 239799, 865243, 525489,
     302318, 940007, 974635, 145878, 555871, 970024, 79329, 89104, 850808, 938543, 89281, 243913, 714179, 652226,
     176496, 691673, 973994, 262065, 472186, 742873, 988272, 346455, 657174, 238321, 562626, 644218, 164526, 363655,
     374914, 27742, 313064, 230421, 72374, 736172, 515364, 950925, 407310, 263216, 697357, 131361, 213435, 897266,
     156887, 402762, 466869, 959540, 170750, 689747, 272842, 865351, 858299, 781873, 707764, 116851, 908642, 27498,
     498651, 718575, 377556, 349405, 460593, 916956, 988183, 94376, 486177, 155453, 653223, 257179, 759719, 415003,
     791303, 780101, 823124, 4577, 102290, 965589, 737582, 836095, 704275, 395067, 883569, 37087, 117796, 180481,
     254444, 681955, 706971, 664842, 605487, 90852, 729017, 262903, 914917, 999386, 107663, 912259, 216708, 924658,
     774457, 855868, 905028, 797711, 957508, 779377, 596325, 875353, 204033, 290206, 434455, 470380, 701273, 363268,
     964674, 527110, 504391, 627102, 29578, 839669, 978805, 649334, 602442, 111459, 997002, 306919, 590547, 565315,
     742278, 608667, 158172, 388211, 83411, 777532, 913585, 524389, 839465, 701653, 919808, 454234, 122550, 739805,
     291001, 125266, 165118, 815720, 188233, 221452, 923586, 418093, 583648]
A = [9, 4, 9, 1, 5]
# A = [2, 2]
sol = Solution()
print (sol.solve(A))
