num =int(input('Введите число: '))
to_trans = str(input('Введите тип, в который нужно перевести \nb - байты \nk-килобайты\n:')).lower()
if (to_trans == 'b'):
    print(f'{num} Кб = {num * 1024} байт')
elif (to_trans == 'k'):
    print(f'{num} байт = {num / 1024} Кб')
else:
    print('Ошибка ввода')