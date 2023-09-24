# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 1

mid = len(arr) // 2
low = 0
high = len(arr) - 1
 
while arr[mid] != n and low <= high:
    if n > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print(-1)
else:
    print("n =", mid)