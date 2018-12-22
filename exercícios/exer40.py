# Aprovado ou reprovado
nota1 = float(input('Nota primeiro semestre: '))
nota2 = float(input('Nota segundo semestre: '))
media = ((nota1+nota2)/2)
if media < 5.0:
    print('Reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação.')
elif media >= 7.0:
    print('Aprovado.') 