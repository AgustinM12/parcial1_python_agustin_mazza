import pandas as pd
# * Importacion de pandas con el alias pd.
import random as rd
# * importacion de la libreria random de python con el alis de rd.

# * Lista de productos
productos = [
{"nombre": "Camiseta", "precio": 20, "cantidad_disponible":100},
{"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
{"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
{"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
{"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
{"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
{"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
{"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
{"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
{"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":25},
{"nombre": "Calcetines", "precio": 10, "cantidad_disponible":150},
{"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
{"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
{"nombre": "Pendientes", "precio": 15, "cantidad_disponible":180},
{"nombre": "Cinturón", "precio": 20, "cantidad_disponible":100},
{"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
{"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
{"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
{"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
{"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

# * Se crea el dataframe a partir de la lista proporcionada.
df = pd.DataFrame(productos, columns=["nombre", "precio", "cantidad_disponible"])

#print(df)

# * 1. Se calcula el valor total del inventario de cada producto y se muestra
df["valor_total"] = df["precio"] * df["cantidad_disponible"]

#print(df["valor_total"])

# * 2. Se calcula el valor acumulado del inventario y se muestra el total, es decir la ultima posición del acumulado. 
#print(df["valor_total"].cumsum()[-1:])

# * 3. Simular algunas ventas y actualizar la cantidad disponible de productos vendidos.

# * funcion para calcular ventas mediante un numero random entre 0 y el numero minimo de la columna "cantidad_disponible"
def ventas_random(cantidad_disponible):
    ventas = cantidad_disponible - rd.randint(0,df["cantidad_disponible"].min())
    return ventas

df["cantidad_disponible"] = df["cantidad_disponible"].apply(ventas_random)


# * 4 Mostrar la cantidad restante disponible de cada producto después de las ventas simuladas.
#print(df[["nombre","cantidad_disponible"]])


# * 5 Crea un DataFrame que incluya dos columnas una para los nombres de los productos y otra para la cantidad disponible de cada producto.

new_df = df[["nombre", "cantidad_disponible"]]

#print(new_df)
