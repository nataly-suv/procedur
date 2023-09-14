# След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
# (количество столбцов = количеству строк).

# ● Задача
# Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
trace = 0

for i in range(len(matrix)):
    trace += matrix[i][i]

print(f"Задача 1. Вариант 1:  {trace}")


trace2 = 0

for i, row in enumerate(matrix):
    for j, el in enumerate(row):
        if i == j:
            trace2 += el
print(f"Задача 1. Вариант 2:  {trace}")


print()


# Добавить процедурную парадигму в имеющуюся реализацию вычисления следа

def get_trace(matrix):
    trace3 = 0
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if i == j:
                trace3 += el
    return trace3


print(f"Задача 1. Вариант 3:  {trace}")


print()


# На вход подается число в десятичной системе счисления
# ● Задача
# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную
# систему счисления. Обоснуйте сделанный выбор парадигм.

decimal = 10

def decumal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


binary = decumal_to_binary(decimal)
print('Задача 2')
print(binary)
