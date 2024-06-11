def es_palindromo(numero_str):
    # Caso base: si la longitud de la cadena es 0 o 1, es palíndromo
    if len(numero_str) <= 1:
        return True
    
    # Verificamos si el primer y último dígito son iguales
    if numero_str[0] != numero_str[-1]:
        return False
    
    # Caso recursivo: si el primer y último dígito son iguales, verificamos el siguiente dígito de la cadena
    return es_palindromo(numero_str[1:-1])
