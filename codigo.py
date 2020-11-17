from math import prod

n = int(input("Introduce un numero entero: "))
print(n)

def primer_persistente(n):
    digitos = [int(i) for i in str(n)] # Lista con los digitos separados
    persistencia = prod(digitos) # Producto de todos los digitos

    if len(digitos) != 1:
        print(persistencia)
        return 1 + primer_persistente(persistencia)
    else:
        return 0

pasos = primer_persistente(n)
print("Los pasos que se han llevado a cabo son:", pasos)