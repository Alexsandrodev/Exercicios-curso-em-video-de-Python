# variaveis
expressao = ''
pilha = []

# entrada de dados

expressao = input('Digite uma expressão: ')
for simb in pilha:
    if simb == '()':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

# Saida
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão está errada')