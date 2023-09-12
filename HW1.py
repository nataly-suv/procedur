# Дан список целых чисел numbers.
# Необходимо написать процедуру для
# сортировки числа в списке в порядке убывания.

array = [5, -6, 0, 8, 15, -7, 54]
array2 = [5, -6, 0, 8, 15, -7, 54]

# Императивный подход
def sort_list_imperativ(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
print('Императивный подход')
print(sort_list_imperativ(array))
print()

# Декларативный подход
def sort_list_declarativ(arr):
    arr.sort(reverse=True)
    return arr

print('Декларативный подход')
print(sort_list_declarativ(array2))
