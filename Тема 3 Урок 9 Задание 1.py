# tmp = {2,3,3,4}
# tmp.add(7)
# tmp.discard(3)
# print(tmp)


# n = int(input())
# used = set()
# for i in range(n):
#     promo = input()
#     if promo in used:
#         print("Невариант")
#     else:
#         used.add(promo)
# print(len(used))


# kolvo = int(input("Введите кол-во сотрудников в первой компании: "))
# imena1 = []
# for i in range(kolvo):
#     name = input("Введите имя: ")
#     imena1.append(name)
#
# uc = set(imena1)
#
# kolvo2 = int(input("Введите кол-во сотрудников во второй компании: "))
# imena2 = []
# for i in range(kolvo2):
#     name = input("Введите имя: ")
#     imena2.append(name)
#
# uc1 = set(imena2)
#
# print(uc.union(uc1))

n = int(input("Введите число: "))
promo = list(map(int, input("Введите другое число: ").split()))
s1 = set(promo)
print(len(s1))
