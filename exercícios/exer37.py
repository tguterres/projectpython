# Bases de Conversão

n = int(input('Informe a base para conversão\n'
        '1 para binário\n'
        '2 para octal\n'
        '3 para hexadecimal\n'))
n1 = int(input('Digite um número para conversão: '))
if n == 1:
        print(bin(n1))
elif n == 2:
        print(oct(n1))
elif n == 3:
        print(hex(n1))

