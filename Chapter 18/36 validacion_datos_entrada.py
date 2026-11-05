def validar_dato(dato, minimo, maximo):
    if dato < minimo:
        return minimo
    elif dato > maximo:
        return maximo
    return dato

# Ejemplo de uso
nivel = obtener_nivel_embalse()
nivel_validado = validar_dato(nivel, 400, 600)
ajustar_valvula(nivel_validado)