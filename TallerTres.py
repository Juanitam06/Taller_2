def es_primo(numero):
    if numero <= 1:
        return False
    else:
        if numero <= 3:
            return True
        else:
            if numero % 2 == 0 or numero % 3 == 0:
                return False
            else:
                i = 5
                while i * i <= numero:
                    if numero % i == 0 or numero % (i + 2) == 0:
                        return False
                    i += 6
                return True

def imprimir_impares(numero):
    print("Números impares entre -{} y {}:".format(numero, numero))
    for i in range(-numero, numero + 1):
        if i % 2 != 0:
            print(i, end=" ")

def imprimir_primos(numero):
    print("\nNúmeros primos entre 0 y {}:".format(numero * 100))
    for i in range(numero * 100 + 1):
        if es_primo(i):
            print(i, end=" ")

def main():
    while True:
        try:
            numero = int(input("Ingrese un número mayor que 0: "))
            if numero <= 0:
                print("Por favor, ingrese un número mayor que 0.")
                continue
            imprimir_impares(numero)
            imprimir_primos(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main() 