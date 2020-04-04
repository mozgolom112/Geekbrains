#Решето Эратосфена
#нахождение простых числе до n

def eratos(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2,n):
        if sieve[i] != 0:
            j = i * 2
            
            while (j < n):
                sieve[j] = 0
                j += i
    
    result = [i for i in sieve if i != 0] 
    #генератор списка https://younglinux.info/python/feature/generators

    return result

#list_1 = [i for i in range(100) if i > 50]
#print(list_1)


print(f'{eratos(40)}')