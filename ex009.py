#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#Primeira versão
numeroIn = int(input('Insira um número inteiro: '))
print('{} x 1 ='.format(numeroIn), numeroIn * 1)
print('{} x 2 ='.format(numeroIn), numeroIn * 2)
print('{} x 3 ='.format(numeroIn), numeroIn * 3)
print('{} x 4 ='.format(numeroIn), numeroIn * 4)
print('{} x 5 ='.format(numeroIn), numeroIn * 5)
print('{} x 6 ='.format(numeroIn), numeroIn * 6)
print('{} x 7 ='.format(numeroIn), numeroIn * 7)
print('{} x 8 ='.format(numeroIn), numeroIn * 8)
print('{} x 9 ='.format(numeroIn), numeroIn * 9)
print('{} x 10 ='.format(numeroIn), numeroIn * 10)

#Segunda versão
numeroIn = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(numeroIn, 1, numeroIn*1))
print('{} x {:2} = {}'.format(numeroIn, 2, numeroIn*2))
print('{} x {:2} = {}'.format(numeroIn, 3, numeroIn*3))
print('{} x {:2} = {}'.format(numeroIn, 4, numeroIn*4))
print('{} x {:2} = {}'.format(numeroIn, 5, numeroIn*5))
print('{} x {:2} = {}'.format(numeroIn, 6, numeroIn*6))
print('{} x {:2} = {}'.format(numeroIn, 7, numeroIn*7))
print('{} x {:2} = {}'.format(numeroIn, 8, numeroIn*8))
print('{} x {:2} = {}'.format(numeroIn, 9, numeroIn*9))
print('{} x {} = {}'.format(numeroIn, 10, numeroIn*10))
print('-' * 12)