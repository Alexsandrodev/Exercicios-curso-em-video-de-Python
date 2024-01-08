# Funções
def factorial(f, show=False):
    """
    -> Retorna o fatorial do numero.
    :Para f: Numero a ser calcular.
    :para show: se sera ou não mostrado o processo.
    :return: 0 do fatoria de f.
    """
    
    if show == True:
        for n in range(f, 0, -1):
            if n > 1:
                print(f"{n} x ", end='')
            else:
                print(f'{n} = ', end='')

    for n in range(f-1, 1, -1):
        f *= n
    
    return f

# Programa principal

print(factorial(5, True))