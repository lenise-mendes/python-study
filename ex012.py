#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Primeira versão
precoOriginal = float(input('Preço: R$'))
precoDesconto = precoOriginal * 0.95
print('Seu produto com 5% de desconto fica R${:.2f}.'.format(precoDesconto))

#Segunda versão
precoOriginal = float(input('Preço: R$'))
precoDesconto = precoOriginal - (precoOriginal * 5 / 100)
print('Seu produto com 5% de desconto fica R${:.2f}.'.format(precoDesconto))
