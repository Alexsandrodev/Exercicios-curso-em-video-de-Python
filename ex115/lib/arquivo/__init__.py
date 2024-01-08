from lib.interface import cabecalho

def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close

    except:
        print('Erro na criação de arquivo.')
    
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    
    except: 
        print('Erro ao ler o arquivo.')

    else:   
        cabecalho('Pessoas Cadratradas')
        
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<35}{dado[1]} anos')

    finally:
        a.close()

def cadrastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')

    except:
        print('Erro na abertura do arquivo.')

    else:
        try:    
            a.write(f'{nome};{idade}\n')

        except:
            print('Erro na inscrição de dados.')

        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()