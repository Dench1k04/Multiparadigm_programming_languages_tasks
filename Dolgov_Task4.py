# Introduction to programming, Lab № 4
# Dolgov Denis IKM-221a

print("Introduction to programming, Lab № 4")
print("Dolgov Denis IKM-221a")

# Определение функции для решета Эратосфена
def eratosthenes(n):
    # Создание списка-решета
    sieve = [True] * (n+1)
    # Установка значений 0 и 1 в список-решето в False
    sieve[0] = sieve[1] = False
    # Итерация по числам от 2 до sqrt(n) включительно
    for i in range(2, int(n**0.5)+1):
        # Если текущее число является простым,
        # то помечаем все кратные ему числа как составные
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(sieve[i*i:n+1:i])
    # Возврат списка простых чисел, которые соответствуют индексам списка-решета, равным True
    return [i for i in range(2, n+1) if sieve[i]]

# Получение числа N от пользователя
n = int(input("Введите число N: "))
# Вызов функции для решета Эратосфена
primes = eratosthenes(n)
# Вывод простых чисел, меньших N, на экран
print("Простые числа, меньшие", n, ":")
print(primes)
