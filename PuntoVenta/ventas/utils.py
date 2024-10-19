

def validar_dpi(dpi):
    dpi = dpi.replace('-', '').replace(' ', '')  # Elimina guiones y espacios

    if len(dpi) != 13:
        return False  # Longitud no válida para DPI

    try:
        # Los primeros 12 dígitos son el número del DPI, el último dígito es el dígito verificador
        digito_verificador = int(dpi[-1])
        numeros = list(map(int, dpi[:-1]))

        suma = 0
        multiplicador = 2
        for digito in reversed(numeros):
            suma += digito * multiplicador
            multiplicador = 1 if multiplicador == 2 else 2

        residuo = suma % 10
        digito_calculado = (10 - residuo) % 10

        return digito_calculado == digito_verificador
    except ValueError:
        return False
