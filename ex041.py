import datetime

ano = int(input('Informe o ano de nascimento do participante: '))

idade = datetime.date.today().year - ano

if idade <= 9:
    print('Categoria: \033[0;32mMIRIN\033[m')
elif idade <= 14:
    print('Categoria: \033[0;32mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[0;32mJUNIOR\033[m')
elif idade <= 20:
    print('Categoria: \033[0;32mSênior\033[m')    
else:
    print('Categoria: \033[0;32mMASTER\033[m')