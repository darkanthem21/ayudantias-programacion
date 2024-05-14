def detectives_por_unidad() -> dict:
    D = dict()
    ruts = set()
    
    return D

def valida_caso_de_reincidente(ID_caso: str, criminales: list, cargos: list, RUT_detective:str ) -> int:
    try:
        pass
    except Exception as msj:
        return(msj)
    return(0)

def main():
    dect = detectives_por_unidad()
    print(f"los detectives son: {dect}")

    res0 = valida_caso_de_reincidente("123",["15.435.633-7"],"Portonazo","17.438.834-K")
    print(f"Se pudo ingresar el caso 0? {res0}")

    res1 = valida_caso_de_reincidente("3556",["15.435.633-7"],"Portonazo","17.438.834-K")
    print(f"Se pudo ingresar el caso 1? {res1}")

    res2 = valida_caso_de_reincidente("1234",["15.435.633-2"],"Portonazo","17.438.834-K")
    print(f"Se pudo ingresar el caso 2? {res2}")

    res3 = valida_caso_de_reincidente("1236",["15.435.633-7"],"Portonazo","17.438.834-1")
    print(f"Se pudo ingresar el caso 3? {res3}")

    res4 = valida_caso_de_reincidente("123",["15.437.535-2"],"Portonazo","17.438.834-1")
    print(f"Se pudo ingresar el caso 4? {res4}")

if __name__ == "__main__":
    main()
