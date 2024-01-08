salario = float(input('Qual o sálario do funcionario? R$'))

if salario > 1250.00:
    aumento = (salario * 10 / 100) + salario
else:
    aumento = (salario * 15 / 100) + salario
    
print(f'Quem ganhava R${salario} vai passar a ganhar R${aumento}')