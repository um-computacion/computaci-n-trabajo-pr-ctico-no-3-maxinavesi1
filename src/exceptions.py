def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.

    Returns:
        int: El número ingresado si es válido.

    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero

