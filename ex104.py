# Funções
def leiaint(msg):
    num = input(msg)
    while num != int:
        try:
            num = int(num)
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            num = input(msg)

        return(num)    


#Programa principal
n = leiaint('digite um número: ') 
print(f'Você digitou o numero {n}')