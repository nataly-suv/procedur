import math

arr_x = [12, 56, 48, 23, 96, 12, 14, 54, 78, 53, 56, 77, 11]
arr_y = [21, 65, 85, 24, 105, 132, 54, 51, 79, 153, 22, 8, 45]

def koef_pirsone(arr_x, arr_y):
    arg_x = sum(arr_x)/len(arr_x)
    arg_y = sum(arr_y)/len(arr_y)
    print (arg_x, arg_y)
    def numerator():                
        return sum(map(lambda x, y: (x-arg_x)*(y-arg_y), arr_x, arr_y))

    def denominator():
        return  math.sqrt(sum(map(lambda x, y: (x-arg_x)**2*(y-arg_y)**2, arr_x, arr_y)))

    return numerator()/denominator()

print(koef_pirsone(arr_x, arr_y))