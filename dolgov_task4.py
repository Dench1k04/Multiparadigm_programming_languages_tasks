# Multiparadigm programming languages, Lab № 4
# Dolgov Denis IKM-221a

print('Multiparadigm programming languages, Lab № 4')
print(' Dolgov Denis IKM-221a')

# We ask the user to enter the number N
n = int(input('Enter your N: '))

# We check each number from 2 to N for simplicity
for num in range(2, n):
    # We check whether the number is prime
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # If the number is simple, display it on the screen
    if is_prime:
        print(num)
