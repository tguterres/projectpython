# Pedra Papel Tesoura
import random
lis1 = ['pedra', 'papel', 'tesoura']
sort = random.choice(lis1)

n = str(input('Escolha entre Padre, Papel ou Tesoura:')).strip().lower()
if (n == sort):
    print('Empate.')

