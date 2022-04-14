"""Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

#no for vc volta da ultima letra usando -1

palavra = str(input('Digite sua frase: ')).upper().strip()
separar = palavra.split()
juntar = ''.join(separar)
inverso = ''
for c in range(len(juntar) -1, -1, -1):
    inverso += juntar[c]
print(juntar)
if inverso == juntar:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')