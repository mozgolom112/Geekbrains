#Алгоритм Евклида Нахождение нод

#var 1 
#слишком долго
#циклический алгоритм, основанный на вычитании
def gcd_1(m, n):
    while (m != n): #базовый случай - случай при котором заканчивается цикл
        if (m > n):
            m -= n
        else:
            n -= m
    return m

#var 2
#быстро но может быть переполнение из-за рекурсии
#рекурсивный алгоритм, основанный на нахождении остатка от деления
def gcd_2(m, n):
    if (n == 0):
        return m
    return gcd_2(n, m % n)

#var 3
#оптимальный
#циклический алгоритм, основанный на нахождении осттка от деления
def gcd_3(m, n):
    while (n != 0):
        m, n = n, m % n
    return m

#print(gcd_1(540, 5636663464))
#print(gcd_2(540, 5636663464))
print(gcd_3(5443560, 5636663464665564))
