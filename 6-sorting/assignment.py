import sys


class Solution:
    # Q1. Sort by Color
    # Problem Description
    # Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    #
    # We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.
    #
    # Note: Using the library sort function is not allowed.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 1000000
    # 0 <= A[i] <= 2
    #
    #
    # Input Format
    # First and only argument of input contains an integer array A.
    #
    #
    # Output Format
    # Return an integer array in asked order
    #
    #
    # Example Input
    # Input 1 :
    # A = [0 1 2 0 1 2]
    # Input 2:
    #
    # A = [0]
    #
    #
    # Example Output
    # Output 1:
    # [0 0 1 1 2 2]
    # Output 2:
    #
    # [0]
    #
    #
    # Example Explanation
    # Explanation 1:
    # [0 0 1 1 2 2] is the required order.
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        colorCount = 3
        count = [0 for i in range(colorCount)]
        for el in A:
            count[el] += 1
        index = 0
        for i in range(colorCount):
            for j in range(count[i]):
                A[index] = i
                index += 1
        return A

    # Q2. Kth Smallest Element
    # Problem Description
    # Find the Bth smallest element in given array A .
    #
    # NOTE: Users should try to solve it in less than equal to B swaps.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 100000
    #
    # 1 <= B <= min(|A|, 500)
    #
    # 1 <= A[i] <= 109
    #
    #
    #
    # Input Format
    # The first argument is an integer array A.
    #
    # The second argument is integer B.
    #
    #
    #
    # Output Format
    # Return the Bth smallest element in given array.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [2, 1, 4, 3, 2]
    # B = 3
    # Input 2:
    #
    # A = [1, 2]
    # B = 2
    #
    #
    # Example Output
    # Output 1:
    #
    # 2
    # Output 2:
    #
    # 2
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # 3rd element after sorting is 2.
    # Explanation 2:
    #
    # 2nd element after sorting is 2.
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = A.list()
        if B > len(A):
            return -1
        for i in range(B):
            minVal = A[i]
            index = i
            for j in range(i+1, len(A)):
                if A[j] < minVal:
                    index = j
                    minVal = A[j]
            temp = A[i]
            A[i] = A[index]
            A[index] = temp
        return A[B-1]

    # Q3. Noble Integer
    # Problem Description
    # Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 2*105
    # 1 <= A[i] <= 107
    #
    #
    # Input Format
    # First and only argument is an integer array A.
    #
    #
    #
    # Output Format
    # Return 1 if any such integer p is present else, return -1.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [3, 2, 1, 3]
    # Input 2:
    #
    # A = [1, 1, 3, 3]
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # -1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # For integer 2, there are 2 greater elements in the array..
    # Explanation 2:
    #
    # There exist no integer satisfying the required conditions.
    # @param A : list of integers
    # @return an integer
    def ifNobleIntegerExistsInArray(self, A):
        A.sort()
        n = len(A)
        for i in range(n):
            if i != n-1 and A[i] == A[i+1]:
                continue
            if n-i-1 == A[i]:
                return 1
        return -1

    # Q4. Arithmetic Progression?
    # Problem Description
    # Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
    #
    # A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
    #
    #
    #
    # Problem Constraints
    # 2 <= N <= 105
    #
    # -109 <= A[i] <= 109
    #
    #
    #
    # Input Format
    # The first and only argument is an integer array A of size N.
    #
    #
    #
    # Output Format
    # Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [3, 5, 1]
    # Input 2:
    #
    # A = [2, 4, 1]
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
    # We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
    # Explanation 2:
    #
    # There is no way to reorder the elements to obtain an arithmetic progression.
    # @param A : list of integers
    # @return an integer
    def isArithmeticProgression(self, A):
        hashMap = {}
        min1 = sys.maxint
        min2 = sys.maxint
        for el in A:
            if el < min1:
                min1 = el
            if el in hashMap.keys():
                hashMap[el] += 1
            else:
                hashMap[el] = 1
        A.remove(min1)
        for el in A:
            if el < min2:
                min2 = el
        if len(hashMap) == 1:
            return 1
        print("min1, min2 : ", min1, min2)
        print("hashMap : ", hashMap, len(A))
        d = min2 - min1
        val = min1
        for i in range(len(A)):
            val += d
            print("AP Val : ", i, val)
            if val not in hashMap.keys():
                return 0
            else:
                hashMap.pop(val)
            print("yes, present")
        return 1
    # Q5. Stepwise Selection Sort!
    # Problem Description

    # Given an integer array A of size N.
    #
    # You need to sort the elements in increasing order using SelectionSort. Return a array containing the min value's index position before every iteration.
    #
    # NOTE:
    #
    # Consider 0 based indexing while looking for min value in each step of selection sort.
    # There will be total N - 1 iterations in selection sort so the output array will contain N - 1 integers.
    #
    #
    # Problem Constraints
    #
    # 2 <= N <= 104
    #
    # 1 <= A[i] <= 106
    #
    # All elements are distinct in array A.
    #
    #
    #
    # Input Format
    #
    # First and only argument is an integer array A.
    #
    #
    #
    # Output Format
    #
    # Return an integer array containing N - 1 integers denoting min value's index position before every iteration.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = [6, 4, 3, 7, 2, 8]
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # [4, 2, 2, 4, 4]
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # Explanation : 6 4 3 7 2 8 : Index of 1st min - 4
    # After 1st Iteration : 2 4 3 7 6 8 : Index of 2nd min - 2
    # After 2nd Iteration : 2 3 4 7 6 8 : Index of 3rd min - 2
    # After 3rd Iteration : 2 3 4 7 6 8 : Index of 4th min - 4
    # After 4th iteration : 2 3 4 6 7 8 : Index of 5th min - 4
    # After 5th iteration. : 2 3 4 6 7 8.
    # @param A : list of integers
    # @return a list of integers
    def stepWiseSelectionSort(self, A):
        n = len(A)
        print(A)
        minPosArr = []
        for i in range(n-1):
            index = i
            for j in range(i+1, n):
                if A[j] < A[i]:
                    minVal = A[j]
                    index = j
            print("minVal, index : ", minVal, index)
            minPosArr.append(index)
            temp = A[i]
            A[i] = A[index]
            A[index] = temp
        return minPosArr

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
            currElement += 1
            print("curr el", currElement, A[i], diff)
            # print ("count", count, diff)
        return count

    # minimize DIffernce
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def minDiff(self, A, B):
        # calculate maxVal, minVal, frequency of each number in hashmap
        freq = {}
        maxVal, minVal = A[0], A[0]
        for el in A:
            maxVal = max(el, maxVal)
            minVal = min(el, minVal)
            if el in freq.keys():
                freq[el] += 1
            else:
                freq[el] = 1
        while (minVal < maxVal) and B > 0:
            # print("max, min before : ", minVal, maxVal, B)
            # increment operation
            if freq[minVal] <= freq[maxVal]:
                if B < freq[minVal]:
                    break
                if (minVal+1) in freq.keys():
                    freq[minVal+1] += freq[minVal]
                else:
                    freq[minVal+1] = freq[minVal]
                B -= freq[minVal]
                minVal += 1
            # decrement operation
            if freq[maxVal] <= freq[minVal]:
                if B < freq[maxVal]:
                    break
                if maxVal-1 in freq.keys():
                    freq[maxVal-1] += freq[maxVal]
                else:
                    freq[maxVal-1] = freq[maxVal]
                B -= freq[maxVal]
                maxVal -= 1
            # print("max, min after : ", minVal, maxVal, B)
        if minVal < maxVal:
            return maxVal-minVal
        return 0



sol = Solution()
A1 = [0, 1, 2, 0, 1, 2]
# print (sol.sortColors(A1))

A2 = [3, 5, 1]
A3 = [2, 4, 1]
A4 = [-72, -82, 57, -96, -11, 76, -64, -96, -34, -19, 42, -16, 18, -35, 36]
# print (sol.isArithmeticProgression(A4))


A5 = [6, 4, 3, 7, 2, 8]
# print (sol.stepWiseSelectionSort(A5))

A8 = [1, 1, 3]
A6 = [2, 4, 5]
A7 = [1, 2, 2, 3, 3, 3, 5, 6, 7, 8]
# print(sol.uniqueElements001(A7))


A8 = [2, 6, 3, 9, 8]
B8 = 3
A9 = [1, 1, 7]
B9 = 7
A10 = [2, 8, 3, 7, 8, 7, 9]
B10 = 9
A11 = [4, 1]
B11 = 6
print(sol.minDiff(A11, B11))