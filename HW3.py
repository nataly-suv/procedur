# Крестики-нолики
from colorama import init, Fore
from colorama import Back
from colorama import Style

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]

# метод печати игрвого поля
def print_fild(arr1, arr2, arr3):
    print(Fore.RED + "Игровое поле:")
    print(Style.RESET_ALL)
    print(f"{arr1[0]} | {arr1[1]} | {arr1[2]}")
    print("----------")
    print(f"{arr2[0]} | {arr2[1]} | {arr2[2]}")
    print("----------")
    print(f"{arr3[0]} | {arr3[1]} | {arr3[2]}")
    print(Fore.RED + "Для выхода введите end")
    print(Style.RESET_ALL)


# метод заполнения поля
def fill_fild(num_cell, marker):
    if num_cell == 1:
        arr1[0] = marker
    elif num_cell == 2:
        arr1[1] = marker
    elif num_cell == 3:
        arr1[2] = marker
    elif num_cell == 4:
        arr2[0] = marker
    elif num_cell == 5:
        arr2[1] = marker
    elif num_cell == 6:
        arr2[2] = marker
    elif num_cell == 7:
        arr3[0] = marker
    elif num_cell == 8:
        arr3[1] = marker
    elif num_cell == 9:
        arr3[2] = marker


#  метод проверки выйгрыша
def check_win():
    if arr1[0] == arr1[1] == arr1[2]:        
        return True
    elif arr2[0] == arr2[1] == arr2[2]:
        return True
    elif arr3[0] == arr3[1] == arr3[2]:
        return True
    elif arr1[0] == arr2[1] == arr3[2]:
        return True
    elif arr1[2] == arr2[1] == arr3[0]:
        return True
    elif arr1[0] == arr2[0] == arr3[0] or arr1[1] == arr2[1] == arr3[1] or arr1[2] == arr2[2] == arr3[2]:
        return True
    else:  
        return False

# метод хода игрока
def player(count):
    if (count % 2):
        num_cell = int(input("Игрок Х введите номер игрового поля для заполенения: "))
        fill_fild(num_cell, "X")
        count = count + 1
        return count
    else:
        num_cell = int(input("Игрок O введите номер игрового поля для заполенения: "))
        fill_fild(num_cell, "O")  
        count = count + 1
        return count



print_fild(arr1, arr2, arr3)
count =1

while not check_win():
    try:
        count = player(count)
        print_fild(arr1, arr2, arr3)
    except:
        print("Вы закончили игру")
        break

if (check_win()):
    print("Уры, вы победили!")


# исопльзовала императивную структурную и  процедурную парадигмы
