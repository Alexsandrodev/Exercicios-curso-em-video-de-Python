# Importações
from datetime import date

# Funções 
def voto(nascimento):
    global idade
    # Calcula a idade
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    # Retorna valor
    if idade >= 18:
        return 'VOTO OBRIGATORIO' 
    
    elif idade >= 16:
        return 'VOTO OPCIONAL'
    
    else:
        return 'NÃO VOTA'

# programa principal
    # variaveis 
idade = 0

    # Entradad de dados
ano_nascimento = int(input('Data de nascimento: '))

    # Saida de dados
tipo_voto = voto(ano_nascimento)
print(f'Com {idade} anos: {tipo_voto}')