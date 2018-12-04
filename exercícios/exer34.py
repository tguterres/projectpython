#Exercíocio 34
slry = int(input('Salário: '))
if slry >= 1250:
    print('O seu salário com aumento é R${:.2f}.'.format((slry*1.1)))
else:
    print('O seu salário com aumento é R${:.2f}.'.format((slry*1.15)))
