frase = str(input('Digite uma frase: ')).lower().strip()


separador = frase.split()
juncao = ''.join(separador)
inverso = ''


for letras in range(len(juncao) -1, -1, -1):
    inverso += juncao[letras]

print('O inverso de {} é {}'.format(juncao, inverso))

if juncao == inverso:
    print('A frase digitada é um palíndromo ')
else:
    print('A frase digitada não é um palíndromo')