#PA

n = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
dec = n+(10-1) * rz
for c in range(n, dec+rz, rz):
    print(c, end=' ')
print('Fim.')
