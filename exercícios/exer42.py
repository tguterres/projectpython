#triangulos
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1< r2+r3 and r2 < r1+r3 and r3< r1+r2:
    print('As retas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 != r2 != r3 != r1:
        print('escaleno.')
    else:
        print('isósceles.')
else:  
    print('As retas NÃO formam um triângulo.')
    