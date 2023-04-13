# Introduction to programming, Lab № 4
# Dolgov Denis IKM-221a

print('Introduction to programming, Lab № 4')
print(' Dolgov Denis IKM-221a')


# Запитуємо користувача ввести число N
n = int(input('Enter your N: '))

# Перевіряємо кожне число від 2 до N на простоту
for num in range(2, n):
    # Перевіряємо, чи є число простим
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # Якщо число просте, виводимо його на екран
    if is_prime:
        print(num)
