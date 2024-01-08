def resumo(v, aument, redu):
    print('-' * 40)
    print(f'{"Resumo do Valor":^40}')
    print('-' * 40)

    print(f'{"Preço analisado:"} {moeda(v):>23}')
    print(f'{"Dobro do Preço:"} {dobro(v, True):>24}')
    print(f'{"Metade do Preço:"} {metade(v, True):>23}')
    print(f'{f"{aument:2}% de aumento:"} {aumentar(v, aument, True):>24}')
    print(f'{f"{redu:2}% de redução:"} {diminuir(v, redu, True):>24}')


def aumentar(n, porcent, form=False):
    """
    ->Aumenta o valor recebido pela porcentagem passada pelo úsuario.
    :para n: Valor recebido.
    :para porcent: Porcentagem do aumento.
    :Para form: Valor opcional caso o úsuario deseje formatar os valores enviados ou não. 
    :Return: Valor aumentado pela porcentagem passar no porcent, sendo formatada ou não
    """
    aumento = (n * porcent) / 100
    if form == False:
        return aumento + n
    
    else:
        return moeda(aumento + n)

    


def diminuir(n, porcent, form=False):
    """
    ->desconta o valor recebido pela porcentagem passada pelo úsuario.
    :para n: Valor recebido.
    :para porcent: Porcentagem do Desconto.
    :Para form: Valor opcional caso o úsuario deseje formatar os valores enviados ou não. 
    :Return: Valor Descontado pela porcentagem passar no porcent, sendo formatada ou não
    """
    desconto = (n * porcent) / 100
    if form == False:    
        return n - desconto 
    
    else:
        return moeda(n - desconto)        


def dobro(n, form=False):
    """
    ->Dobra o valor recebido pela porcentagem passada pelo úsuario.
    :para n: Valor recebido.
    :Para form: Valor opcional caso o úsuario deseje formatar os valores enviados ou não. 
    :Return: Valor dobrado, sendo formatada ou não
    """
    if form == False:    
        return n * 2
    
    else:
        return moeda(n * 2)


def metade(n, form=False):
    """
    ->Divide o valor recebido pela metade.
    :para n: Valor recebido.
    :Para form: Valor opcional caso o úsuario deseje formatar os valores enviados ou não. 
    :Return: Valor dividido pela metade, sendo formatada ou não
    """
    if form == False:
        return n / 2
    
    else:
        return moeda(n / 2)


def moeda(v):
    """
    ->Formata o valor recebido para Real.
    :para n: Valor recebido. 
    :Return: Valor formatado em forma de Real.
    """
    return  f'R$ {v:,.2f}'.replace('.', ',')