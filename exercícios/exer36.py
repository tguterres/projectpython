#Empréstimo Bancário
house = float(input('Qual o valor da casa? '))
slry = float(input('Qual o seu salário atual? '))
time = int(input('Em quantos anos você quer pagar? '))
prest = (house / (time*12))

if prest<=(slry*30 /100):
    print('Sua prestação será de R$ {:.2f}.'.format(prest))
else:
    print('Empréstimo negado.')

print ('A prestação é de R${:.2f}'.format(prest))
