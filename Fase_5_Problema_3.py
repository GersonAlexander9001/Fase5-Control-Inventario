
# Nombre del estudiante: Gerson Alexander Hinestroza Peña
# Grupo: 213022_336
# Programa: Ingeniería de Sistemas
# Problema 3: Control de inventario
# Código fuente: autoría propia


# R3 y R4: Función para calcular la cantidad que se debe solicitar
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


print("=== CONTROL DE INVENTARIO ===")


# R1: Crear matriz con cinco artículos
# Cada fila contiene: código, nombre, stock actual y stock mínimo

inventario = [
    ["A01", "Arroz", 8, 20],
    ["A02", "Aceite", 15, 10],
    ["A03", "Azúcar", 5, 15],
    ["A04", "Café", 12, 12],
    ["A05", "Leche", 4, 18]
]


# R2: Recorrer la matriz para revisar cada artículo
print("\n===== RESULTADOS DEL INVENTARIO =====")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # R4 y R5: Calcular la cantidad que se debe solicitar
    cantidad_pedido = calcular_pedido(stock_actual, stock_minimo)

    # R6: Mostrar el nombre y la cantidad a solicitar
    print(f"\nCódigo: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Cantidad a solicitar: {cantidad_pedido} unidades")


print("\n===== FIN DEL REPORTE =====")
