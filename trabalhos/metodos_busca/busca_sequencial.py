'''
Sequential Search

**Computational complexity**:
 - best case = 1
 - Worst Case = n
 - Average Case = n/2

**Advantages**:
 - Simple
 - small data

**Disadvantages**:
 - high computational complex
 - big data is slow
 - inefficient
'''


def busca_sequencial_for(lista, valor_procurado):
    for i in range(len(lista)):
        if lista[i] == valor_procurado:
            return True;
    return False


def busca_sequencial_while(lista, valor_procurado):
    indice = 0
    found = False

    while indice < len(lista):
        if lista[indice] == valor_procurado:
            found == True
        else:
            indice += 1
    return found


# test
lista = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(busca_sequencial_for(lista, 13))
print(busca_sequencial_while(lista, 3))


# love python
print("\nlove python")
print(42 in lista)
