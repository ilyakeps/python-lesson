word = input("Введите слово из маленьких латинских букв: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
cons_count = 0
vowel_count = 0
vowel_stats = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_stats[letter] += 1
    else:
        cons_count += 1

print(f"Согласных букв: {cons_count}")
print(f"Гласных букв: {vowel_count}")

# Выводим статистику по каждой гласной
for vowel in sorted(vowel_stats):
    count = vowel_stats[vowel]
    print(f"{vowel}: {count if count > 0 else False}")