extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
verificador = (0, 1, 2, 3,4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

num = input('Digite um número entre 0 e 20: ')
while num.isdigit() == False:
    num = input('Por favor. Digite um número entre 0 e 20: ')

num = int(num)

print(f'Você digitou o número {extenso[num]}')
