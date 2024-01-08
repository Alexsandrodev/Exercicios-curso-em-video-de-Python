from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "pessoas.txt"

if not arq_existe(arq):
    criar_arquivo(arq)

while True:
    sleep(.5)
    resposta = menu([f'Ver Pessoas Cadastradas', 'Cadrastrar Nova Pessoas', 'Sair do Programa'])


    if resposta == 1:
        ler_arquivo(arq)
    
    elif resposta == 2:
        cabecalho('Novo Cadrastro')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')

        cadrastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('\33[31mSaindo do Sistema... Volte sempre!!\33[m')       
        sleep(.5)
        break

    else:
        print('\33[31mError, por favor digite uma opção valida!!\33[m')
        sleep(1)