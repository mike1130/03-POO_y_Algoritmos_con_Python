import random

#BigO(n**2)

def bubble_sort(lista):
    n = len(lista)

    iter_i = 0
    iter_j = 0

    for i in range(n):
        iter_i += 1
        for j in range(0, n - i - 1):
            iter_j += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1]= lista[j + 1], lista[j]

    return lista, iter_i, iter_j

def main():
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
 
    lista = [random.randint(0, 100) for i in range (tamano_de_lista)]
    print(lista)

    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada[0], lista_ordenada[1], lista_ordenada[2])


if __name__ == '__main__':
    main()
