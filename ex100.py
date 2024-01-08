# importações
from random import randint
from time import sleep
# Variaveis
valores = []
# Funções
def sorteia():
    print('Sortenado 5 valores para a lista: ', end='')
    for v in range(0, 5):
        valores.append(randint(1, 10))


    for v in valores:
        print(v, end=' ', flush=True)
        sleep(.5)
    print('Valores sorteados.')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v

    print(f'Somando os valores pares de {lista}, temos {soma}')

# Tratamento e saida de dados
sorteia()
somapar(valores)