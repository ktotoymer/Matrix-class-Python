from Matrix import *

if __name__ == '__main__':
    mat = [[3 for _ in range(3)] for _ in range(3)]
    mat1 = Matrix([[3 for _ in range(3)] for _ in range(3)])
    mat2 = Matrix([[1 for _ in range(3)] for _ in range(3)])
    print(mat1 - mat2)
    print("Hello, world!")
