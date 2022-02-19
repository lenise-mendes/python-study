#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valorM = float(input('Insira o valor em metros: '))
valorCm = valorM * 100
valorMm = valorM * 1000
print('O valor em metros é {}, em centímetros é {} e em milímetros é {}'.format(valorM, valorCm, valorMm))
