#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

info = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(info)))
print('Só tem espaços? {}'.format(info.isspace()))
print('É um número? {}'.format(info.isnumeric()))
print('É alfabético? {}'.format(info.isalpha()))
print('É alfanumérico? {}'.format(info.isalnum()))
print('Está em maiúsculas? {}'.format(info.isupper()))
print('Está em minúsculas? {}'.format(info.islower()))
print('Está capitalizada? {}'.format(info.istitle()))
