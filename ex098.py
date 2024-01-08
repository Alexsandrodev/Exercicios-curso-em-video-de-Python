# importações
from time import sleep

# Funções
def contador(inicio, fim, passo):
    print('-=-' * 30)
    print(f'Contagem de {inicio} até {fim} com o passo de {passo} em {passo}.', flush=True)
    sleep(1)

    # transforma negativo em positivo 
    if passo < 0:
        aux = passo
        passo = passo - passo - passo


    while inicio <= fim:
        if inicio != fim:
            print(inicio, end=', ', flush=True)
        else:
            print(inicio, flush=True)
        inicio += passo 

        sleep(0.5)
        if inicio == fim:
            break    


    while inicio >= fim:
        if inicio != fim:
            print(inicio, end=', ', flush=True)
        else:
            print(inicio, flush=True)

        sleep(0.5)
        inicio -= passo     


# entradada de dados

# Saida de dados
contador(1, 10, 1)
contador(10, 0, 2)


print('-=-' * 30)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if passo == 0:
    passo = 1

contador(inicio, fim, passo)