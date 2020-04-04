num = int(input('Введите число: '))
while num > 0:
    print(f'{num%10}')
    num = num //10

while True:
    num = float(input('Input number: '))
    if (num > 0 and num < 100):
        break

for i in range(11):
    print(i)

