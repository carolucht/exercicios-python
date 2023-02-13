import math
cateto1 = int(input('Qual a medida do cateto 1? '))
cateto2 = int(input('Qual a medida do cateto 2? '))
a = (cateto1**2 + cateto2**2)
b = math.sqrt(a)
print(f'A hipotenusa é igual a {b}')