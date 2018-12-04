#Exercício 33
n1 = int(input('número: '))
n2 = int(input('número: '))
n3 = int(input('número: '))
#verificando o menor
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor número é {}.'.format(menor))
#verificando o maior
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior número é {}.'.format(maior))
