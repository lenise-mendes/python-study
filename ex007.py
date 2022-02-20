#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
s = (n1 + n2) / 2
print('A sua primeira nota foi {:.1f} e a sua segunda nota foi {:.1f}. Portanto, a sua média é: {:.1f}.'.format(n1, n2, s))
