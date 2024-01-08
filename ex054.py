from datetime import date

jovens = []
adultos = []

"""
jovens = 0
adultos = 0
"""
atual = date.today().year 

for c in range(1, 8):
    data = int(input('digite a {}° datas de nascimento:'.format(c)))
    
    idade = atual - data 
    if idade < 21:
        jovens.append(1)
    else:
        adultos.append(1)

    """
    if idade < 21:
        jovens += 1
    else:
        adultos += 1
    """
        

print('''{} Pessoas ainda faltam atingir a maior idade
{} pessoas já aingiram a maior idade'''.format(len(jovens), len(adultos)))