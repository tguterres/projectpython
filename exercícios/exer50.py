# 6 números inteiros
s = 0
for c in range(0,6):
   n = int(input('Digite um número inteiro: '))
   if n % 2 == 0 and n != 0:
       s += n
print(s)

