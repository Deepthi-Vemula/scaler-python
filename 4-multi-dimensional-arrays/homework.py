class Homework:
    # Q1. Search in a row wise and column wise sorted matrix
    # Problem Description
    #
    # Given a matrix of integers A of size N x M and an integer B.
    # In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix in the given form:
    # If A[i][j] = B then return (i * 1009 + j)
    # If B is not present return -1.
    #
    # Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
    # Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
    #
    #
    # Problem Constraints
    #
    # 1 <= N, M <= 1000
    # -100000 <= A[i] <= 100000
    # -100000 <= B <= 100000
    #
    #
    # Input Format
    #
    # The first argument given is the integer matrix A.
    # The second argument given is the integer B.
    #
    #
    # Output Format
    #
    # Return the position of B and if it is not present in A return -1 instead.
    #
    #
    # Example Input
    #
    # A = [ [1, 2, 3]
    #       [4, 5, 6]
    #       [7, 8, 9] ]
    # B = 2
    #
    #
    # Example Output
    #
    # 1011
    #
    #
    # Example Explanation
    #
    # A[1][2]= 2
    # 1*1009 + 2 =1011
    def searchInSortedMatrix(self, A, B):
        #check closest value in row 1
        const = 1009
        rows = len(A)
        columns = len(A[0])
        col = -1
        print("r,c : ", rows, columns)
        for i in range(columns):
            if A[0][i] == B:
                col = i
                break
            elif A[0][i] < B:
                col = i
            else:
                break
        print("col val after row 1 : ", col)
        if col == -1:
            return -1
        elif A[0][col] == B:
            print("r,c : ", 0, col)
            return const + col + 1

        for i in range(1, rows):
            if A[i][col] > B:
                while A[i][col] > B and col > 0:
                    col -= 1
            elif A[i][col] < B:
                while A[i][col] < B and col < columns-1:
                    col += 1
            print ("col val after row", i, "is", col, A[i][col])
            if A[i][col] == B:
                print("r,c : ", i, col)
                return (i+1)*const + (col+1)


        return -1



A1 = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]
A2 = [[1, 3, 5, 7, 16],
      [2, 7, 10, 15, 20],
      [5, 12, 18, 31, 42],
      [17, 19, 29, 34, 56]]
hw = Homework()
B = 2
# print("search", B, " in sorted matrix ", A, hw.searchInSortedMatrix(A, B))
B2 = 56

A3 =[[2, 8, 8, 8],
    [2, 8, 8, 8],
    [2, 8, 8, 8]]
B3 = 8
print("search", B2, " in sorted matrix is ", hw.searchInSortedMatrix(A2, B2))

