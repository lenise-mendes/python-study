#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (Considere US$1,00 = R$3,27)

dinheiro = float(input('Quantos reais você tem na sua carteira? R$'))
cambio = dinheiro / 3.27
print('Você tem R${:.2f} na sua carteira. Poderá comprar US${:.2f}.'.format(dinheiro, cambio))
