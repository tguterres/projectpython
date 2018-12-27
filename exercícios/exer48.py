# Soma ímpares de 1-500
s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        s = s + i
print('A soma de todos os {} valores solicitados é {}.'.format(cont, s))
