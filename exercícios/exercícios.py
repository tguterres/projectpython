#exercícios aula 07
#desafio 5
n = int(input('Numero: '))
a = (n-1)
b = (n+1)
print('{}, {}'.format(a,b))

#desafio 6
n = int(input('Número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print("Dobro {}, Triplo {}, Raiz Quadrada {}".format(d,t,r))

#desafio 7
n1 = int(input('nota 1: '))
n2 = int(input('nota 2: '))
m = (n1+n2)/2
print('A média do aluno é: {}'.format(m))

#desafio 9 - tabuada
n=int(input('n: '))
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
print('A tabuado deste número é {},{},{},{},{},{},{},{},{}'.format(t1,t2,t3,t4,t5,t6,t7,t8,t9))

#desafio 11 - tinta necessária
lag = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lag*alt
li = area / 2
print('Você precisa de {} litros de tinta'.format(li))

# desafio 12 - desconto
n = float(input('Preço: '))
d = (n*115)/100
print('O seu valor com desconto é: {:.2f}'.format(d))

#desafio 13 -