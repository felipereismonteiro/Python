"""Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 

No final, mostre qual foi o maior e o menor peso lidos."""


#vc coloca o meior e menor a 0, se o peso for o primeiro vai ser ele agr se o peso foi maior vai passar a ser ele
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))