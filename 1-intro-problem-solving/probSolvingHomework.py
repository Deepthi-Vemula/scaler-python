import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        pass
    # Homework Q1
    # You are given an Array A of size N.
    #
    # Find for how many elements, there is a strictly smaller element and a strictly greater element.
    #
    # Input Format
    #
    # Given only argument A an Array of Integers.
    # Output Format
    #
    # Return an Integer X, i.e number of elements.
    # Constraints
    #
    # 1 <= N <= 1e5
    # 1 <= A[i] <= 1e6
    # For Example
    #
    # Example Input:
    # A = [1, 2, 3]
    #
    # Example Output:
    # 1
    #
    # Explanation:
    # only 2 have a strictly smaller and strictly greater element, 1 and 3 respectively.
    def numberswithStrictlyGreaterElements(self, A):
        minVal = min(A)
        maxVal = max(A)
        count = 0
        for val in A:
            if minVal < val < maxVal:
                count += 1
        return count

    # Homework Q2
    # You are given an array of distinct integers A,
    # you have to find and return all elements in array
    # which have at-least two greater elements than themselves.
    # NOTE: The result should have the order in which they are present in the original array.
    def getArrayWithout2Maximums(self, A):
        del A[A.index(max(A))]
        del A[A.index(max(A))]
        return A

    # Homework Q3
    # You are given an array of integers A of size N.
    # Return the difference between the maximum
    # among all even numbers of A and the minimum among all odd numbers in A.
    def getMaxEvenMinOddDiff(self, A):
        minOdd = sys.maxint
        maxEven = -sys.maxint


        for val in A:
            if (val%2 == 0 and val>maxEven):
                maxEven = val
            if(val%2==1 and val<minOdd) :
                minOdd = val
        return maxEven-minOdd

    # Homework Q4
    # Print a Pattern According to The Given Value of A.
    # Example: For A = 3 pattern looks like:
    # 1 0 0
    # 1 2 0
    # 1 2 3
    def printPattern(self, val):
        ans = [[0]*val for i in range(val)]
        for i in range(0,val+1):
            for j in range(i):
                ans[i-1][j] = j+1
        return ans


arr1 = [1, 2, 3, 4, 5]
sol = Solution()
print(sol.numberswithStrictlyGreaterElements(arr1))

arr2 = [10999, 5, 11, 18, 890]
print(sol.getArrayWithout2Maximums(arr2))

arr3 = [5, 17, 100, 1]
print(sol.getMaxEvenMinOddDiff(arr3))

print(sol.printPattern(4))

