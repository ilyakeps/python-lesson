n = list(map(int, input("Введите число: ").split()))
s1 = set()
for i in n:
    if i in s1:
        print("NO")
    else:
        print("YES")
        s1.add(i)