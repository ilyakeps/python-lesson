# def chet(a):
#     if a % 2 == 0:
#         return True
#     return False
#
# print(chet(5))
# print(chet(4))

# def tmp(name):
#     print(f'Привет {name}')
#
# tmp('MARK')

# def vis(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     return False
#
# y = int(input("Введите год: "))
# print(vis(y))

# def nechet(n):
#     return(n % 2 !=0)
#
# def res(l):
#     for i in l:
#         if nechet(i):
#             print(i)
#
# tmp = [1,2,3,4,5,6,78,9,]
# res(tmp)

# def new_year():
#     print('С новым годом!!!')
#
# def birthday():
#     name = input("Укажите имя имениника: ")
#     print(f'С днем рождения {name}!!!')
#
# def mart8():
#     print('Поздравляю с 8 мартом!!!')
#
# n = int(input("Укажите кол-во команд которые будут выполнены: "))
# for i in range(n):
#     cmname = input('Введите значение "новый год", "день рожденье" или "8 марта": ')
#     if cmname == 'новый год':
#         new_year()
#     elif cmname == 'день рожденье':
#         birthday()
#     elif cmname == '8 марта':
#         mart8()
#     else:
#         print('Неправильная команда')

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial2(start_num):
    first_fact = factorial(start_num)
    numbers = range(first_fact, 0, -1)
    result = [factorial(num) for num in numbers]
    return result


input_num = int(input("Введите число: "))
result_list = factorial2(input_num)
print(f"Факториал числа {input_num}: {factorial(input_num)}")
print(f"Результирующий список: {result_list}")