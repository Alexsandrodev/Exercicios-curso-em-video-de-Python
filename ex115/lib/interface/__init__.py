from lib.dados import *

def linhas(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linhas())
    print(txt.center(42))
    print(linhas())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    
    print(linhas())
    
    opc = leiaint('Sua opção: ')
    return opc
    