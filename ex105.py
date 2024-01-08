# Funções
def notas(*valores, sit=False):
    """
    -> Cria um dicionario com as notas recebidas pelo usuário
    :Para valores: As notas recebidas
    :Para sit: (Valor opcional) Se deseja ou não saber a situação do aluno
    :Return: Dicionario com, total de notas, maior nota, menor nota, media e situação (opcional)
    """
    dicionario = {}
    maior = menor = 0
    cont = 1
    soma = 0
    media = 0
    
    for valor in valores:
        if cont == 1:
            maior = valor
            menor = valor

        else:
            if maior < valor:
                maior = valor

            if menor > valor:
                menor = valor    

        soma += valor
        cont +=1

    media = soma / len(valores)
    
    dicionario['total'] = len(valores)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit == True:
        if media >= 7:
            dicionario['situação'] = 'Boa'
        elif media > 4:
            dicionario['situação'] = 'Razoavel'
        else:
            dicionario['situação'] = 'Ruim'            
    
    return dicionario

# Programa principal
resp = notas(2, 5, 6, 1, sit=True)
print(resp)