# sortear aluno
import random
a1 = str('tiago')
a2 = str('rafael')
a3 = str('gabriela')
a4 = str('felipe')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O escolhido é: {}'.format(escolhido))
