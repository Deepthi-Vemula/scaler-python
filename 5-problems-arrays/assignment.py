import sys


class Solution:
    # Q1. Special Subsequences "AG"
    # Problem Description
    # You have given a string A having Uppercase English letters.
    #
    # You have to find how many times subsequence "AG" is there in the given string.
    #
    # NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
    #
    #
    #
    # Problem Constraints
    # 1 <= length(A) <= 105
    #
    #
    #
    # Input Format
    # First and only argument is a string A.
    #
    #
    #
    # Output Format
    # Return an integer denoting the answer.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = "ABCGAG"
    # Input 2:
    #
    # A = "GAB"
    #
    #
    # Example Output
    # Output 1:
    #
    # 3
    # Output 2:
    #
    # 0
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Subsequence "AG" is 3 times in given string
    # Explanation 2:
    #
    # There is no subsequence "AG" in the given string.
    def countSubsequence(self, A):
        n = len(A)
        count = 0
        countG = 0
        for i in range(n-1, -1, -1):
            if A[i] == 'G':
                countG += 1
            elif A[i] == 'A':
                count += countG
        return count
    # Q2. Closest MinMax
    # Problem Description
    # Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
    #
    # and at least one occurrence of the minimum value of the array.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 2000
    #
    #
    #
    # Input Format
    # First and only argument is vector A
    #
    #
    #
    # Output Format
    # Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 3]
    # Input 2:
    #
    # A = [2]
    #
    #
    # Example Output
    # Output 1:
    #
    # 2
    # Output 2:
    #
    # 1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Only choice is to take both elements.
    # Explanation 2:
    #
    # Take the whole array.
    # @param A : list of integers
    # @return an integer
    def findClosestMinMax(self, A):
        minVal, maxVal = A[0], A[0]
        for el in A:
            if el < minVal:
                minVal = el
            elif el > maxVal:
                maxVal = el
        print("max, min : ", maxVal, minVal)
        maxIndex = -1*sys.maxint
        minIndex = -1*sys.maxint
        ans = len(A)
        for i in range(len(A)):
            if A[i] == minVal:
                minIndex = i
                ans = min(ans, (i-maxIndex+1))
            if A[i] == maxVal:
                maxIndex = i
                ans = min(ans, (i-minIndex+1))
        return ans

    # Q3. Pattern Printing -2
    # Problem Description
    #
    # Print a Pattern According to The Given Value of A.
    #
    # Example: For A = 3 pattern looks like:
    #
    # 1
    # 2 1
    # 3 2 1
    #
    #
    # Problem Constraints
    #
    # 1 <= A <= 1000
    #
    #
    # Input Format
    #
    # First and only argument is an integer denoting A.
    #
    #
    #
    # Output Format
    #
    # Return a two-dimensional array where each row in the returned array represents a row in the pattern.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = 3
    # Input 2:
    #
    # A = 4
    #
    #
    # Example Output
    #
    # Output :1
    #
    # [
    #     [0, 0, 1]
    #     [0, 2, 1]
    #     [3, 2, 1]
    # ]
    # Output 2:
    #
    # [
    #     [0, 0, 0, 1]
    #     [0, 0, 2, 1]
    #     [0, 3, 2, 1]
    #     [4, 3, 2, 1]
    # ]
    #
    #
    # Example Explanation
    #
    # Explanation 2:
    #
    #
    # For A = 4 pattern looks like:
    # 1
    # 2 1
    # 3 2 1
    # 4 3 2 1
    # So we will return it as two-dimensional array.
    # Row 1 contains 3 spaces and 1 integer so spaces will be considered as 0 in the output.
    def patternPrint(self, A):
        matrix = [[0 for i in range(A)] for i in range(A)]
        print(matrix)
        for i in range(A):
            val = i+1
            for j in range(A-1-i, A):
                matrix[i][j] = val
                val -= 1
        print(matrix)

    # Q4. Length of longest consecutive ones
    # Given a binary string A.
    # It is allowed to do at most one swap between any 0 and 1.
    # Find and return the length of the longest consecutive 1s that can be achieved.
    # Input Format
    #
    # The only argument given is string A.
    # Output Format
    #
    # Return the length of the longest consecutive 1s that can be achieved.
    # Constraints
    #
    # 1 <= length of string <= 1000000
    # A contains only characters 0 and 1.
    # For Example
    #
    # Input 1:
    # A = "111000"
    # Output 1:
    # 3
    #
    # Input 2:
    # A = "111011101"
    # Output 2:
    # 7
    # @param A : string
    # @return an integer
    def longestConsecutive1s(self, A):
        totalOnes = 0
        n = len(A)
        left = [0 for i in range(n)]
        if A[0] == '1':
            left[0] = 1
            totalOnes += 1
        for i in range(1, n):
            if A[i] == '1':
                totalOnes += 1
                left[i] = left[i-1] + 1
        if totalOnes == n:
            return n
        right = [0 for i in range(n)]
        if A[n-1] == '1':
            right[n-1] = 1
        for i in range(n-2, -1, -1):
            if A[i] == '1':
                right[i] = right[i+1] + 1
        ans = 0
        if n >= 2:
            if A[0] == '0':
                ans = max(ans, right[1] + 1)
            if A[n-1] == '0':
                ans = max(ans, left[n-2] + 1)
        for i in range(1, n-1):
            if A[i] == '0':
                ans = max(ans, left[i-1]+1+right[i+1])
        if ans > totalOnes and ans > 0:
            ans -= 1
        return ans








sol = Solution()
# A = "ABCGAG"
# print (sol.countSubsequence(A))
#
# A1 = [1, 3]
# A3 = [2]
# A4 = [ 834, 563, 606, 221, 165 ]
# print(sol.findClosestMinMax(A4))
#
# print (sol.patternPrint(3))
A1 = "111011101"
A2 = "1101"
print(sol.longestConsecutive1s(A2))



