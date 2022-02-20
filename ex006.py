#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Primeira opção
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O número que você escolheu foi {}.\nO seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}.'.format(numero, dobro, triplo, raiz))

#Segunda opção
numero = int(input('Digite um número: '))
print('O número que você escolheu foi {}.\nO seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}.'.format(numero, (numero*2), (numero*3), (numero*(1/2))))