def printMatrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(A[i][j]),
        print('')


def reverseRow(A):
    l = int(len(A) / 2)
    n = len(A) - 1
    for i in range(l):
        temp = A[i]
        A[i] = A[n - i]
        A[n - i] = temp


class Solution:
    # Q1. Spiral Order Matrix II
    # Problem Description
    # Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
    # Problem Constraints
    # 1 <= A <= 1000
    # Input Format
    # First and only argument is integer A
    # Output Format
    # Return a 2-D matrix which consists of the elements in spiral order.
    # Example Input
    # Input 1:
    #
    # 1
    # Input 2:
    #
    # 2
    #
    #
    # Example Output
    # Output 1:
    #
    # [ [1] ]
    # Output 2:
    #
    # [ [1, 2], [4, 3] ]
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    #
    # Only 1 is to be arranged.
    # Explanation 2:
    #
    # 1 --> 2
    # |
    # |
    # 4<--- 3

    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        print ("method : generateMatrix")
        matrix = [[0 for i in range(A)] for i in range(A)]
        top, left = 0, 0
        bottom, right = A - 1, A - 1
        val = 1
        printMatrix(matrix)
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                # print("i, j, val : ", top, i, val)
                matrix[top][i] = val
                val += 1
            top += 1
            # printMatrix(matrix)
            for i in range(top, bottom + 1):
                print("i, j, val : ", i, right, val)
                matrix[i][right] = val
                val += 1
            right -= 1
            printMatrix(matrix)
            for i in range(right, left - 1, -1):
                # print("i, j, val : ", bottom, i, val)
                matrix[bottom][i] = val
                val += 1
            bottom -= 1
            # printMatrix(matrix)
            for i in range(bottom, top - 1, -1):
                # print("i, j, val : ", i, left, val)
                matrix[i][left] = val
                val += 1
            # printMatrix(matrix)
            left += 1

        printMatrix(matrix)
        return matrix

    # Q2. Rotate Matrix
    # Problem Description
    # You are given a n x n 2D matrix A representing an image.
    #
    # Rotate the image by 90 degrees (clockwise).
    #
    # You need to do this in place.
    #
    # Note: If you end up using an additional array, you will only receive partial score.
    #
    #
    #
    # Problem Constraints
    # 1 <= n <= 1000
    #
    #
    #
    # Input Format
    # First argument is a 2D matrix A of integers
    #
    #
    #
    # Output Format
    # Return the 2D rotated matrix.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # [
    #     [1, 2],
    #     [3, 4]
    # ]
    # Input 2:
    #
    # [
    #     [1]
    # ]
    #
    #
    # Example Output
    # Output 1:
    #
    # [
    #     [3, 1],
    #     [4, 2]
    # ]
    # Output 2:
    #
    # [
    #     [1]
    # ]
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # After rotating the matrix by 90 degree:
    # 1 goes to 2, 2 goes to 4
    # 4 goes to 3, 3 goes to 1
    # Explanation 2:
    #
    # 2D array remains the ssame as there is only element.
    def rotateArray90Clockwise(self, A):
        n = len(A)
        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
        # reverse each row
        for i in range(n):
            reverseRow(A[i])
        printMatrix(A)

    # Q3. Anti Diagonals
    # Problem Description
    # Give a N * N square matrix A, return an array of its anti-diagonals.
    # Look at the example for more details.
    #
    #
    # Problem Constraints
    # 1<= N <= 1000
    # 1<= A[i][j] <= 1e9
    #
    #
    # Input Format
    # First argument is an integer N, denoting the size of square 2D matrix.
    # Second argument is a 2D array A of size N * N.
    #
    #
    # Output Format
    # Return a 2D integer array of size (2 * N-1) * N,
    # representing the anti-diagonals of input array A.
    # The vacant spaces in the grid should be assigned to 0.
    #
    #
    # Example Input
    # Input 1:
    # 3
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Input 2:
    #
    # 1 2
    # 3 4
    #
    #
    # Example Output
    # Output 1:
    # 1 0 0
    # 2 4 0
    # 3 5 7
    # 6 8 0
    # 9 0 0
    # Output 2:
    #
    # 1 0
    # 2 3
    # 4 0
    #
    #
    # Example Explanation
    # For input 1:
    # The first anti diagonal of the matrix is [1 ],
    # the rest spaces should be filled with 0 making the row as [1, 0, 0].
    # The second anti diagonal of the matrix is [2, 4 ],
    # the rest spaces should be filled with 0 making the row as [2, 4, 0].
    # The third anti diagonal of the matrix is [3, 5, 7 ],
    # the rest spaces should be filled with 0 making the row as [3, 5, 7].
    # The fourth anti diagonal of the matrix is [6, 8 ],
    # the rest spaces should be filled with 0 making the row as [6, 8, 0].
    # The fifth anti diagonal of the matrix is [9 ],
    # the rest spaces should be filled with 0 making the row as [9, 0, 0].
    # For input 2:
    #
    # The first anti diagonal of the matrix is [1 ],
    # the rest spaces should be filled with 0 making the row as [1, 0, 0].
    # The second anti diagonal of the matrix is [2, 4 ],
    # the rest spaces should be filled with 0 making the row as [2, 4, 0].
    # The third anti diagonal of the matrix is [3, 0, 0 ],
    # the rest spaces should be filled with 0 making the row as [3, 0, 0].
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        matrix = [[0 for i in range(n)] for i in range(2 * n - 1)]
        for i in range(n):
            row = 0
            col = i
            for j in range(i + 1):
                matrix[i][j] = A[row][col]
                col -= 1
                row += 1
        for i in range(n, 2 * n - 1):
            row = i - n + 1
            col = n - 1
            for j in range(2 * n - 1 - i):
                matrix[i][j] = A[row][col]
                col -= 1
                row += 1
        return matrix

    # Q4. Pascal Triangle
    # Problem Description
    #
    # Write a program to input an integer N from user and print pascal triangle up to N rows.
    # Problem Constraints
    # 1 <= N <= 25
    # Input Format
    # First line is an integer N.
    # Output Format
    #
    # N lines whose each row contains N+1 space separated integers.
    # Example Input
    #
    # Input 1:
    #
    # 3
    # Input 2:
    #
    # 5
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # 1 0 0
    # 1 1 0
    # 1 2 1
    # Output 2:
    #
    # 1 0 0 0 0
    # 1 1 0 0 0
    # 1 2 1 0 0
    # 1 3 3 1 0
    # 1 4 6 4 1
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # Row 1 = 1 0 0 0 0
    # Row 2 = 1C0 1C1 0 0 0= 1 1 0 0 0
    # Row 3 = 2C0 2C1 2C2 0 0= 1 2 1 0 0
    # Row 4 = 3C0 3C1 3C2 3C3 0= 1 3 3 1 0
    def pascalTriangle(self, A):
        matrix = [[0 for i in range(A)] for i in range(A)]
        if A < 1:
            return matrix
        matrix[0][0] = 1
        for i in range(1, A):
            matrix[i][0] = 1
            for j in range(1, i):
                matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]
            matrix[i][i] = 1
        return matrix

    # Q5. Row with maximum number of ones
    # Problem Description
    # Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
    #
    # NOTE:
    #
    # If two rows have the maximum number of 1 then return the row which has a lower index.
    # Rows are numbered from top to bottom and columns are numbered from left to right.
    # Assume 0-based indexing.
    # Assume each row to be sorted by values.
    # Expected time complexity is O(rows).
    #
    #
    # Problem Constraints
    #
    # 1 <= N <= 1000
    #
    # 0 <= A[i] <= 1
    #
    #
    #
    # Input Format
    #
    # The only argument given is the integer matrix A.
    #
    #
    #
    # Output Format
    #
    # Return the row with the maximum number of 1.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = [   [0, 1, 1]
    #         [0, 0, 1]
    #         [0, 1, 1]   ]
    # Input 2:
    #
    # A = [   [0, 0, 0, 0]
    #         [0, 1, 1, 1]    ]
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # 0
    # Output 2:
    #
    # 1
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # Row 0 has maximum number of 1s.
    # Explanation 2:
    #
    # Row 1 has maximum number of 1s.
    def getRowWithMaxOnes(self, A):
        n = len(A)
        row = -1
        # check the first row having atleast single 1
        for i in range(n):
            if A[i][n - 1] == 1:
                row = i
                break
        # if no 1s found, return -1
        if row == -1:
            return -1

        colVal = n - 1
        while A[i][colVal] == 1:
            colVal -= 1
        for i in range(1, n):
            while A[i][colVal] == 1 and colVal>=0:
                colVal -= 1
                row = i
        return row



sol = Solution()
# matrix = sol.generateMatrix(5)
# printMatrix(matrix)
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
# print (sol.generateMatrix(5))
# print(sol.rotateArray90Clockwise(matrix))

# print(sol.diagonal(matrix))
# print(sol.pascalTriangle(5))
A1 = [[0, 1, 1],
      [0, 0, 1],
      [0, 1, 1]]
A2 = [[0, 0, 0, 0],
      [0, 1, 1, 1]]
A3 = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]]

print("getRowWithMaxOnes : ", sol.getRowWithMaxOnes(A3))
