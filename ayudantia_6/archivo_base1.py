def extrae_digito(n, d):
    pass

def dibujar_rectangulo(base, altura):
    pass

def main():
    ## Funcionalidad codigo ##



    ## Funcionalidad codigo ##

    numero_generado = extrae_digito(int(n), int(d))
    print("Número generado en orden inverso:", numero_generado)

    base = int(max(numero_generado))
    altura = int(min(numero_generado))
    print("\nDibujo del rectángulo:")
    dibujar_rectangulo(base, altura)

if __name__ == "__main__":
    main()
