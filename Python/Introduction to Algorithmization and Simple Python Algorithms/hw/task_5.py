#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
code_of_letter = int(input('Введите номер буквы латинского алфавита: '))
pos_a = ord('a')
if (code_of_letter < 1 or code_of_letter > 26):
    print('В латинском алфавите 26 букв')
else:
    print(f'{chr(pos_a + code_of_letter - 1)}')