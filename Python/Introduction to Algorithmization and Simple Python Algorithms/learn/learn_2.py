try:
    num = int(input('Введите трехзначное число: '))
except:
    pass
a = num //100
b = num % 100 // 10
c = num % 10

sum = a + b + c
mult = a * b * c

print('Sum: {}'.format(sum))
print(f'Mult: {mult}')
    