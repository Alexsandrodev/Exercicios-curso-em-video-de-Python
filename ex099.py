# importações
from time import sleep
# Funções
def maior(*num):
    maior = 0
    cont = 1

    print('-=-' * 30)
    print('Analisando os valores passados... ', flush=True)
    sleep(1)
    for v in num:
        sleep(.2)
        print(v, end=' ', flush=True)
        
        if cont == 1:
            maior = v
        else:
            if maior < v:
                maior = v   

        cont += 1 
    
    print(f'Foram informados {len(num)} valores ao todo.')

    print(f'O maior valor informa do foi {maior}')

# Entradada de dados

maior(2, 9, 4, 5, 7, 1)
sleep(.2)
maior(4, 7, 0)
sleep(.2)
maior(1, 2)
sleep(.2)
maior(6)
sleep(.2)
maior()