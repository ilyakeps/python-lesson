# clients = int(input("Сколько клиентов?"))
# beers = int(input("Сколько у тебя пива на продажу?"))
# count = 0
#
# while clients > 0 and beers >= 0:
#     prodano_beers = int(input("Сколько пива хочет купить клиент?"))
#     clients -= 1
#     if beers >= prodano_beers:
#         beers -= prodano_beers
#     print(f"Осталось пива {beers}")
#     if beers <= 0:
#         print(f"Пиво закончилось")


number = int(input("Ведите число:" ))
count = 0

for n in range(number):
    whole_number = int(input("Введите целое число: "))
    if whole_number == 0:
        count += 1

print(f"Количество нулей: {count}")


