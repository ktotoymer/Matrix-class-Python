class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        result = []
        if isinstance(other, Matrix):
            if self.m == other.m and self.n == other.m:
                for i in range(len(self.matrix)):
                    row = []
                    for j in range(len(self.matrix[0])):
                        row.append(self.matrix[i][j] + other.matrix[i][j])
                    result.append(row)
            else:
                print("Операция сложения для данных матриц не допустима")
        elif isinstance(other, int):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other)
                result.append(row)
        else:
            ValueError("")
        return Matrix(result)

    def __sub__(self, other):
        result = []
        if isinstance(other, Matrix):
            if self.m == other.m and self.n == other.m:
                for i in range(len(self.matrix)):
                    row = []
                    for j in range(len(self.matrix[0])):
                        row.append(self.matrix[i][j] - other.matrix[i][j])
                    result.append(row)
            else:
                print("Операция сложения для данных матриц не допустима")
        elif isinstance(other, int):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] - other)
                result.append(row)
        else:
            ValueError("")
        return Matrix(result)

    def __mul__(self, other):
        result = []
        if isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    element = 0
                    for k in range(len(self.matrix[0])):
                        element += self.matrix[i][k] * other.matrix[k][j]
                    row.append(element)
                result.append(row)
        elif isinstance(other, int):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other)
                result.append(row)
        else:
            ValueError("")
        return Matrix(result)


class SquareMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)
        if self.m != self.n:
            raise ValueError("SquareMatrix должна быть квадратной матрицей")


class IdentityMatrix(SquareMatrix):
    def __init__(self, n):
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 1
        super().__init__(matrix)


class StepMatrix(Matrix):
    def __init__(self, m, n, step):
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j:
                    matrix[i][j] = step
        super().__init__(matrix)
