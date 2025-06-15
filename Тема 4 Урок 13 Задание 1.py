import random


def generate_matrix(rows, cols, min_val=-100, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера")

    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
            for i in range(len(matrix1))]


def print_matrix(matrix):
    for row in matrix:
        print(row)



matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

print("Матрица 1:")
print_matrix(matrix_1)
print("\nМатрица 2:")
print_matrix(matrix_2)


matrix_3 = add_matrices(matrix_1, matrix_2)
print("\nРезультат сложения (Матрица 3):")
print_matrix(matrix_3)


small_matrix_1 = generate_matrix(4, 3)
small_matrix_2 = generate_matrix(4, 3)

print("\nМаленькая матрица 1:")
print_matrix(small_matrix_1)
print("\nМаленькая матрица 2:")
print_matrix(small_matrix_2)

small_matrix_3 = add_matrices(small_matrix_1, small_matrix_2)
print("\nРезультат сложения маленьких матриц:")
print_matrix(small_matrix_3)