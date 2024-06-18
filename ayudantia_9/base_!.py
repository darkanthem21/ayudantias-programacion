def retorna_edad_mas_cercana(modelos: list, edad: int) -> int:
    pass

def main():
    modelos = [1, 2, 4, 6, 7, 10, 11, 13, 16, 17, 18, 18, 19, 20, 22,
    22, 22, 23, 24, 24, 25, 26, 26, 26, 27, 28, 28,29, 31,
    32, 33, 34, 36, 37, 39, 43, 44, 45, 47, 51, 52, 53, 57,
    58, 59, 61, 62, 65, 66, 66, 67, 67, 68, 71, 72, 73, 76,
    78, 81, 83, 84, 86, 91]
    print(retorna_edad_mas_cercana(modelos,75))

if __name__ == "__main__":
    main()
