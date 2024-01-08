from time import sleep
print('Hora dos fogos')

for c in range(10, -1, -1):
    print('\033[34m {}\033[m'.format(c))
    sleep(1)
    
print('\033[32mFeliz ano novo!\033[m')