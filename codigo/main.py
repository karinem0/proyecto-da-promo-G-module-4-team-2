#%%
from src import soporte_proyecto as sp
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#%%
## 🛠️ Apertura CSV

df_hotel = sp.apertura_csv("../files/finanzas-hotel-bookings.csv",True)
df_hotel.name = "CSV Hotel"

## 🛠️ Cambio nombre columnas
sp.cambio_nombre_columnas_df(df_hotel)

#display(df_hotel.head(2))

# 🛠️ Eliminacion duplcados

# sp.exploracion_df(df_hotel)

df_sin_duplicados = df_hotel.drop_duplicates()
df_sin_duplicados.name = "Hotel - Historial sin duplicados"
print(f"El número de filas que tenemos es {df_sin_duplicados.shape[0]}, y el número de columnas es {df_sin_duplicados.shape[1]}")
print(f"Nº Duplicados despues de la limpieza: {df_sin_duplicados.duplicated().sum()}")

# 🛠️ Eliminacion de columnas
df_sin_duplicados.drop(columns= ["0","company", "market_segment"], inplace=True)


# 🛠️ Gestion de nulos

# Columnas no modificadas (dejamos valores nulos)
# ARRIVAL_DATE_YEAR, ARRIVAL_DATE_MONTH, ARRIVAL_DATE_WEEK_NUMBER, ARRIVAL_DATE_WEEK_NUMBER,  AGENT, REQUIRED_CAR_PARKING_SPACES, RESERVATION_STATUS_DATE


cambio_unknow = ["hotel", "is_canceled", "meal", "country", "distribution_channel", "is_repeated_guest", "reserved_room_type", "assigned_room_type", "customer_type", "reservation_status"]

cambio_media_mediana = ["lead_time", "stays_in_weekend_nights", "stays_in_week_nights","booking_changes", "days_in_waiting_list","adr", "total_of_special_requests"]

cmabio_map = "children", "babies"

columnas_a_revisar = "adults", "previous_cancellations", "previous_bookings_not_canceled"


for col in cambio_media_mediana:
    sp.imputar_valores_nulos(df_sin_duplicados,col)

for col in cambio_unknow:
    sp.imputar_valores_nulos_categoricas(df_sin_duplicados,col,"Unknow")


# 🛠️ Cambio valores columnas

cambiar_int =  ["lead_time","arrival_date_year","arrival_date_week_number","arrival_date_day_of_month","stays_in_weekend_nights","stays_in_week_nights","adults","previous_cancellations","previous_bookings_not_canceled","booking_changes","agent","days_in_waiting_list","adr","required_car_parking_spaces","total_of_special_requests"]

cambiar_positivo = ["adr"]

for col in cambiar_int:
    df_sin_duplicados[col] = df_sin_duplicados[col].apply(sp.cambio_int)

sp.negativos(df_sin_duplicados,"adr")

meses = { "1": "January", "2": "February", "3": "March", "April": "April", "May": "May", "June": "June", "July": "July", "August": "August", "September": "September", "October": "October", "November": "November","December": "December","January": "January", "February": "February", "March": "March"}

df_sin_duplicados["arrival_date_month"] = df_sin_duplicados["arrival_date_month"].map(meses)


df_sin_duplicados["viajan_con_niños"] = df_sin_duplicados["children"].apply(sp.cambio_categorica)
df_sin_duplicados["viajan_con_bebes"] = df_sin_duplicados["babies"].apply(sp.cambio_categorica)
df_sin_duplicados["is_repeated_guest"] = df_sin_duplicados["is_repeated_guest"].apply(sp.cambio_categorica)

cambio_habitacion = ["reserved_room_type", "assigned_room_type"]

for col in cambio_habitacion:
    df_sin_duplicados[col] = df_sin_duplicados[col].apply(sp.cambio_habitacion_hotel)


df_sin_duplicados["distribution_channel"] = df_sin_duplicados["distribution_channel"].str.replace("Unknow","Undefined")
df_sin_duplicados["meal"] = df_sin_duplicados["meal"].str.replace("Unknow","Undefined")
df_sin_duplicados["meal"] = df_sin_duplicados["meal"].apply(sp.cambio_regimen_pension)
df_sin_duplicados["reservation_status_date"] = df_sin_duplicados["reservation_status_date"].str.split(" ", expand = True).get([0])




# %%
