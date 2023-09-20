print("Task 1")
arr = [1, 5, 6, 7, 8, 10]

def normalaiz(arr):
    max_el = max(arr)
    min_el = min(arr)

    def norm_el(x):
        return (x-min_el)/(max_el - min_el)

    return list(map(norm_el, arr))

print(normalaiz(arr))

print("Task 2")
arr1 = [1, 5, 31, 55, 41, 12, 58, 33]
n=30
def count_person(arr1, n):
    return list(filter(lambda x: x > n, arr1))

print(len(count_person(arr1, n)))

print("Task 3")

arr2 = [1, 5, 4, 1, 9, 7, 8, 6, 1]
def double_data(arr2):
    one_set = set()
    return list(filter(lambda x: x in one_set or one_set.add(x), arr2))

print(double_data(arr2))