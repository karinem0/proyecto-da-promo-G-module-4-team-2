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


cambio_unknow = "hotel", 

cambio_media_mediana = "lead_time"


#columnas OK
# is_canceled
# stays_in_weekend_nights	
# stays_in_week_nights
# country

# #Completar info descriptiva 
# meal
# reserved_room_type
# assigned_room_type

#Columnas revisar 
# arrival_date_day_of_month (16 valores) - valores numericos y nombre
# arrival_date_week_number (54 valores) Quietar 0 
# arrival_date_day_of_month (32 valores revisar si es por valor nulo) Quitar 0
# IS_REPEATED_GUEST (cambiar a SI/NO - Nulos desconocidos)
# PREVIOUS_BOOKINGS_NOT_CANCELED (cambiar int)
# booking_changes (gestionar nulos mirar relacion con cancelacion)
# AGENT (cambiar int)
# days_in_waiting_list (cambiar int)- propuesta politica cancelaciones
# adr (imputacion nulos)
# required_car_parking_spaces (imputacion nulos)
# total_of_special_requests (cambiar a int)
# reservation_status (gestion nulos)
# reservation_status_date (gestion datas)


# #Preguntar 
# stays_in_weekend_nights (Quitar decimales )
# stays_in_week_nights (Quitar decimales )
# adults	(valores muy altos)
# children (revisar valores altos)
# DISTRIBUTION_CHANNEL
# PREVIOUS_CANCELLATIONS
# customer_type

# # Valorar eliminacion 
# MARKET_SEGMENT (50% nulos) - ligada a DISTRIBUTION_CHANNEL
# COMPANY (90% Nulos)
# '0'


# %%
df_sin_duplicados[df_sin_duplicados["previous_cancellations"] >10]
# %%
