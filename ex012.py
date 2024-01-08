valor = float(input('Qual o valor do seu produto? R$'))

desc = valor * 5 / 100
valorf = valor - desc

print(f'O valor do seu produto é de R${valor:.2f}, e esse produto com o desconto de 5% é igual a R${valorf:.2f}')