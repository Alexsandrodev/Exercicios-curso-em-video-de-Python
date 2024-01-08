dias = int(input('Você ficou quantos dias com o carro? '))
kms = int(input('Você rodou quantos Km? '))

SomaD = dias * 60
SomaK = kms * 0.15
valor = SomaD + SomaK

print(f'você ficou {dias} dias com o carro e rodou {kms}kms, então você deve R${valor:.2f}')