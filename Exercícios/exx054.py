"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 

No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,5):
    nasc = int(input('Digite o ano de nascimento da primeira pessoa: '))
    resultado = atual - nasc
    if resultado >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} maiores de idade'.format(totmaior))
print('Temos {} menores de idade'.format(totmenor))
