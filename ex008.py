#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Primeira versão
valorM = float(input('Insira o valor em metros: '))
valorCm = valorM * 100
valorMm = valorM * 1000
print('O valor em metros é {}, em centímetros é {:.0f} e em milímetros é {:.0f}'.format(valorM, valorCm, valorMm))

#Segunda versão
valorM = float(input('Insira o valor em metros: '))
valorDm = valorM * 10
valorCm = valorM * 100
valorMm = valorM * 1000
valorDam = valorM / 10
valorHm = valorM / 100
valorKm = valorM / 1000
print('O valor em metros é {}.'.format(valorM))
print('Em decímetros é {:.0f}.'.format(valorDm))
print('Em centímetros é {:.0f}.'.format(valorCm))
print('Em milímetros é {:.0f}.'.format(valorMm))
print('Em decâmetros é {}.'.format(valorDam))
print('Em hectômetros é {}.'.format(valorHm))
print('Em kilômetros é {}.'.format(valorKm))
