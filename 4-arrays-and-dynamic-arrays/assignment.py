# coding=utf-8
def searchInArray(A, val, start, end):
    print(A, val, start, end)
    if start > end:
        return False
    if val < A[start] or val > A[end]:
        return False
    mid = int((start + end) / 2)
    print("mid: ", mid)
    if val == A[mid]:
        print("yes, they are same!")
        return True
    if val > A[mid]:
        return searchInArray(A, val, mid + 1, end)
    if val < A[end]:
        return searchInArray(A, val, start, mid - 1)
    return False


class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        pass

    # Q1. Good Pair
    #
    # Problem Description
    # Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B).
    # Check if any good pair exist or not.
    #
    # Problem Constraints
    # 1 <= A.size() <= 104
    #
    # 1 <= A[i] <= 109
    #
    # 1 <= B <= 109
    #
    # Input Format
    # First argument is an integer array A.
    #
    # Second argument is an integer B.
    #
    # Output Format
    # Return 1 if good pair exist otherwise return 0.
    #
    # Example Input
    # Input 1:
    #
    # A = [1,2,3,4]
    # B = 7
    # Input 2:
    #
    # A = [1,2,4]
    # B = 4
    # Input 3:
    #
    # A = [1,2,2]
    # B = 4
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 0
    # Output 3:
    #
    # 1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # (i,j) = (3,4)
    # Explanation 2:
    #
    # No pair has sum equal to 4.
    # Explanation 3:
    #
    # (i,j) = (2,3)
    def solveGoodPair(self, A, B):
        # sort the array A
        A.sort()
        n = int(len(A))
        for i in range(0, n):
            val = B - A[i]
            if searchInArray(A, val, i + 1, n - 1):
                return 1
        return 0

    # Q2. FizzBuzz
    # Problem Description
    #
    # Given a positive integer A, return an array of strings with all the integers from 1 to N.
    # But for multiples of 3 the array should have “Fizz” instead of the number. For the multiples of 5,
    # the array should have “Buzz” instead of the number. For numbers which are multiple of 3 and 5 both, the array should have "FizzBuzz" instead of the number.
    #
    # Look at the example for more details.
    #
    #
    #
    # Problem Constraints
    #
    # 1 <= A <= 500000
    #
    #
    #
    # Input Format
    #
    # The first argument has the integer A.
    #
    #
    #
    # Output Format
    #
    # Return an array of string.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = 5
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # [1 2 Fizz 4 Buzz]
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # 3 is divisible by 3 so it is replaced by "Fizz".
    # Similarly, 5 is divisible by 5 so it is replaced by "Buzz".
    def fizzBuzz(self, A):
        numArr = []
        for i in range(1, A + 1):
            if i % 3 == 0 and i % 5 == 0:
                numArr.append("FizzBuzz")
            elif i % 3 == 0:
                numArr.append("Fizz")
            elif i % 5 == 0:
                numArr.append("Buzz")
            else:
                numArr.append(str(i))
        return numArr

    # Q3. Odd Even Subsequences
    # Given an array of integers A of size, N. Find the longest subsequence of A, which is odd-even.
    #
    # A subsequence is said to be odd-even in the following cases:
    #
    # The first element of the subsequence is odd; the second element is even, the third element is odd, and so on.
    # For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]
    #
    # The first element of the subsequence is even, the second element is odd, the third element is even, and so on.
    # For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]
    #
    # Return the maximum possible length of odd-even subsequence.
    #
    # Note: An array B is a subsequence of an array A if B can be obtained from A by deleting several (possibly, zero, or all) elements.
    #
    # Input Format
    #
    # The only argument given is the integer array A.
    # Output Format
    #
    # Return the maximum possible length of odd-even subsequence.
    # Constraints
    # 1 <= N <= 100000
    # 1 <= A[i] <= 10^9
    # For Example
    #
    # Input 1:
    # A = [1, 2, 2, 5, 6]
    # Output 1:
    # 4
    # Explanation 1:
    # Maximum length odd even subsequence is [1, 2, 5, 6]
    #
    # Input 2:
    # A = [2, 2, 2, 2, 2, 2]
    # Output 2:
    # 1
    # Explanation 2:
    # Maximum length odd even subsequence is [2]
    def oddEvenSubSequenceOfArray(self, A):
        count = 1
        i = 1
        odd = False
        if A[0] % 2 == 1:
            odd = True
        for i in range(len(A)):
            if (A[i] % 2 == 1) != odd:
                count = count + 1
                odd = not odd

        return count

    # Q4. Time to equality
    # Given an integer array A of size N. In one second, you can increase the value of one element by 1.
    #
    # Find the minimum time in seconds to make all elements of the array equal.
    # Problem Constraints
    # 1 <= N <= 1000000
    # 1 <= A[i] <= 1000
    #
    #
    # Input Format
    # First argument is an integer array A.
    #
    #
    # Output Format
    # Return an integer denoting the minimum time to make all elements equal.
    #
    #
    # Example Input
    # A = [2, 4, 1, 3, 2]
    #
    #
    # Example Output
    # 8
    #
    #
    # Example Explanation
    # We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.
    # @param A : list of integers
    # @return an integer
    def timeToEquality(self, A):
        maxVal = max(A)
        sec = 0
        for el in A:
            sec = sec + (maxVal - el)
        return sec

    # Q5. Rotation Game
    # Problem Description
    # Given an integer array **A** and an integer **B**, you have to print the same array after rotating it **B** times towards the right.
    #
    #
    # Output Format
    # Print an array of integers which is the **Bth** right rotation of input array **A**, on a separate line.
    #
    #
    # Example Input
    # Input 1:
    #
    #
    # Example Output
    # Output 1:
    #
    #
    # Example Explanation
    # Explanation 1:
    # [1,2,3,4] => [4,1,2,3] => [3,4,1,2]
    #NOTE: this code works only for python 3
def reverse(A, start, end):
    i, j = start, end
    while(i < j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i, j = i + 1, j - 1

def main():
    temp = input().split()
    N = int(temp[0])
    A = [0] * N
    for i in range(1, N + 1):
        A[i - 1] = int(temp[i])
    B = int(input())
    B = B % N
    reverse(A, 0, N - 1);
    reverse(A, 0, B - 1);
    reverse(A, B, N - 1);
    for i in range(0, N):
        print(A[i],' ')
    print()
    return 0

if __name__ == '__main__':
    main()

# A = [1, 2, 3, 4]
# B = 7

# A = [ 652437, 548143, 817759, 412805, 982146, 432095, 69432, 443328, 913932, 822954 ]
# B = 829843

# A = [633299, 189622, 811214, 549111, 864962, 673215, 526221, 271580, 78335, 890164]
# B = 968499
sol = Solution()
# print("sol val: ", sol.solveGoodPair(A, B))
# print(sol.fizzBuzz(15))

A3 = [2, 2, 2, 2, 2, 2]
B3 = [1, 2, 2, 5, 6]
# print ("oddEvenSubSequenceOfArray: ", sol.oddEvenSubSequenceOfArray(B3))

print (sol.timeToEquality(B3))
