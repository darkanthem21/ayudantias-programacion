def extrae_digito(n, d):
    return n.replace(str(d), '')[::-1]

def dibujar_rectangulo(base, altura):
    for i in range(altura):
        for j in range(base):
            if i == 0 or i == altura - 1 or j == 0 or j == base - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    while True:
        n = input("Ingrese un número entero positivo con 5 o más dígitos: ")
        if n.isdigit() and len(n) >= 5 and int(n) > 0:
            break
        print("Ingrese un número válido.")  

    while True:
        d = input("Ingrese un dígito (0-9): ")
        if d.isdigit() and 0 <= int(d) <= 9:
            break
        print("Ingrese un dígito válido.")

    numero_generado = extrae_digito(n, d)
    print("Número generado en orden inverso:", numero_generado)

    base = int(max(numero_generado))
    altura = int(min(numero_generado))
    print("\nDibujo del rectángulo:")
    dibujar_rectangulo(base, altura)

if __name__ == "__main__":
    main()
