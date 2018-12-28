#Primos
import colorama
n = int(input('Número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\33[33m', end='')
        tot = tot+1
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end='')
if tot == 2:
    print('\nO número é primo.')
else:
    print('\nO número NÃO é primo.')