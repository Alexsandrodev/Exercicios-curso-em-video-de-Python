cores = {'\33[m33'}

def leiaint(msg):
    while True:
        try:
            num = input(msg).strip()
            num = int(num)
            break

        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[0;31mO Usuário preferio não digitar esse numero.\033[m')
            num = 0
            break

        except Exception as erro:
             print(f'\n\033[0;31mErro de {erro.__cause__}.\033[m')

    return(num)
    