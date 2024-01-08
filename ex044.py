preco = float(input('infome o preço do produto: R$'))
forma = int(input('''informe a forma de pagamento: 
[1] À vista dinheiro ou cheque. 
[2] À vista no cartão. 
[3] em até 2x no cartão. 
[4] 3x ou mais no cartão.
'''))

if forma == 1:
    valorF =  preco - (preco * 10 / 100) 
    print(f'O valor final com o descoto de 10% sera de R${valorF:.2f}')
elif forma == 2:
    valorF =  preco - (preco * 5 / 100) 
    print(f'O valor final com o descoto de 5% sera de R${valorF:.2f}')    
elif forma == 3:
    print('O valor final será o mesmo de R${:.2f}'.format(preco))
elif forma == 4:
    valorF =  preco + (preco * 20 / 100) 
    print(f'O valor final com o aumento de 20% de juros sera de R${valorF:.2f}') 