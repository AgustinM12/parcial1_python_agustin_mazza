import matplotlib.pyplot as plt
# * importacion matplotlib con el alias de plt
from ejercicio_pandas import new_df as df
# * importacion del modulo new_df (con el alias df) del fichero de la actividad de pandas.

plt.bar(df["nombre"], df["cantidad_disponible"], color="red")
plt.title("Productos y su disponibilidad")
plt.xlabel("Nombre de los productos")
plt.ylabel("Cantidad disponible")
plt.show()