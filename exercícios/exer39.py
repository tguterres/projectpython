# Vai pro quartel!
birth = int(input('Qual o ano do seu nascimento: '))

if birth > 2000:
    print('Você ainda não precisa se alistar.')
elif birth == 2000:
    print('Você precisa se alistar neste ano.')
elif birth < 2000:
    print('O seu alistamento já passou.')
    