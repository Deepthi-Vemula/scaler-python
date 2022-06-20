# Q5. Count ways to make sum of odd and even indexed elements equal by removing an array element
# Problem Description
# Given an array, arr[] of size N, the task is to find the count of array indices such that
# removing an element from these indices makes the sum of even-indexed and
# odd-indexed array elements equal.
#
#
#
# Problem Constraints
# 1 <= n <= 105
# -105 <= A[i] <= 105
#
#
# Input Format
# First argument contains an array A of integers of size N
#
#
# Output Format
# Return the count of array indices such that removing an element from these indices makes the
# sum of even-indexed and odd-indexed array elements equal.
#
#
#
# Example Input
# Input 1:
# A=[2, 1, 6, 4]
# Input 2:
#
# A=[1, 1, 1]
#
#
# Example Output
# Output 1:
# 1
# Output 2:
#
# 3
#
#
# Example Explanation
# Explanation 1:
# Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that,
# arr[0] + arr[2] = arr[1].
# Therefore, the required output is 1.
# Explanation 2:
#
# Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Therefore, the required output is 3.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        sumArray = [0 for i in range(n)]
        if n == 1:
            return A[0] == 0
        sumArray[0], sumArray[1] = A[0], A[1]
        for i in range(2, n):
            sumArray[i] = sumArray[i - 2] + A[i]
        print(sumArray)
        lastOdd, lastEven, count = -1, -1, 0
        if n % 2 == 1:
            lastEven = n - 1
            lastOdd = n - 2
        else:
            lastOdd = n - 1
            lastEven = n - 2
        print(lastOdd, lastEven)
        for i in range(n):
            evenSum, oddSum = 0, 0
            if i % 2 == 1:
                print(i, "odd index")
                print("for oddSum ", sumArray[lastEven], sumArray[i-1])
                print("for evenSum ", sumArray[lastOdd], sumArray[i])

                if i > 0:
                    evenSum = sumArray[i - 1]
                    if i < n-1:
                        oddSum -= sumArray[i-1]
                if i > 1:
                    oddSum += sumArray[i - 2]
                if i < n-1:
                    oddSum += sumArray[lastEven]
                    evenSum += sumArray[lastOdd] - sumArray[i]
            else:
                print(i, "even index", lastEven, lastOdd)
                print("for oddSum ", sumArray[lastEven], sumArray[i])
                print("for evenSum ", sumArray[lastOdd], sumArray[i - 1])
                if i > 0:
                    oddSum = sumArray[i - 1]
                    if i < n-1:
                        evenSum -= sumArray[i-1]
                if i > 1:
                    evenSum += sumArray[i - 2]
                if i < n-1:
                    evenSum += sumArray[lastOdd]
                    oddSum += sumArray[lastEven] - sumArray[i]
            if oddSum == evenSum:
                count += 1
            print(i, evenSum, oddSum)
        return count


sol = Solution()
A = [2, 1, 6, 4]
A2 = [1, 1, 1]
A3 = [1, 2, 3, 7, 1, 2, 3]
A4 = [1, 2, 5, 1, 2]
print (sol.solve(A4))
