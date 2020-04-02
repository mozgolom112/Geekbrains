numbers = []
numbers.append(int(input("Ввод a: ")))
numbers.append(int(input("Ввод b: ")))
numbers.append(int(input("Ввод c: ")))

max = numbers[0]

for num in numbers[1:]:
    if max < num:
        max = num
print(f'Максимум: {max}')