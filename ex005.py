#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#Primeira opção
nInteiro = int(input('Digite um número inteiro: '))
nAntecessor = nInteiro - 1
nSucessor = nInteiro + 1
print('O número que você escolheu foi {}. O seu antecessor é {} e o seu sucessor é {}.'.format(nInteiro, nAntecessor, nSucessor))

#Segunda opção
nInteiro = int(input('Digite um número inteiro: '))
print('O número que você escolheu foi {}. O seu antecessor é {} e o seu sucessor é {}'.format(nInteiro, (nInteiro-1), (nInteiro+1)))
