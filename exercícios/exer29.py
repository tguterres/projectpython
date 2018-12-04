#exercício 29
velc = float(input('Velocidade: '))
if velc >=80:
    print('Você foi multado em R${}.'.format((velc-80)*7))
else:
    print('Você estava dentro do limite permitido.')