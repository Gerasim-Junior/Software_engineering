import random


def generate_random_matrix(rows, cols):
    """Генерация матрицы случайными числами от 1 до 10"""
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """Вывод матрицы в консоль"""
    for row in matrix:
        print(row)


def matrix_addition(matrix1, matrix2):
    """Сложение матриц"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: Размеры матриц не совпадают для сложения.")
        return None
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def matrix_subtraction(matrix1, matrix2):
    """Вычитание матриц"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: Размеры матриц не совпадают для вычитания.")
        return None
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrix_by_number(matrix, number):
    """Умножение матрицы на число"""
    return [[matrix[i][j] * number for j in range(len(matrix[0]))] for i in range(len(matrix))]


def matrix_trace(matrix):
    """Вычисление следа матрицы (сумма элементов главной диагонали)"""
    if len(matrix) != len(matrix[0]):
        print("Ошибка: След можно вычислить только у квадратной матрицы.")
        return None
    return sum(matrix[i][i] for i in range(len(matrix)))


def get_positive_integer(prompt):
    """Запрос положительного целого числа у пользователя"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: Введите положительное целое число.")
        except ValueError:
            print("Ошибка: Введите целое число.")


def get_integer(prompt):
    """Запрос целого числа у пользователя"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")


def input_matrix(rows, cols):
    """Ввод матрицы пользователем"""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(get_integer(f"({i + 1},{j + 1}): "))
        matrix.append(row)
    return matrix


def main():
    print("1. Заполнить матрицы случайными числами")
    print("2. Ввести матрицы вручную")

    while True:
        choice = get_integer("Введите ваш выбор (1 или 2): ")
        if choice in [1, 2]:
            break
        print("Ошибка: Введите 1 или 2.")

    print("\nВведите размеры первой матрицы:")
    rows1 = get_positive_integer("Количество строк: ")
    cols1 = get_positive_integer("Количество столбцов: ")

    print("\nВведите размеры второй матрицы:")
    rows2 = get_positive_integer("Количество строк: ")
    cols2 = get_positive_integer("Количество столбцов: ")

    if choice == 1:
        matrix1 = generate_random_matrix(rows1, cols1)
        matrix2 = generate_random_matrix(rows2, cols2)
    else:
        print("\nМатрица 1:")
        matrix1 = input_matrix(rows1, cols1)
        print("\nМатрица 2:")
        matrix2 = input_matrix(rows2, cols2)

    print("\nМатрица 1:")
    print_matrix(matrix1)
    print("\nМатрица 2:")
    print_matrix(matrix2)

    print("\nСложение матриц:")
    result = matrix_addition(matrix1, matrix2)
    if result:
        print_matrix(result)

    print("\nВычитание матриц:")
    result = matrix_subtraction(matrix1, matrix2)
    if result:
        print_matrix(result)

    num_1 = get_integer("\nВведите число для умножения первой матрицы: ")
    num_2 = get_integer("\nВведите число для умножения второй матрицы: ")
    print("\nМатрица 1, умноженная на число:")
    print_matrix(multiply_matrix_by_number(matrix1, num_1))
    print("\nМатрица 2, умноженная на число:")
    print_matrix(multiply_matrix_by_number(matrix2, num_2))

    if rows1 == cols1:
        print("\nСлед первой матрицы:")
        trace = matrix_trace(matrix1)
        if trace is not None:
            print(trace)

    if rows2 == cols2:
        print("\nСлед второй матрицы:")
        trace = matrix_trace(matrix2)
        if trace is not None:
            print(trace)

if __name__ == "__main__":
    main()