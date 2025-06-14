import collections


#Словарь
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1

    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f'Добавлен новый питомец с ID {new_id}')

def read():
    pet_id = int(input("Введите ID питомца для поиска информации: "))
    pet_info = get_pet(pet_id)

    if not pet_info:
        print("Питомец с таким ID не найден")
        return

    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    age = pet_data['Возраст питомца']

    print(f'\nЭто {pet_data["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {age} {get_suffix(age)}. '
          f'Имя владельца: {pet_data["Имя владельца"]}')

def update():
    pet_id = int(input("Введите ID питомца для обновления информации: "))
    pet_info = get_pet(pet_id)

    if not pet_info:
        print("Питомец с таким ID не найден")
        return

    pet_name = list(pet_info.keys())[0]
    print("Текущая информация")
    print(f'1. Имя питомца {pet_name}')
    print(f'2. Вид питомца {pet_info[pet_name]["Вид питомца"]}')
    print(f'3. Возраст питомца {pet_info[pet_name]["Возраст питомца"]}')
    print(f'4. Имя владельца {pet_info[pet_name]["Имя владельца"]}')

    field = input("Введите номер поля для обновления(1-4): ")
    new_value = input("Введите новое значение: ")

    if field == "1":
        pets[pet_id][new_value] = pets[pet_id].pop(pet_name)
    elif field == "2":
        pet_info[pet_name]['Вид питомца'] = new_value
    elif field == "3":
        pet_info[pet_name]['Возраст питомца'] = int(new_value)
    elif field == "4":
        pet_info[pet_name]['Имя владельца'] = new_value
    else:
        print("Неверный номер поля")
        return
    print("Информация успешно обновлена! ")


def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    if pet_id in pets:
        yes = input("Вы уверены что надо удалить этого питомца? Восстановление данных будет невозможно. (Да/Нет): ")
        if yes.lower() == 'да':
            del pets[pet_id]
            print("Запись о питомце успешно удалена!")
        else:
            print("Вы отказались от удаления это питомца")
    else:
        print("Питомец с таким ID не найден")



def get_pet(ID):
  # функция, с помощью которой вы получите информацию о питомце в виде словаря
  # сделайте проверку, если питомца с таким ID нету в нашей "базе данных"
  # верните в этом случае False
  # а если питомец всё же есть в "базе данных" - верните информацию о нём
  # выглядеть это может примерно так:
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
  # функция, с помощью которой можно получить суффикс
  # 'год', 'года', 'лет'
  # реализацию этой функции вам предстоит придумать самостоятельно
  # функция будет возвращать соответствующую строку
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

def pets_list():
  # Эта функция будет создана для удобства отображения всего списка питомцев
  # Информацию по каждому питомцу можно вывести с помощью цикла for
    print("Список всех питомцев: ")
    for id, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        print(f'ID {id}, Имя {pet_name}')

def main():
    print("Добро пожаловать в базу данных наших питомцев!")
    print("Выберете одну из команд: create, read, update, delete, list, stop")

    while True:
        command = input("Введите команду: ").lower()
        if command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        elif command == "stop":
            print("Вы вышли из базы данных")
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()

