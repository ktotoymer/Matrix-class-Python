class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

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
        print("minus")

    def __mul__(self, other):
        pass


if __name__ == '__main__':
    mat = [[0 for _ in range(3)] for _ in range(3)]
    mat1 = Matrix(mat)
    print("Hello, world!")
