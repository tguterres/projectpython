# Preço e condição de pagamento
price = float(input('Qual o preço do produto em R$: '))
mtd_pgmt = int(input('Escolha o método de pagamento:\n'
            'Digite 1 para pagamento à vista\n'
            'Digite 2 para pagamento à vista no cartão\n'
            'Digite 3 para pagamento em 2x no cartão\n'
            'Digite 4 para pagamento no cartão em 3x ou mais.'
            'Digite sua forma de pagamento: '))

if mtd_pgmt == 1: 
    print('O produto vai custar R${}.'.format(price * 0.9))
elif mtd_pgmt == 2:
    print('O produto vai custar R${}.'.format(price * 0.95))
elif mtd_pgmt == 3:
    print('O produto vai custar duas parcelas de R${}.'.format(price / 2))
elif mtd_pgmt == 4:
    print('O produto vai ser pago parcelado no valor de R${}.'.format(price*1.3))

#teste