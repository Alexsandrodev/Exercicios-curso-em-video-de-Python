pesos = []

for c in range(1,6):
    peso = float(input('informe o peso da {}° pessoa em kilos: '.format(c, end=' '))) 
    pesos.append(peso)
    
print('O maior peso informado foi {}Kg.'.format(max(pesos)))
print('O menor peso informado foi {}Kg.'.format(min(pesos)))