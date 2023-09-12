# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится ли target в array.
# Такую процедуру будем называть поиском.

arr = [1, 2, 3, 4]
target = 3


def one(array, n):
    for number in array:
        if number == n:
            return True
    return False


print(f"Task one:  {one(arr, target)}")


def two(arr, target):
    return target in arr


print(f"Task two:  {two(arr, target)}")


# Условие
# На вход подается: список целых чисел arr
# Задача
# Реализовать императивную функцию, которая возвращает три числа:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел

arr2 = [0, 1, -5, 10, -6, 56, 0]

positiv = 0
negativ = 0
nyl = 0


def task_3(arr):
    numbers = [0, 0, 0]
    for number in arr:
        if (number < 0):
            numbers[0] += 1
        elif (number == 0):
            numbers[1] += 1
        elif (number > 0):
            numbers[2] += 1
    print("Task three:")

    print(numbers[0]/len(arr))
    print(numbers[1]/len(arr))
    print(numbers[2]/len(arr))


task_3(arr2)


def task_3_2(arr):
    oneN = len(list(filter(lambda n: n > 0, arr)))
    twoN = len(list(filter(lambda n: n == 0, arr)))
    treeN = len(list(filter(lambda n: n < 0, arr)))
    # dictOne= [oneN, twoN, treeN]
    print("Task three (part two):")
    counts=[oneN, twoN, treeN]
    # print(oneN/len(arr))
    # print(twoN/len(arr))
    # print(treeN/len(arr))
    return list(map(lambda count: count/len(arr), counts))

print(task_3_2(arr2))






