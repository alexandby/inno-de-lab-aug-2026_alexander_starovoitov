import random

print('Я загадал число от 1 до 20. У тебя 5 попыток!')
guess_number = random.randint(1, 20)
attempts = 5
count = 0

while attempts > 0:
    count += 1
    your_number = int(input(f'Попытка { count } Введите число: '))
    if your_number == guess_number:
        print('Ты угадал! Отличная работа!')
        break
    elif your_number > guess_number:
        attempts -= 1
        print(f'Слишком много! Осталось попыток: { attempts }')
    elif your_number < guess_number:
        attempts -= 1
        print(f'Слишком мало! Осталось попыток: { attempts }')
    elif attempts == 0:
        print('Ты не угадал! Попыток не осталось!')
        break