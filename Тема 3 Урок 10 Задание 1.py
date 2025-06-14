pets = {}

name = input("Введите имя питомца: ")
vid = input("Введите вид питомца: ")
vozrast = int(input("Введите возраст питомца: "))
nameVladelca = input("Введите имя владельца: ")

pets[name] = {
    1: vid,
    2: vozrast,
    3: nameVladelca,
}

if 11 <= vozrast % 100 <= 14:
    vozrast_str = f"{vozrast} лет"
elif vozrast % 10 == 1:
    vozrast_str = f"{vozrast} год"
elif 2 <= vozrast % 10 <= 4:
    vozrast_str = f"{vozrast} года"
else:
    vozrast_str = f"{vozrast} лет"

pet_info = pets[name]
print(f'Это {pet_info[1]} по кличке "{name}". Возраст питомца: {vozrast_str}. Имя владельца: {pet_info[3]}')