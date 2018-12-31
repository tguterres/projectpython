#Palíndromo

k = str(input('Digite um frase: ')).strip().lower()
words = k.split()
join = ''.join(words)
rev = join[::-1]
if rev == join:
    print('Palíndromo')
else:
    print('Não é palídromo')