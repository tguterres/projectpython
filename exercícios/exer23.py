#exercicio 23 
nu = int(input('Digite um número de 1 a 9999: '))
n = str(nu)
print("Analisando o número {}".format(n))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))