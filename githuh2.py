def func1 (a):
    return sum (a), sum (a)/len (a) 


def substituir_palavra (lista, procurada, nova):
    for i in range(len(lista)):
        if lista[i] == procurada:
            lista[i] = nova
   
    return lista

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print ('*' * i)
