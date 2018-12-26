#Jokenpô
import random
papel = str('Papel').strip().lower()
tesoura = str('Tesoura').strip().lower()
pedra = str('Pedra').strip().lower()
sorteio = [papel, tesoura, pedra]
jokenpo = random.choice(sorteio)

jkp = str(input('Escolha:\n'
    '1 para papel\n'
    '2 para tesoura\n'
    '3 para pedra\n'
    ''))

if jkp == 1:
    if jokenpo == papel == jkp:
        print('Empate.')
    elif jokenpo == tesoura:
        print('Você ganhou!')
    elif jokenpo == pedra:
        print('Você perdeu!')
elif jkp == 2:
    if jokenpo == tesoura == jkp:
        print('Empate.')
    elif jokenpo == papel:
        print('Você ganhou!')
    elif jokenpo == pedra:
        print('Você perdeu!')


