minSumm = int(input())
Mike = int(input())
Ivan = int(input())

if Mike >= minSumm and Ivan >= minSumm:
    print(2)
elif Mike >= minSumm:
    print("Mike")
elif Ivan >= minSumm:
    print("Ivan")
elif Mike + Ivan >= minSumm:
    print(1)
elif Mike + Ivan < minSumm:
    print(0)