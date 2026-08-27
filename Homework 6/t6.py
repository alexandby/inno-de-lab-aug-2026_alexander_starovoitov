while True:
    try:
        # 1. Ввод чисел с защитой от ввода букв
        first_number = float(input('Введите первое число (или "выход"): '))
        second_number = float(input('Введите второе число: '))
    except ValueError:
        # Проверка на выход из программы
        print('Программа завершена.')
        break

    # 2. Ввод и валидация оператора
    calc_operator = input('Выберите оператор (+, -, *, /): ').strip()
    if calc_operator not in ['+', '-', '*', '/']:
        print('Неверный оператор! Попробуйте заново.\n')
        continue

    # 3. Выполнение вычислений
    if calc_operator == '+':
        result = first_number + second_number
    elif calc_operator == '-':
        result = first_number - second_number
    elif calc_operator == '*':
        result = first_number * second_number
    elif calc_operator == '/':
        # Защита от деления на ноль
        if second_number == 0:
            print('Ошибка: Деление на ноль невозможно!\n')
            continue
        result = first_number / second_number

    # 4. Вывод красивого результата (убираем лишние нули у целых чисел)
    if result.is_integer():
        result = int(result)

    print(f'Результат операции: {first_number} {calc_operator} {second_number} = {result}\n')