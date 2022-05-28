class ClassHomeWork:
    def __init__(self):
        pass

    def printSpiralMatrix(self, matrix):
        top, left = 0, 0
        A = len(matrix)
        bottom, right = A - 1, A - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                print(matrix[top][i]),
            top += 1
            for i in range(top, bottom + 1):
                print(matrix[i][right]),
            right -= 1
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i]),
            bottom -= 1
            # print("bottom, top: ", bottom, top)
            for i in range(bottom, top - 1, -1):
                # print("i, j: ", i, left)
                print(matrix[i][left]),
            left += 1
        print ('')

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
sol = ClassHomeWork()
print (sol.printSpiralMatrix(matrix))
