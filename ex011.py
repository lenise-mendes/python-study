#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2m²

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
litros = int(largura * altura) // 2
print('Para pintar a sua parede, você precisará de {} litros de tinta.'.format(litros))
