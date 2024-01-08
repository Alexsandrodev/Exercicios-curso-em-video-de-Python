casa = float(input('informe o valor da casa: R$'))
salario = float(input('informe o seu salário: R$'))
anos = int(input('informe com quantos anos você ira pagar: '))

parcelas = casa / (anos * 12)
porcentagem = salario * 30 / 100

if parcelas <= porcentagem:
    print('você pode fazer o emprestimo!')
    print(f'O valor da parcela será de R${parcelas:.2f} ao mês')
else:
    print('Infelizmente você não pode comprar a casa!')
    print(f'O valor de parcela é de R${parcelas:.2f} e o valor máximo de parcelar para você é de R${porcentagem}')