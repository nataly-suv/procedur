import math

arr = [2, 5, 2, 8, 9, 23, 6]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    arr_result = []
    i_left = 0
    i_right = 0
    while len(left) > i_left and len(right) > i_right:
        if left[i_left] > right[i_right]:
            arr_result.append(right[i_right])
            i_right += 1
        else:
            arr_result.append(left[i_left])
            i_left += 1
    while len(left) > i_left:
        arr_result.append(left[i_left])
        i_left += 1
    while len(right) > i_right:
        arr_result.append(right[i_right])
        i_right += 1
    return arr_result


print(merge_sort(arr))

print()
print("Task 2")
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]


def mse(arr1, arr2):
    if len(arr1) == len(arr2):
        return sum(map(lambda x, y: (x-y)**2, arr1, arr2))/len(arr1)
    else:
        return -1


print(mse(arr1, arr2))

print()
print("Task 3")

arr4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 2
i_min = 0
i_max = len(arr4)-1


def search(arr4, n, i_min, i_max):

    if i_min > i_max:
        return -1
    mid = (i_max + i_min) // 2 
    if arr4[mid] == n:
        return mid
    elif arr4[mid] > n:
        return search(arr4, n, i_min, mid-1)
    elif arr4[mid] < n:
        return search(arr4, n, mid+1, i_max)
    
    

print(search(arr4, n, i_min, i_max))

# def binary_search(arr, left, right, n):
#     if left > right:
#         return -1    
#     mid = (left + right) // 2    
#     if arr[mid] == n:
#         return mid
#     elif arr[mid] < n:
#         return binary_search(arr, mid + 1, right, n)
#     else:
#         return binary_search(arr, left, mid - 1, n)


# arr1 = [2, 4, 6, 8, 10, 12, 14]
# n = 5
# print(binary_search(arr1, 0, len(arr1)-1, n))