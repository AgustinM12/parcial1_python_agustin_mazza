import matplotlib.pyplot as plt
# * importacion matplotlib con el alias de plt.
from ejercicio_pandas import new_df as df
# * importacion del modulo new_df (con el alias df) del fichero de la actividad de pandas.

# * definir el grafico de barras con los ejes x e y indicados.
plt.bar(df["nombre"], df["cantidad_disponible"], color="red")

# * titulo del grafico. 
plt.title("Productos y su disponibilidad")

# * label del eje x.
plt.xlabel("Nombre de los productos")

# * label del eje Y.
plt.ylabel("Cantidad disponible")

# * Mostrar el grafico.
plt.show()