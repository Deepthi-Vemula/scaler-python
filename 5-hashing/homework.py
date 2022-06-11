from numpy.oldnumeric.alter_code1 import char


def checkFrequencies(B, A):
    for i in range(len(B)):
        if B[i] != A[i]:
            return False
    return True


class Solution:
    # Q1. Permutations of A in B
    # Problem Description
    # You are given two strings, A and B, of size N and M, respectively.
    #
    # You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.
    #
    #
    #
    # Problem Constraints
    # 1 <= N < M <= 105
    #
    #
    #
    # Input Format
    # Given two arguments, A and B of type String.
    #
    #
    #
    # Output Format
    # Return a single integer, i.e., number of permutations of A present in B as a substring.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = "abc"
    # B = "abcbacabc"
    # Input 2:
    #
    # A = "aca"
    # B = "acaa"
    #
    #
    # Example Output
    # Output 1:
    #
    # 5
    # Output 2:
    #
    # 2
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Permutations of A that are present in B as substring are:
    # 1. abc
    # 2. cba
    # 3. bac
    # 4. cab
    # 5. abc
    # So ans is 5.
    # Explanation 2:
    #
    # Permutations of A that are present in B as substring are:
    # 1. aca
    # 2. caa
    # @param A : string
    # @param B : string
    # @return an integer
    # the following implementation is TLE - still want to retain it here
    def permutationsOfAInB(self, A, B):
        lenB = len(B)
        lenA = len(A)
        if lenA > lenB or lenB == 0 or lenA == 0:
            print("len exceeded")
            print("lengths A, B", lenA, lenB)
            return 0
        wipStr = ""
        if lenA > 1:
            wipStr = B[0:lenA - 1]
        A = ''.join(sorted(A))
        # print("sorted small string ", A)
        hashVal = hash(A)
        count = 0
        for i in range(lenA - 1, lenB):
            wipStr += B[i]
            substr = ''.join(sorted(wipStr))
            # print("for index", i, " substr ", substr)
            if hash(substr) == hashVal:
                count += 1
            wipStr = wipStr[1:]
        return count

    def perms2(self, A, B):
        lenB = len(B)
        lenA = len(A)
        letterFreqA = [0 for i in range(26)]
        letterFreqB = [0 for i in range(26)]
        offsetVal = ord("a")
        if lenA > lenB or lenB == 0 or lenA == 0:
            return 0
        for i in range(lenA):
            letterFreqA[ord(A[i]) - offsetVal] += 1
            if i < lenA - 1:
                letterFreqB[ord(B[i]) - offsetVal] += 1
        count = 0
        for i in range(lenA - 1, lenB):
            letterFreqB[ord(B[i]) - offsetVal] += 1
            # check for frequencies match
            if checkFrequencies(letterFreqB, letterFreqA):
                count += 1
            # print ("val to be deleted : ", i-lenA+1, B[i-lenA+1])
            letterFreqB[ord(B[i - lenA + 1]) - offsetVal] -= 1
        return count

    # Q2. Valid Sudoku
    # Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

    # The Sudoku board could be partially filled, where empty cells are filled with the character .
    # The input corresponding to the above configuration :
    #
    # ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
    # A partially filled sudoku which is valid.
    #
    # Note:
    #
    # A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
    # Return 0 / 1 ( 0 for false, 1 for true ) for this problem
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        # validate rows
        # validate columns
        # validate boxes - 3x3 matrices
        sudokuSize = len(A)
        # for i in range(sudokuSize):
        #     for j in range(sudokuSize):
        #         print(A[i][j]),
        #     print()
        # if len(A) != sudokuSize:
        #     return False
        # rows
        for i in range(sudokuSize):
            hashVals = {}
            for j in range(sudokuSize):
                if A[i][j] == '.':
                    continue
                if A[i][j] in hashVals.keys():
                    return 0
                if '0' <= A[i][j] <= '9':
                    hashVals[A[i][j]] = 1
            # print("for row", i, hashVals)
        # columns
        for i in range(sudokuSize):
            hashVals = {}
            for j in range(sudokuSize):
                if A[j][i] == '.':
                    continue
                if A[j][i] in hashVals.keys():
                    return 0
                if '0' <= A[j][i] <= '9':
                    hashVals[A[j][i]] = 1
            # print("for column", i, hashVals)
        boxStartIndices = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for box in range(len(boxStartIndices)):
            hashVals = {}
            for i in range(3):
                for j in range(3):
                    xVal = boxStartIndices[box][0] + i
                    yVal = boxStartIndices[box][1] + j
                    if A[xVal][yVal] == '.':
                        continue
                    if A[xVal][yVal] in hashVals.keys():
                        return False
                    hashVals[A[xVal][yVal]] = 1
        return 1


A = "p"
B = "pccdpeeooadeocdoacddapacaecb"

A1 = "ebbp"
B1 = "qaoedpcebeaqocbacoccqoebpqdoqcpbdbqcecdoqcpebqpebbabqdpepcpbqbepbabocpc"

A2 = "abc"
B2 = "abcbacabc"

sol = Solution()
# print(sol.perms2(A2, B2))

# A3 = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
# A3 = "9 ....5..1. .4.3..... .....3..1 8......2. ..2.7.... .15...... .....2... .2.9..... ..4......"
A3 = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
      "....8..79"]
print (sol.isValidSudoku(A3))
