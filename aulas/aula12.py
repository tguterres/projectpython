#Condições Aninhadas
name = str(input('Seu nome:'))

if name == 'Tiago':
    print('Que nome lindo!') 
elif name == 'Nick' or name == 'James':
    print('Seu nome é comum.') 
elif name in 'Ana Julia Maria':
    print('Nome feminino.')
else:
    print('Bom dia, {}.'.format(name))