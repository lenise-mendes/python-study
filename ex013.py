#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioAntigo = float(input('Preencha o seu salário atual: '))
salarioNovo = salarioAntigo * 1.15
print('Parabéns! Você recebeu um aumento de 15% e o seu novo salário é R${}.'.format(salarioNovo))
