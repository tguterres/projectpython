#Jokenpô
from random import randint
from time import sleep
jokenpo = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0 , 2)
print('''Escolha entre:
[0] Pedra
[1] Papel
[2] Tesoura''')
player = int(input('Qual é a sua jogada? '))
print('--' * 10)
print('O computador escolheu {}.'.format(jokenpo[pc]))
print('Você escolheu {}.'.format(jokenpo[player]))
print('--' * 10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
if pc == 0:
    if player == 0:
        print('Empate.')
    elif player == 1:
        print('Você ganhou!')
    elif player == 2:
        print('Você perdeu!')
    else:
        print('Jogada inválida.')
elif pc == 1:
    if player == 1:
        print('Empate.')
    elif player == 0:
        print('Você perdeu!')
    elif player == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida.')
elif pc == 2:
    if player == 2:
        print('Empate.')
    elif player == 0:
        print('Você ganhou!')
    elif player == 1:
        print('Você perdeu!')
    else:
        print('Jogada inválida.')


