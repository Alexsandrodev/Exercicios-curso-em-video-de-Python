#importaçoes
from time import sleep
#variaveis
saque = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

print('-=-' * 10)
print('Iniando Caixa Eletronico ')
print('-=-' * 10)
sleep(2)

while True:
    #Entrada
   
    saque = input('valor a ser sacado: R$').strip()
    print('-=-' * 10)
    sleep(1)

    #Verificador
    while type(saque) == str:
        try:
            saque = int(saque)
        except ValueError:
            print('Por favor!')
            print('Digite apenas numeros inteiros')
            saque = input('valor a ser sacado: ')
        
    #Calculo de cedulas
    while saque > 0:
        if saque >= 50:
            saque -= 50
            nota50 += 1

        elif saque >= 20:
            saque -= 20
            nota20 += 1  

        elif saque >= 10:
            saque -= 10
            nota10 += 1 

        elif saque >= 5:
            saque -= 5
            nota5 += 1  

        else:
            saque -= 1
            nota1 += 1

    #Parada
    if saque == 0:
        break

#Saidas
if nota50 > 0:
    print(f'total de {nota50}  notas de R$ 50,00')

if nota20 > 0:
    print(f'total de {nota20} notas de R$ 20,00')

if nota10 > 0:
    print(f'total de {nota10} notas de R$ 10,00')

if nota5 > 0:
    print(f'total de {nota5} notas de R$ 5,00')

if nota1 > 0:
    print(f'total de {nota1} notas de R$ 1,00')