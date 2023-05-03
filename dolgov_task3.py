# Multiparadigm programming languages, Lab № 3
# Dolgov Denis IKM-221a

import math as m

print('Multiparadigm programming languages, Lab № 3')
print('Dolgov Denis IKM-221a')

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if (2 * a) + b == 0 or b == 0:
    raise Exception('Division by 0 is not possible. The value of b must be different from 0,'
                    ' or the value of (2 * a) + b must be different from 0.')
else:
    result = ((a - 2) / ((2 * a) + b)) + (m.sin(3 * a) / m.cos(b))

print(f"Result: {result}")
