# Q3. SUBARRAY OR
# Problem Description
# You are given an array of integers A of size N.
#
# The value of a subarray is defined as BITWISE OR of all elements in it.
#
# Return the sum of value of all subarrays of A % 109 + 7.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= A[i] <= 108
#
#
#
# Input Format
# The first argument given is the integer array A.
#
#
#
# Output Format
# Return the sum of Value of all subarrays of A % 109 + 7.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# Input 2:
#
# A = [7, 8, 9, 10]
#
#
# Example Output
# Output 1:
#
# 71
# Output 2:
#
# 110
#
#
# Example Explanation
# Explanation 1:
#
# Value([1]) = 1
# Value([1, 2]) = 3
# Value([1, 2, 3]) = 3
# Value([1, 2, 3, 4]) = 7
# Value([1, 2, 3, 4, 5]) = 7
# Value([2]) = 2
# Value([2, 3]) = 3
# Value([2, 3, 4]) = 7
# Value([2, 3, 4, 5]) = 7
# Value([3]) = 3
# Value([3, 4]) = 7
# Value([3, 4, 5]) = 7
# Value([4]) = 4
# Value([4, 5]) = 5
# Value([5]) = 5
# Sum of all these values = 71
# Explanation 2:
#
# Sum of value of all subarray is 110.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve1(self, A):
        n, sumVal, modVal = len(A), 0, 1000000007
        for i in range(n):
            orVal = 0
            for j in range(i, n):
                orVal = orVal | A[j]
                sumVal = (sumVal + orVal) % modVal
        return sumVal

    def solve(self, A):
        n, maxVal, ans, modVal = len(A), A[0], 0, 1000000007
        for i in range(n):
            maxVal = max(maxVal, A[i])
        maxVal = len(bin(maxVal)[2:])
        for i in range(maxVal):
            index, sumVal = 0, 0
            # print("for each position", i, index, sumVal)
            while index < n:
                while index < n and ((A[index] >> i) & 1):
                    index += 1
                cnt1 = 0
                # print("1st index", index)
                while index < n and not ((A[index] >> i) & 1):
                    cnt1 += 1
                    index += 1
                # print("2nd index", index, cnt1, 1 << i)
                sumVal += int((cnt1 * (cnt1 + 1)) / 2)
            tempAns = (int((n * (n + 1)) / 2) - sumVal) % modVal
            ans = (ans + tempAns * (1 << i)) % modVal
        return ans


sol = Solution()
A1 = [1, 2, 3, 4, 5]
A = [165711, 168085, 366621, 16961, 99152, 8199, 70876, 82733, 229357, 255042, 22297, 37966, 75776, 13065, 28293,
     505601, 727321, 12663, 641901, 29156, 63361, 448033, 216751, 147761, 154281, 40376, 128745, 365517, 175087, 202255,
     279685, 152353, 59889, 1, 115561, 47571, 22051, 17253, 118595, 326977, 581053, 226656, 344499, 140676, 55913,
     195961, 9925, 105709, 120658, 239876, 528641, 16233, 9781, 8482, 61018, 80561, 443161, 155145, 34041, 237399, 1,
     439525, 195456, 92401, 373463, 8281, 132469, 393317, 63532, 2851, 145681, 686713, 32701, 95745, 82461, 673201,
     103156, 180097, 243283, 87283, 121028, 645910, 290113, 1905, 147833, 343486, 94968, 132386, 526989, 946081, 368987,
     817657, 376489, 249034, 94817, 17382, 17986, 190817, 220351, 49267]
print (sol.solve(A))
