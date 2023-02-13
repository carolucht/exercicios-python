import math
ang = float(input('Insira um ângulo qualquer: '))
x = math.radians(ang)
cos = math.cos(x)
seno = math.sin(x)
tang = math.tan(x)
print(f'O cosseno do ângulo {ang} é {cos:.3f}')
print(f'O seno do ângulo {ang} é {seno:.3f}')
print(f'A tangente do ângulo {ang} é {tang:.3f}')