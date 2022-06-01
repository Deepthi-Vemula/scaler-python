class Solution:

    # Q1. Subarray with given sum
    # Problem Description
    # Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
    #
    # If the answer does not exist return an array with a single element "-1".
    #
    # First sub-array means the sub-array for which starting index in minimum.
    #
    # Problem Constraints
    # 1 <= length of the array <= 100000
    # 1 <= A[i] <= 109
    # 1 <= B <= 109
    #
    # Input Format
    # The first argument given is the integer array A.
    #
    # The second argument given is integer B.
    #
    # Output Format
    # Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 2, 3, 4, 5]
    # B = 5
    # Input 2:
    #
    # A = [5, 10, 20, 100, 105]
    # B = 110
    #
    #
    # Example Output
    # Output 1:
    #
    # [2, 3]
    # Output 2:
    #
    # -1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # [2, 3] sums up to 5.
    # Explanation 2:
    #
    # No subarray sums up to required number.
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def findSubArrayWithGivenSum(self, A, B):
        hashMap = {}
        prefixSum = 0
        for i in range(len(A)):
            prefixSum += A[i]
            hashMap[prefixSum] = i+1
            print(prefixSum, i+1)
            if prefixSum == B:
                return A[:i+1]
            if (prefixSum - B) in hashMap.keys():
                return A[hashMap[prefixSum - B]:i+1]
        return [-1]

    # Q2. Sub-array with 0 sum
    # Problem Description
    # Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
    #
    # If the given array contains a sub-array with sum zero return 1, else return 0.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 100000
    #
    # -10^9 <= A[i] <= 10^9
    #
    #
    #
    # Input Format
    # The only argument given is the integer array A.
    #
    #
    #
    # Output Format
    # Return whether the given array contains a subarray with a sum equal to 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 2, 3, 4, 5]
    # Input 2:
    #
    # A = [-1, 1]
    #
    #
    # Example Output
    # Output 1:
    #
    # 0
    # Output 2:
    #
    # 1
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # No subarray has sum 0.
    # Explanation 2:
    #
    # The array has sum 0.
    # @param A : list of integers
    # @return an integer
    def getSubarrayWithZeroSum(self, A):
        hashMap = {}
        prefixSum = 0
        for i in range(len(A)):
            prefixSum += A[i]
            if (prefixSum in hashMap.keys()) or prefixSum == 0:
                return 1
            hashMap[prefixSum] = i+1
        return 0

    # Q3. Equal
    # Problem Description
    # Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P, Q, R & S are integers values in the array
    #
    # Expected time complexity O(N2)
    #
    # NOTE:
    #
    # 1) Return the indices `A1 B1 C1 D1`, so that
    # A[A1] + A[B1] = A[C1] + A[D1]
    # A1 < B1, C1 < D1
    # A1 < C1, B1 != D1, B1 != C1
    #
    # 2) If there are more than one solutions, \
    #                               then return the tuple of values which are lexicographical smallest.
    #
    # Assume we have two solutions
    # S1 : A1 B1 C1 D1 ( these are values of indices in the array )
    # S2 : A2 B2 C2 D2
    #
    # S1 is lexicographically smaller than S2 if:
    # A1 < A2 OR
    # A1 = A2 AND B1 < B2 OR
    # A1 = A2 AND B1 = B2 AND C1 < C2 OR
    # A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
    # If no solution is possible, return an empty list.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 1000
    #
    # 0 <= A[i] <= 1000
    #
    #
    #
    # Input Format
    # First and only argument is an integer array A of length N.
    #
    #
    #
    # Output Format
    # Return an array of size four which contains indices of values P, Q, R, and S.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [3, 4, 7, 1, 2, 9, 8]
    # Input 2:
    #
    # A = [2, 5, 1, 6]
    #
    #
    # Example Output
    # Output 1:
    #
    # [0, 2, 3, 5]
    # Output 2:
    #
    # [0, 1, 2, 3]
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # A[0] + A[2] = A[3] + A[5]
    # Note: indexes returned should be 0-based.
    # Explanation 2:
    #
    # A[0] + A[1] = A[2] + A[3]
    # @param A : list of integers
    # @return a list of integers



    def isCurrentAnsLexSmaller(self, PrevAnswer, CurrentAnswer):
        print("isCurrentAnsLexSmaller: prev, curr ", PrevAnswer, CurrentAnswer)
        for i in range(len(PrevAnswer)):
            if PrevAnswer[i] < CurrentAnswer[i]:
                return False
            if PrevAnswer[i] > CurrentAnswer[i]:
                return True
        return False

    def isCurrentValid(self, CurrentAnswer):
        if CurrentAnswer[0] == CurrentAnswer[2] or CurrentAnswer[0] == CurrentAnswer[3] or CurrentAnswer[1] == CurrentAnswer[2] or CurrentAnswer[1] == CurrentAnswer[3]:
            return False
        return True


    def equal(self, A):
        sumHashMap = {}
        answer = []
        l = int((len(A)*(len(A)-1))/2)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if (A[i]+A[j]) in sumHashMap.keys():
                    tempAns = sumHashMap[A[i]+A[j]] + [i, j]
                    if self.isCurrentValid(tempAns) and (len(answer) == 0 or self.isCurrentAnsLexSmaller(answer, tempAns)) :
                        answer = tempAns
                else:
                    sumHashMap[A[i]+A[j]] = [i, j]
        return answer


A = [1, 2, 3, 4, 5]
B = 5

A1 = [5, 10, 20, 100, 105]
B1 = 110

A2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
B2 = 15
sol = Solution()
# print(sol.findSubArrayWithGivenSum(A2, B2))

A3 = [1, 2, 3, 4, 5]
A4 = [-1, 1]
# print(sol.getSubarrayWithZeroSum(A4))

A5 = [3, 4, 7, 1, 2, 9, 8]
A6 = [2, 5, 1, 6]
A7 = [5, 5, 5, 5, 5, 5, 5]
A8 = [1, 1, 1, 1, 1]
print (sol.equal(A8))


