import random

nome1 = input('Primeiro aluno:')
nome2 = input('Segundo aluno:')
nome3 = input('Terceiro aluno:')
nome4 = input('quarto aluno:')

names = []

names.append(nome1)
names.append(nome2)
names.append(nome3)
names.append(nome4)

print(f'O aluno escolhido foi {random.choice(names)}')