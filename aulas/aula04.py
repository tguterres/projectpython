#Exercício Aluguel de Carros
d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kilometros foram rodados? '))
v = (d*60) + (km * 0.15)
print('O valor do aluguel é: R${:.2f}'.format(v))
