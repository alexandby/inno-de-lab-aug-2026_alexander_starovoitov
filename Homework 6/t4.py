whole_number = input('Введите целое число: ')
if int(whole_number) % 2 == 0:
    print('Число ' + str(whole_number) + ' - чётное!')
else:
    print(f'Число { str(whole_number) } - нечётное!')