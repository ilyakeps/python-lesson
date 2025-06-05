A = int(input("Введите целое число А: "))
B = int(input("Введите целое число B: "))
C = A if A % 2 == 0 else A + 1

vivod = range(C, B + 1, 2)

print(*vivod)