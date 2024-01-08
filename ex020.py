import random

nome1 = input('Primeiro aluno:')
nome2 = input('Segundo aluno:')
nome3 = input('Terceiro aluno:')
nome4 = input('quarto aluno:')

names = [nome1, nome2, nome3, nome4]
random.shuffle(names)

print(f'A ordem de aprasentação sera')
print(names)