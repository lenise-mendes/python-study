#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoOriginal = float(input('Preço: '))
precoDesconto = precoOriginal * 0.95
print('Seu produto com 5% de desconto fica R${}.'.format(precoDesconto))
