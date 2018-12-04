# Exercício ano bissexto
ano = int(input('ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('O ano não é Bissexto')
