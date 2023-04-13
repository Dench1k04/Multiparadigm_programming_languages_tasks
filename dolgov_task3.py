# Introduction to programming, Lab № 3
# Dolgov Denis IKM-221a

import math as m

print('Introduction to programming, Lab № 3')
print('Dolgov Denis IKM-221a')

a = int(input('Введіть значення a: '))
b = int(input('Введіть значення b: '))

if (2 * a) + b == 0 or b == 0:
    raise Exception("Ділення на 0 неможливе. Значення b має бути відмінним від 0, або значення (2 * a) + b"
          " має бути відмінним від 0.")
else:
    result = ((a - 2) / ((2 * a) + b)) + (m.sin(3 * a) / m.cos(b))
    print(f"Результат: {result}")
