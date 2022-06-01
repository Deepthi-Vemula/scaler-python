class Solution:
    # Q1. 2 Sum
    # Problem Description
    #
    # Given an array of integers, find two numbers such that they add up to a specific target number.
    #
    # The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.
    #
    # If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.
    #
    # Input: [2, 7, 11, 15], target=9
    # Output: index1 = 1, index2 = 2
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        # Python dictionary is a built-in type that supports key-value pairs.
        hashVal = {}
        index = []
        for i in range(len(A)):
            if (B - A[i]) in hashVal.keys():
                index.append(hashVal[B - A[i]])
                index.append(i + 1)
                break
            elif A[i] not in hashVal.keys():
                hashVal[A[i]] = i + 1
        return index

    #Q2. Common Elements
    #Problem Description
    # Given two integer arrays, A and B of size N and M, respectively.
    # Your task is to find all the common elements in both the array.
    #
    # NOTE:
    #
    # Each element in the result should appear as many times as it appears in both arrays.
    # The result can be in any order.
    #
    #
    # Problem Constraints
    # 1 <= N, M <= 105
    #
    # 1 <= A[i] <= 109
    #
    #
    #
    # Input Format
    # First argument is an integer array A of size N.
    #
    # Second argument is an integer array B of size M.
    #
    #
    #
    # Output Format
    # Return an integer array denoting the common elements.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 2, 2, 1]
    # B = [2, 3, 1, 2]
    # Input 2:
    #
    # A = [2, 1, 4, 10]
    # B = [3, 6, 2, 10, 10]
    #
    #
    # Example Output
    # Output 1:
    #
    # [1, 2, 2]
    # Output 2:
    #
    # [2, 10]
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
    # Explantion 2:
    #
    # Elements (2, 10) appears in both the array.
    def findCommonElements(self, A, B):
        common = []
        hashVal = {}
        for el in A:
            if el in hashVal.keys():
                hashVal[el] += 1
            else:
                hashVal[el] = 1
        for el in B:
            if el in hashVal.keys():
                if hashVal[el] == 1:
                    hashVal.pop(el)
                else:
                    hashVal[el] -= 1
                common.append(el)
        return common


    # Q3. Pairs With Given Xor
    # Problem Description
    # Given an integer array A containing N distinct integers.
    #
    # Find the number of unique pairs of integers in the array whose XOR is equal to B.
    #
    # NOTE:
    #
    # Pair (a, b) and (b, a) is considered to be the same and should be counted once.
    #
    #
    # Problem Constraints
    # 1 <= N <= 105
    #
    # 1 <= A[i], B <= 107
    #
    #
    #
    # Input Format
    # The first argument is an integer array A.
    #
    # The second argument is an integer B.
    #
    #
    #
    # Output Format
    # Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [5, 4, 10, 15, 7, 6]
    # B = 5
    # Input 2:
    #
    # A = [3, 6, 8, 10, 15, 50]
    # B = 5
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 2
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # (10 ^ 15) = 5
    # Explanation 2:
    #
    # (3 ^ 6) = 5 and (10 ^ 15) = 5
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def getPairWithGivenXOR(self, A, B):
        pairCount = 0
        hashVal = {}
        for i in range(len(A)):
            if (B ^ A[i]) in hashVal.keys():
                pairCount += 1
                hashVal.pop(B^A[i])
            elif A[i] not in hashVal.keys():
                hashVal[A[i]] = i + 1
        return pairCount



sol = Solution()
A1 = [2, 6, 7, 11, 15, 3]
A2 = [2, 3, 4, 5, 6]
B2 = 1
B1 = 9
A3 = [5, 3, 14, 23, 18, 89, 5, 7]
B3 = 10
A4 = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B4 = -3
print(sol.twoSum(A4, B4))
