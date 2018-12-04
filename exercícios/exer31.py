#exercício 31
km = int(input('Quantos km você quer viajar? '))

if km <= 200:
    print('Sua viagem custará R${:.2f}.'.format(km*0.5))
else:
    print('Sua viagem custará R${:.2f}.'.format(km*0.45))
print('Deseja comprar um bilhete?')
