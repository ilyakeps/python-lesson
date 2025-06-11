s1 = int(input("Введите кол-во в первом списоке: "))
sl1 = []
for i in range(s1):
    cifra = input("Введите число в первом списке: ")
    sl1.append(cifra)

uc = set(sl1)

s2 = int(input("Введите кол-во во втором списоке: "))
sl2 = []
for i in range(s2):
    cifra2 = input("Введите число во втором списке: ")
    sl2.append(cifra2)

uc2 = set(sl2)

print(len(uc.intersection(uc2)))
