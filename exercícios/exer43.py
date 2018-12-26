# Cálculo do IMC
peso = int(input('Digite seu peso em KG: '))
alt = float(input('Digite sua altura: '))
imc = (peso / (alt * alt))

#Status do indivíduo
if imc < 18.5:
    print('Abaixo do peso.')
elif  18.5 == imc < 25:
    print('Peso ideal.')
elif 25.1 < imc <=30:
    print('Sobrepeso.')
else:
    print('Obesidade mórbida.')
    
