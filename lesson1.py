# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# string = input('enter string')
# print(string)
# # string = 'as 23 fdfdg544'
# print(','.join([ch for ch in string if ch.isdigit()]))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# print(','.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# greeting = 'Hello, world'
# print([ch for ch in greeting.upper()])


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# print([i** 2 for i in range(50) if i % 2])


# function
#
# - створити функцію яка виводить ліст
# def show(some_list):
#     for i in some_list:
#         print(i)
#
#
# show([2, 345, 6, 1, 4, 6, 3, 66])

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def show_max_number(a, b, c):
#     return print(max(a, b, c))
#
#
# show_max_number(2, 4, 2)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def return_min_show_max(*args):
#     res = min(*args)
#     print(max(*args))
#     return res
#
#
# return_min_show_max(1, 3, 5, 2, 3, 4)
# - створити функцію яка повертає найбільше число з ліста

# def max_in_list(numbers):
#     return max(numbers)
#
#
# some_list = [1, 2, 3, 4]
# max_in_list(some_list)
# - створити функцію яка повертає найменьше число з ліста

# def min_from_list(numbers):
#     return min(numbers)
#
#
# min_from_list([1, 2, 3, 4])
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def sum_of_list(numbers):
#     print(sum(numbers))
#     return sum(numbers)
#
#
# sum_of_list([1, 3, 4, 5, 5])
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def average(numbers):
#     print(sum(numbers) // len(numbers))
#     return sum(numbers) // len(numbers)
#
#
# average([1, 2, 3, 4, 5])

# ################################################################################################
# 1)Дан list:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

nums = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def min_num():
    arr = nums.copy()
    print(min(arr))


def duble():
    arr = nums.copy()
    print(list(set(arr)))


def to_x():
    arr = nums.copy()
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(arr)])


def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


# square(4)


def multiply():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            # print(' ' if res//10 else '  ', end='')
            # print(res, end='')
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1


def menu():
    while True:
        print('1) знайти мін число')
        print('2) видалити усі дублікати')
        print('3) замінити кожне 4-те значення на "x"')
        print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
        print('5) вывести табличку множення за допомогою цикла while')
        print('6) exit')

        ch = input('make a choice: ')
        if ch == '1':
            min_num()
        elif ch == '2':
            duble()
        elif ch == '3':
            to_x()
        elif ch == '4':
            square(5)
        elif ch =='5':
            multiply()
        elif ch == '6':
            break



menu()



