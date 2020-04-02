# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first_letter = str(input('Первая буква: ')).lower().replace(' ','')
second_letter = str(input('Вторая буква: ')).lower().replace(' ','')

first_letter = ord(first_letter)
second_letter = ord(second_letter)

position_a = ord('a')
position_z = ord('z')
if (first_letter < position_a or first_letter > position_z or second_letter < position_a or second_letter > position_z):
   print('Введите буквы латинского алфавита')
else:
    print(f'Буква {chr(first_letter)} стоит на {first_letter - position_a + 1} месте\n' 
         +f'Буква {chr(second_letter)} стоит на {second_letter - position_a + 1} месте\n') 
    if (first_letter < second_letter):
        print(f'Между ними находится: {second_letter - first_letter - 1}')
    else:
        print(f'Между ними находится: {first_letter - second_letter - 1}')


       
