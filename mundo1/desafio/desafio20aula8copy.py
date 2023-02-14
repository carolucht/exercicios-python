""" 
import random
name = ('Escreva um nome: ')
name = ('Escreva um nome: ')
name = ('Escreva um nome: ')
name = ('Escreva um nome: ')


print(num1 + random.sample(name))
print(num2 + random.sample(name))
print(num3 + random.sample(name))
print(num4) + (random.sample(name))
 
-------------------------------------
import random
name = ('Matheus','Caio','Vinicius','Fernando')
num = ('1','2','3','4')
print(random.choice(num)+ random.choice(name))
print(random.choice(num)+ random.choice(name))
print(random.choice(num)+ random.choice(name))
print(random.choice(num)+ random.choice(name))

-------------------------------------


import random

name = ['Matheus','Caio','Vinicius','Fernando']

num1 = ('1')
num2 = ('2')
num3 = ('3')
num4 = ('4')

r1 = random.choice(name)
name.remove(r1)
print(f'{r1} ({num1})')
r2 = random.choice(name)
name.remove(r2)
print(f'{r2} ({num2})')
r3 = random.choice(name)
name.remove(r3)
print(f'{r3} ({num3})')
r4 = random.choice(name)
name.remove(r4)
print(f'{r4} ({num4})')

-------------------------------------

 """

from random import shuffle
nome1 = input('Qual o primeiro nome? ')
nome2 = input('Qual o segundo nome? ')
nome3 = input('Qual o terceiro nome? ')
nome4 = input('Qual o quarto nome? ')

mylist = []
mylist.append(nome1)
mylist.append(nome2)
mylist.append(nome3)
mylist.append(nome4)



shuffle(mylist)


print(mylist)



