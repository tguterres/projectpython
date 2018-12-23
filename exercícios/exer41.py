from datetime import date
atual = date.today().year
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print('MIRIM')
elif 9 > idade < 15:
    print('INFANTIL')
elif 9 < idade < 21:
    print('JUNIOR')
elif idade >= 20:
    print('MASTER')
