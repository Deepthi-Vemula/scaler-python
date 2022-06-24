class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        prefixSum = [0 for i in range(n)]
        sumHashMap = {}
        maxLen = 0
        for i in range(n):
            if A[i] == 0:
                A[i] = -1
            if i == 0:
                prefixSum[i] = A[0]
            else:
                prefixSum[i] = prefixSum[i-1] + A[i]
            #check if there are equal number of 0s and 1s
            # 1 - if prefixSum = 0
            # 2 - if prefixSum[i] == prefixSum[j]
            if prefixSum[i] == 0:
                print("0 present at ", i)
                maxLen = max(maxLen, i+1)
            elif prefixSum[i] in sumHashMap.keys():
                print("same sum present at ", i, prefixSum[i])
                maxLen = max(maxLen, (i - sumHashMap[prefixSum[i]]))
            else:
                sumHashMap[prefixSum[i]] = i
            print(sumHashMap)
            print("\t\t maxlen for index ",i, maxLen)
            
        print(prefixSum)
        print(A)
        return maxLen  


sol = Solution()
A = [1, 0, 1, 0, 1]
A1 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]

print(sol.solve(A1)) 