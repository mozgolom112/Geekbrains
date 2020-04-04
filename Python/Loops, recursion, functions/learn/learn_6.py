def to_binary(num : int) -> str:
    s = ''
    if num < 0:
        return 0
    while num != 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s

# print(to_binary(256))

while True:
    n = int(input('Введите целое число: '))
    if n != 0:
        print(to_binary(n))
    else:
        break