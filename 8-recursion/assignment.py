import sys
def isPalindrome(A, start, end):
    if start >= end:
        return 1
    if A[start] != A[end]:
        return 0
    return isPalindrome(A, start+1, end-1)
class Solution:
    # Q1. Check Palindrome
    # Problem Description
    # Write a recursive function that checks whether string A is a palindrome or Not.
    # Return 1 if the string A is a palindrome, else return 0.
    #
    # Note: A palindrome is a string that's the same when read forward and backward.
    #
    #
    #
    # Problem Constraints
    # 1 <= A <= 50000
    #
    # String A consists only of lowercase letters.
    #
    #
    #
    # Input Format
    # The first and only argument is a string A.
    #
    #
    #
    # Output Format
    # Return 1 if the string A is a palindrome, else return 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = "naman"
    # Input 2:
    #
    # A = "strings"
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 0
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # "naman" is a palindomic string, so return 1.
    # Explanation 2:
    #
    # "strings" is not a palindrome, so return 0.
    # @param A : string
    # @return an integer
    def checkPalindrome(self, A):
        sys.setrecursionlimit(10**6)
        return isPalindrome(A, 0, len(A)-1)

    # Q2. Find Fibonacci - II
    # Problem Description
    # The Fibonacci numbers are the numbers in the following integer sequence.
    #
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
    #
    # In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:
    #
    # Fn = Fn-1 + Fn-2
    #
    # Given a number A, find and return the Ath Fibonacci Number.
    #
    # Given that F0 = 0 and F1 = 1.
    #
    #
    #
    # Problem Constraints
    # 0 <= A <= 20
    #
    #
    #
    # Input Format
    # First and only argument is an integer A.
    #
    #
    #
    # Output Format
    # Return an integer denoting the Ath term of the sequence.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = 2
    # Input 2:
    #
    # A = 9
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 34
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # f(2) = f(1) + f(0) = 1
    # Explanation 2:
    #
    # f(9) = f(8) + f(7) = 21 + 13  = 34
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        fibSeries = []
        fibSeries.append(0)
        fibSeries.append(1)
        for i in range(2, A+1):
            fibSeries.append(fibSeries[i-1]+fibSeries[i-2])
        return fibSeries[A]