#%%
from src import soporte_proyecto as sp
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# %%
## Apertura CSV

df_hotel = sp.apertura_csv("../files/finanzas-hotel-bookings.csv",True)
df_hotel.name = "CSV Hotel"

## Cambio nombre columnas
sp.cambio_nombre_columnas_df(df_hotel)

#%%
display(df_hotel.head(2))

sp.exploracion_df(df_hotel)
#%%
df_sin_duplicados = df_hotel.drop_duplicates()
df_sin_duplicados.name = "Hotel - Historial sin duplicados"
print(f"El número de filas que tenemos es {df_sin_duplicados.shape[0]}, y el número de columnas es {df_sin_duplicados.shape[1]}")
print(f"Nº Duplicados despues de la limpieza: {df_sin_duplicados.duplicated().sum()}")

#%%
sp.exploracion_col_df(df_sin_duplicados)
#%%
sp.comprobacion_valores_nulos(df_sin_duplicados)
# %%
