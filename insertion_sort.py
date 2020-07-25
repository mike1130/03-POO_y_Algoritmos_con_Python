import random

#BigO(n**2)

def insertion_sort(lista):
    iter_indice = 0
    iter_posicion_actual = 0

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        iter_indice += 1

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            iter_posicion_actual += 1

        lista[posicion_actual] = valor_actual

    return lista, iter_indice, iter_posicion_actual   


def main():
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
 
    lista = [random.randint(0, 100) for i in range (tamano_de_lista)]
    print(lista)

    lista_ordenada = insertion_sort(lista)
    print(lista_ordenada[0], lista_ordenada[1], lista_ordenada[2])


if __name__ == '__main__':
    main()