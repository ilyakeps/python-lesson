chislo = int(input())
a = "отрицательное четное число"
b = "отрицательное нечетное число"
c = "нулевое число"
d = "положительное четное число"
e = "положительное нечетное число"

if (chislo == 0):
    print({c})
elif (chislo <0) and (chislo % 2 == 0):
    print({a})
elif (chislo < 0) and (chislo % 2 == 1):
    print({b})
elif (chislo > 0) and (chislo % 2 == 0):
    print({d})
elif (chislo > 0) and (chislo % 2 == 1):
    print({e})