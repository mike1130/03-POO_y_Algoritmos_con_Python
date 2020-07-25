import random

#BigO(n**2)

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo >final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo) 
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
        


def main():
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range (tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

if __name__ == '__main__':
    main()
