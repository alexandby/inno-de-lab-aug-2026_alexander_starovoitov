# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

#1
new_string = raw_user_record.split(sep=';')

#2
for i in range(len(new_string)):
    new_string[i] = new_string[i].strip()

#3
new_string[0] = f'UID-{ new_string[0] }'

#4
new_string[1] = new_string[1].replace('_', ' ').title()

#5
new_string[2] = new_string[2].upper()

#6
new_string[3] = new_string[3].lower()

#7
print(f'Нормализованная запись: { ' | '.join(new_string) }')