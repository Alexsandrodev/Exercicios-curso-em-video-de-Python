slr = float(input('Qual é o salário do funcionario? R$'))

aumento = slr * 15 / 100
novoS = aumento + slr

print(f'Um funionário que ganhava R${slr:.2f}, com um almento de 15% passa a receber R$ {novoS:.2f}')