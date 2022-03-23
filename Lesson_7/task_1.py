class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        for row in self.matrix:
            print(' '.join(list(map(str, row))))

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for n in range(len(self.matrix[0])):
                result[i].append(self.matrix[i][n] + other.matrix[i][n])
        return '\n'.join(map(str, result))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print(matrix_1 + matrix_2)
