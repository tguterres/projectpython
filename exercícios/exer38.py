# Qual o valor maior?
n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))

if n1 > n2:
    print('{} é maior que {}.'.format((n1),(n2)))
elif n2 > n1:
    print('{} é maior que {}.'.format((n2),(n1)))
elif n1 == n2:
    print('Os números são iguais.')
 