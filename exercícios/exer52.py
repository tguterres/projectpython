#Primos
import colorama
n = int(input('Número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\33[31m', end='')
        tot = tot+1
    else:
        print('\33[30m', end='')
    print('{}'.format(c), end='')
if tot == 2:
    print('\n\33[30mO número é primo.')
else:
    print('\n\33[30mO número NÃO é primo.')