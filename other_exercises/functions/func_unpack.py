def calcular(importe, descuento):
    return importe - (importe * descuento / 100)


# Paso de tuplas
datos = [1500, 10]
print(calcular(*datos))


# Paso de diccionario
datos = {"descuento": 10, "importe": 1200}
print(calcular(**datos))
