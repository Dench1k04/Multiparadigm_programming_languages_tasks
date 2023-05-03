print('Multiparadigm programming languages, Lab № 2')
print('Dolgov Denis IKM-221a')

TEMPLATE = 'Enter {}'

x = int(input(TEMPLATE.format('x')))
y = int(input('Enter y'))
z = int(input('Enter z'))

a = x - (x + (y / z)) / (78 + y)

print('Result is: ', a)
