def compare(x, y):
    x = str(x)
    y = str(y)
    return x+y > y+x


def elementsRemoval(A):
    A.sort()
    n = len(A)
    sum = 0
    for el in A:
        sum += n*el
        n -= 1
    return sum


class Solution:
    # Q1. Wave Array
    # Problem Description
    # Given an array of integers A, sort the array into a wave-like array and return it.
    # In other words, arrange the elements into a sequence such that
    #
    # a1 >= a2 <= a3 >= a4 <= a5.....
    # NOTE: If multiple answers are possible, return the lexicographically smallest one.
    #
    #
    #
    # Problem Constraints
    # 1 <= len(A) <= 106
    # 1 <= A[i] <= 106
    #
    #
    #
    # Input Format
    # The first argument is an integer array A.
    #
    #
    #
    # Output Format
    # Return an array arranged in the sequence as described.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 2, 3, 4]
    # Input 2:
    #
    # A = [1, 2]
    #
    #
    # Example Output
    # Output 1:
    #
    # [2, 1, 4, 3]
    # Output 2:5-hashing/homework.py
    #
    # [2, 1]
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # One possible answer : [2, 1, 4, 3]
    # Another possible answer : [4, 1, 3, 2]
    # First answer is lexicographically smallest. So, return [2, 1, 4, 3].
    # Explanation 1:
    #
    # Only possible answer is [2, 1].
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        for i in range(1, n, 2):
            print(A[i-1], A[i])
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
        return A

    # Q2. Largest Number
    # Problem Description
    # Given an array A of non-negative integers, arrange them such that they form the largest number.
    #
    # Note: The result may be very large, so you need to return a string instead of an integer.
    #
    #
    #
    # Problem Constraints
    # 1 <= len(A) <= 100000
    # 0 <= A[i] <= 2*109
    #
    #
    #
    # Input Format
    # The first argument is an array of integers.
    #
    #
    #
    # Output Format
    # Return a string representing the largest number.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [3, 30, 34, 5, 9]
    # Input 2:
    #
    # A = [2, 3, 9, 0]
    #
    #
    # Example Output
    # Output 1:
    #
    # "9534330"
    # Output 2:
    #
    # "9320"
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
    # Explanation 2:
    #
    # Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if not compare(A[i], A[j]):
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
        number = ""
        for i in range(len(A)):
            number += str(A[i])
        return str(int(number))

    # Q3. Unique Elements
    # Problem Description
    # You are given an array A of N elements. You have to make all elements unique. To do so, in one step you can increase any number by one.
    #
    # Find the minimum number of steps.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 109
    #
    #
    #
    # Input Format
    # The only argument given is an Array A, having N integers.
    #
    #
    #
    # Output Format
    # Return the minimum number of steps required to make all elements unique.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 1, 3]
    # Input 2:
    #
    # A = [2, 4, 5]
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
    # We can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3].
    # Explanation 2:
    #
    # All elements are distinct.
    # @param A : list of integers
    # @return an integer
    def uniqueElements001(self, A):
        A.sort()
        # find duplicates and missing elements in the sequence - count and list them
        currElement = A[0]
        count = 0
        for i in range(1,len(A)):
            if currElement < A[i]:
                currElement = A[i]
                continue
            diff = (currElement + 1) - A[i]
            count += diff
            currElement += diff
        return count


    def uniqueElements(self, A):
        A.sort()
        # find duplicates and missing elements in the sequence - count and list them
        duplicates = []
        missingEl = []
        n = len(A)
        start = A[0]
        for i in range(1, n):
            if A[i] == A[i+1]:
                duplicates.append(A[i])
            if len(duplicates) > 0 and (A[i+1] - A[i])>1:
                dupLen = len(duplicates)
            while dupLen>0:

    # Q4. Elements Removal
    # Problem Description
    # Given an integer array A of size N. You can remove any element from the array in one operation.
    # The cost of this operation is the sum of all elements in the array present before this operation.
    #
    # Find the minimum cost to remove all elements from the array.
    #
    #
    #
    # Problem Constraints
    # 0 <= N <= 1000
    # 1 <= A[i] <= 103
    #
    #
    #
    # Input Format
    # First and only argument is an integer array A.
    #
    #
    #
    # Output Format
    # Return an integer denoting the total cost of removing all elements from the array.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [2, 1]
    # Input 2:
    #
    # A = [5]
    #
    #
    # Example Output
    # Output 1:
    #
    # 4
    # Output 2:
    #
    # 5
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Given array A = [2, 1]
    # Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
    # Remove 1 from the array => []. Cost of this operation is (1) = 1.
    # So, total cost is = 3 + 1 = 4.
    # Explanation 2:
    #
    # There is only one element in the array. So, cost of removing is 5.

    # @param A : list of integers
    # @return an integer

    # Q5. Minimize Difference
    # Problem Description
    # Given an array of integers A of size, N. Minimize the absolute difference between the maximum and minimum element of the array.
    #
    # You can perform two types of operations at most B times in total to change the values in the array.
    # Multiple operations can be performed on the same element.
    #
    # Increment : A[i] -> A[i] + 1.
    #
    # Decrement : A[i] -> A[i] - 1.
    #
    # Return the minimum difference possible.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 105
    #
    # 1 <= A[i] <= 106
    #
    # 1 <= B <= 109
    #
    #
    #
    # Input Format
    # First argument is an integer array A.
    # Second argument is an integer B which represents the maximum number of operations that can be performed.
    #
    #
    #
    # Output Format
    # Return an integer denoting the minimum difference.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [2, 6, 3, 9, 8]
    # B = 3
    # Input 2:
    #
    # A = [4, 6, 3, 1, 4]
    # B = 5
    #
    #
    # Example Output
    # Output 1:
    #
    # 5
    # Output 2:
    #
    # 1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # We can apply the atmost 3 operations in the following sequence.
    # Initial array => [2, 6, 3, 9, 8].
    # Decrement 9 => [2, 6, 3, 8, 8].
    # Increment 2 => [3, 6, 3, 8, 8].
    # Increment 3 => [3, 6, 4, 8, 8].
    # Max = 8. Min = 3.
    # Therefore, abs|Max - Min| = |8 - 3| = 5.
    # Explanation 2:
    #
    # We can apply the atmost 5 operations in the following sequence.
    # Initial array => [4, 6, 3, 1, 4].
    # Increment 1 => [4, 6, 3, 2, 4].
    # Decrement 6 => [4, 5, 3, 2, 4].
    # Increment 2 => [4, 5, 3, 3, 4].
    # Decrement 5 => [4, 4, 3, 3, 4].
    # Increment 3 => [4, 4, 4, 3, 4].
    # Max = 4. Min = 3.
    # Therefore, abs|Max - Min| = |4 - 3| = 1.

sol = Solution()  # type: Solution
A1 = [1, 2, 3, 4]
A2 = [5, 1, 3, 2, 4]
# print (sol.wave(A2))
A3 = [3, 30, 34, 5, 9]
A4 = [0, 0, 0, 0, 0]
# print(sol.largestNumber(A4))

A5 = [1, 1, 3]
A6 = [2, 4, 5]
A7 = [1, 2, 2, 3, 3, 3, 5, 6, 7, 8]
print (sol.uniqueElements001(A7))