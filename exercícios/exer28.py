#exercício 28
import random
lista = [1,2,3,4,5]
sorteio = random.choice(lista)
adv = int(input('Escolha um número de 1 a 5: '))
if adv == sorteio:
    print('Você acertou!')
else:
    print('Errou. Tente outra vez.')
    




