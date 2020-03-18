# PROGRAMA PRICIPAL PARA O CALCULO DO CLEARSKY BASEADO NO METODO DE DUMORTIER
import pandas as pd
from image_turbidity import image_turbidity
from durmotier_corrected_hour import corrected_hour

data = pd.read_excel('BRASIL_Lon_Lat.xlsx', sheet_name='Plan1')
for i in range(data['LAT'].count()):
    latitude = data['LAT'][i]
    longitude = data['LON'][i]
    altitude = data['ALTITUDE (m)'][i]
    station = data['NOME'][i]
    ID = data['ID'][i]
    year = 2016

    # print(latitude,longitude, altitude, station, ID)
    turbidity = image_turbidity(latitude, longitude)
    # print(turbidity)

    clear_sky_hour_total = []

    for y in range(2015,year+1):
        clear_sky_hour = corrected_hour(y, latitude, longitude, altitude, turbidity)
        clear_sky_hour_total.append(clear_sky_hour)
    
    print(clear_sky_hour_total)
    print()
