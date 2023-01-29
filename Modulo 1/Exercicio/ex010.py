reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = reais / 3.27
print('com R${:.2f} você pode comprar US${:.2f}'.format(reais, dolar))