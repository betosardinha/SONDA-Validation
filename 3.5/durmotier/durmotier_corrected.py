import calendar
import numpy as np

def corrected_hour(year, latitude, longitude, altitude, turbidity):
    # Ls A LONGITUDE PADRAO PARA O BRASIL É DE -45. SE QUISER USAR UTC, Ls = 0
    Ls = 0

    # SERA CALCULADO SE O ANO É BISSEXTO E QUANTAS HORAS E MINUTOS EXISTEM EM UM ANO
    days_year = 366 if calendar.isleap(year) else 365
    days = np.arange(1, days_year+1)
    hour_year = days_year*24

    # QUANTOS MINUTOS E HORAS EXISTEM EM UM ANO
    minutes = []
    hours = []
    for i in range(days_year):
        for j in range(1440):
            minutes.append(j+1)
        for k in range(24):
            hours.append(k+1)

    # FAZENDO O CABECARIO PARA A COLUNA DO ANO
    year_minutes = []
    year_hours = []
    for i in range(days_year):
        for j in range(1440):
            year_minutes.append(year)
        for k in range(24):
            year_hours.append(year)

    # AJUSTE DO DIA JULIANO PARA O ANO EM QUESTAO EM MINUTOS OU HORAS
    day_jul_minutes = []
    day_jul_hours = []
    for i in range(days_year):
        for j in range(1440):
            day_jul_minutes.append(days[i])
        for k in range(24):
            day_jul_hours.append(days[i])

    # CALCULO DOS MESES COM BASE NO DIA JULIANO PARA CADA MINUTO
    month_minute = []
    for i in range(day_jul_minutes[-1]*1440):
        if days_year == 366:
            if day_jul_minutes[i] <= 31:
                month_minute.append(1)
            elif day_jul_minutes[i] > 31 and day_jul_minutes[i] <= 60:
                month_minute.append(2)
            elif day_jul_minutes[i] > 60 and day_jul_minutes[i] <= 91:
                month_minute.append(3)
            elif day_jul_minutes[i] > 91 and day_jul_minutes[i] <= 121:
                month_minute.append(4)
            elif day_jul_minutes[i] > 121 and day_jul_minutes[i] <= 152:
                month_minute.append(5)
            elif day_jul_minutes[i] > 152 and day_jul_minutes[i] <= 182:
                month_minute.append(6)
            elif day_jul_minutes[i] > 182 and day_jul_minutes[i] <= 213:
                month_minute.append(7)
            elif day_jul_minutes[i] > 213 and day_jul_minutes[i] <= 244:
                month_minute.append(8)
            elif day_jul_minutes[i] > 244 and day_jul_minutes[i] <= 274:
                month_minute.append(9)
            elif day_jul_minutes[i] > 274 and day_jul_minutes[i] <= 305:
                month_minute.append(10)
            elif day_jul_minutes[i] > 305 and day_jul_minutes[i] <= 335:
                month_minute.append(11)
            elif day_jul_minutes[i] > 335 and day_jul_minutes[i] <= 366:
                month_minute.append(12)
        else:
            if day_jul_minutes[i] <= 31:
                month_minute.append(1)
            elif day_jul_minutes[i] > 31 and day_jul_minutes[i] <= 59:
                month_minute.append(2)
            elif day_jul_minutes[i] > 59 and day_jul_minutes[i] <= 90:
                month_minute.append(3)
            elif day_jul_minutes[i] > 90 and day_jul_minutes[i] <= 120:
                month_minute.append(4)
            elif day_jul_minutes[i] > 120 and day_jul_minutes[i] <= 151:
                month_minute.append(5)
            elif day_jul_minutes[i] > 151 and day_jul_minutes[i] <= 181:
                month_minute.append(6)
            elif day_jul_minutes[i] > 181 and day_jul_minutes[i] <= 212:
                month_minute.append(7)
            elif day_jul_minutes[i] > 212 and day_jul_minutes[i] <= 243:
                month_minute.append(8)
            elif day_jul_minutes[i] > 243 and day_jul_minutes[i] <= 273:
                month_minute.append(9)
            elif day_jul_minutes[i] > 273 and day_jul_minutes[i] <= 304:
                month_minute.append(10)
            elif day_jul_minutes[i] > 304 and day_jul_minutes[i] <= 334:
                month_minute.append(11)
            elif day_jul_minutes[i] > 334 and day_jul_minutes[i] <= 365:
                month_minute.append(12)

    # CALCULO DOS MESES COM BASE NO DIA JULIANO PARA CADA HORA
    month_hour = []
    for i in range(day_jul_hours[-1]*24):
        if days_year == 366:
            if day_jul_hours[i] <= 31:
                month_hour.append(1)
            elif day_jul_hours[i] > 31 and day_jul_hours[i] <= 60:
                month_hour.append(2)
            elif day_jul_hours[i] > 60 and day_jul_hours[i] <= 91:
                month_hour.append(3)
            elif day_jul_hours[i] > 91 and day_jul_hours[i] <= 121:
                month_hour.append(4)
            elif day_jul_hours[i] > 121 and day_jul_hours[i] <= 152:
                month_hour.append(5)
            elif day_jul_hours[i] > 152 and day_jul_hours[i] <= 182:
                month_hour.append(6)
            elif day_jul_hours[i] > 182 and day_jul_hours[i] <= 213:
                month_hour.append(7)
            elif day_jul_hours[i] > 213 and day_jul_hours[i] <= 244:
                month_hour.append(8)
            elif day_jul_hours[i] > 244 and day_jul_hours[i] <= 274:
                month_hour.append(9)
            elif day_jul_hours[i] > 274 and day_jul_hours[i] <= 305:
                month_hour.append(10)
            elif day_jul_hours[i] > 305 and day_jul_hours[i] <= 335:
                month_hour.append(11)
            elif day_jul_hours[i] > 335 and day_jul_hours[i] <= 366:
                month_hour.append(12)
        else:
            if day_jul_hours[i] <= 31:
                month_hour.append(1)
            elif day_jul_hours[i] > 31 and day_jul_hours[i] <= 59:
                month_hour.append(2)
            elif day_jul_hours[i] > 59 and day_jul_hours[i] <= 90:
                month_hour.append(3)
            elif day_jul_hours[i] > 90 and day_jul_hours[i] <= 120:
                month_hour.append(4)
            elif day_jul_hours[i] > 120 and day_jul_hours[i] <= 151:
                month_hour.append(5)
            elif day_jul_hours[i] > 151 and day_jul_hours[i] <= 181:
                month_hour.append(6)
            elif day_jul_hours[i] > 181 and day_jul_hours[i] <= 212:
                month_hour.append(7)
            elif day_jul_hours[i] > 212 and day_jul_hours[i] <= 243:
                month_hour.append(8)
            elif day_jul_hours[i] > 243 and day_jul_hours[i] <= 273:
                month_hour.append(9)
            elif day_jul_hours[i] > 273 and day_jul_hours[i] <= 304:
                month_hour.append(10)
            elif day_jul_hours[i] > 304 and day_jul_hours[i] <= 334:
                month_hour.append(11)
            elif day_jul_hours[i] > 334 and day_jul_hours[i] <= 365:
                month_hour.append(12)

    # CALCULO DOS DIAS COM BASE NOS MESES PARA CADA MINUTO E HORA
    day_minute = []
    for i in range(day_jul_minutes[-1]*1440):
        if days_year == 366:
            if month_minute[i] == 1:
                day_minute.append(day_jul_minutes[i])
            elif month_minute[i] == 2:
                day_minute.append(day_jul_minutes[i] - 31)
            elif month_minute[i] == 3:
                day_minute.append(day_jul_minutes[i] - 60)
            elif month_minute[i] == 4:
                day_minute.append(day_jul_minutes[i] - 91)
            elif month_minute[i] == 5:
                day_minute.append(day_jul_minutes[i] - 121)
            elif month_minute[i] == 6:
                day_minute.append(day_jul_minutes[i] - 152)
            elif month_minute[i] == 7:
                day_minute.append(day_jul_minutes[i] - 182)
            elif month_minute[i] == 8:
                day_minute.append(day_jul_minutes[i] - 213)
            elif month_minute[i] == 9:
                day_minute.append(day_jul_minutes[i] - 244)
            elif month_minute[i] == 10:
                day_minute.append(day_jul_minutes[i] - 274)
            elif month_minute[i] == 11:
                day_minute.append(day_jul_minutes[i] - 305)
            elif month_minute[i] == 12:
                day_minute.append(day_jul_minutes[i] - 335)
        else:
            if month_minute[i] == 1:
                day_minute.append(day_jul_minutes[i])
            elif month_minute[i] == 2:
                day_minute.append(day_jul_minutes[i] - 31)
            elif month_minute[i] == 3:
                day_minute.append(day_jul_minutes[i] - 59)
            elif month_minute[i] == 4:
                day_minute.append(day_jul_minutes[i] - 90)
            elif month_minute[i] == 5:
                day_minute.append(day_jul_minutes[i] - 120)
            elif month_minute[i] == 6:
                day_minute.append(day_jul_minutes[i] - 151)
            elif month_minute[i] == 7:
                day_minute.append(day_jul_minutes[i] - 181)
            elif month_minute[i] == 8:
                day_minute.append(day_jul_minutes[i] - 212)
            elif month_minute[i] == 9:
                day_minute.append(day_jul_minutes[i] - 243)
            elif month_minute[i] == 10:
                day_minute.append(day_jul_minutes[i] - 273)
            elif month_minute[i] == 11:
                day_minute.append(day_jul_minutes[i] - 304)
            elif month_minute[i] == 12:
                day_minute.append(day_jul_minutes[i] - 334)

    day_hour = []
    for i in range(day_jul_hours[-1]*24):
        if days_year == 366:
            if month_hour[i] == 1:
                day_hour.append(day_jul_hours[i])
            elif month_hour[i] == 2:
                day_hour.append(day_jul_hours[i] - 31)
            elif month_hour[i] == 3:
                day_hour.append(day_jul_hours[i] - 60)
            elif month_hour[i] == 4:
                day_hour.append(day_jul_hours[i] - 91)
            elif month_hour[i] == 5:
                day_hour.append(day_jul_hours[i] - 121)
            elif month_hour[i] == 6:
                day_hour.append(day_jul_hours[i] - 152)
            elif month_hour[i] == 7:
                day_hour.append(day_jul_hours[i] - 182)
            elif month_hour[i] == 8:
                day_hour.append(day_jul_hours[i] - 213)
            elif month_hour[i] == 9:
                day_hour.append(day_jul_hours[i] - 244)
            elif month_hour[i] == 10:
                day_hour.append(day_jul_hours[i] - 274)
            elif month_hour[i] == 11:
                day_hour.append(day_jul_hours[i] - 305)
            elif month_hour[i] == 12:
                day_hour.append(day_jul_hours[i] - 335)
        else:
            if month_hour[i] == 1:
                day_hour.append(day_jul_hours[i])
            elif month_hour[i] == 2:
                day_hour.append(day_jul_hours[i] - 31)
            elif month_hour[i] == 3:
                day_hour.append(day_jul_hours[i] - 59)
            elif month_hour[i] == 4:
                day_hour.append(day_jul_hours[i] - 90)
            elif month_hour[i] == 5:
                day_hour.append(day_jul_hours[i] - 120)
            elif month_hour[i] == 6:
                day_hour.append(day_jul_hours[i] - 151)
            elif month_hour[i] == 7:
                day_hour.append(day_jul_hours[i] - 181)
            elif month_hour[i] == 8:
                day_hour.append(day_jul_hours[i] - 212)
            elif month_hour[i] == 9:
                day_hour.append(day_jul_hours[i] - 243)
            elif month_hour[i] == 10:
                day_hour.append(day_jul_hours[i] - 273)
            elif month_hour[i] == 11:
                day_hour.append(day_jul_hours[i] - 304)
            elif month_hour[i] == 12:
                day_hour.append(day_jul_hours[i] - 334)

    # CALCULO DO LINK TURBIDITY PARA CADA MESES DO ANO EM MINUTO
    link_turbidity_minute = []
    for i in range(day_jul_minutes[-1]*1440):
        if month_minute[i] == 1:
            link_turbidity_minute.append(turbidity[4]/20)
        elif month_minute[i] == 2:
            link_turbidity_minute.append(turbidity[12]/20)
        elif month_minute[i] == 3:
            link_turbidity_minute.append(turbidity[7]/20)
        elif month_minute[i] == 4:
            link_turbidity_minute.append(turbidity[1]/20)
        elif month_minute[i] == 5:
            link_turbidity_minute.append(turbidity[8]/20)
        elif month_minute[i] == 6:
            link_turbidity_minute.append(turbidity[6]/20)
        elif month_minute[i] == 7:
            link_turbidity_minute.append(turbidity[5]/20)
        elif month_minute[i] == 8:
            link_turbidity_minute.append(turbidity[2]/20)
        elif month_minute[i] == 9:
            link_turbidity_minute.append(turbidity[11]/20)
        elif month_minute[i] == 10:
            link_turbidity_minute.append(turbidity[10]/20)
        elif month_minute[i] == 11:
            link_turbidity_minute.append(turbidity[9]/20)
        elif month_minute[i] == 12:
            link_turbidity_minute.append(turbidity[3]/20)

    # LACO PARA SER EFETUADO OS CALCULOS DO CLEAR SKY USANDO O METODO DE DUMORTIER
    clear_sky_minute = []
    clear_sky_hour = []
    TOA = []
    Ees = []
    Eed = []
    IRg = []
    for i in range(day_jul_minutes[-1]*1440):
        # CALCULO DA DECLINACAO SOLAR EM RADS
        day_angle = (0.017201916*day_jul_minutes[i])
        dec = (0.006918 - 0.399912 * np.cos(day_angle) + 0.070257 * np.sin(day_angle) - 0.006758 * np.cos(2* day_angle) + 0.000907 * np.sin(2* day_angle) - 0.002697 * np.cos(3* day_angle) + 0.001480 * np.sin(3* day_angle))
        # CALCULO DA EQUACAO DO TEMPO EM HORA
        eqtime = (0.000075 + 0.001868 * np.cos(day_angle) - 0.032077 * np.sin(day_angle) - 0.014615 * np.cos(2* day_angle) - 0.040849 * np.sin(2* day_angle))*(229.18)
        # CALCULO DO TEMPO TOTAL TRANSCORRIDO OU HORA SOLAR EM MINUTO
        tcorr = (minutes[i]/60 + ((longitude - Ls)/15) + eqtime/60)
        # CALCULO DO ANGULO HORARIO EM GRAU
        hour_angle = (12.00 - tcorr)* 15
        # CALCULO DA DISTÂNCIA MÉDIA TERRA-SOL PARA CADA DIA JULIANO
        e0 = 1.00011 + 0.034221 * np.cos(day_angle) + 0.00128 * np.sin(day_angle) + 0.000719 * np.cos(2 * day_angle) + 0.000077 * np.sin(2 * day_angle)
        # CALCULO DO ÂNGULO ZÊNITAL, COSENO DO ANGULO ZENITAL E DO ANGULO DE ELEVAÇÃO
        u0 = ((np.sin(dec) * np.sin(latitude*np.pi/180)) + (np.cos(dec) * np.cos(latitude*np.pi/180) * np.cos(hour_angle*np.pi/180)))
        zenit_angle = (np.arccos(u0))*180/np.pi
        elevation_angle = (90 - zenit_angle)
        # CALCULO DA RADIAÇÃO SOLAR NO TOPO DA ATMOSFERA EM (W/m2)
        TOA.append(1367 * e0 * u0)
        if TOA[i] < 0:
            TOA[i] = 0
        # CALCULO DA RELATIVE OPTICAL AIR MASS (M)
        delta_elevation_angle = ((0.061359 * (180/np.pi)) * (((0.1594 + ((1.1230) * (np.pi/180) * (elevation_angle))) + (0.065656 * ((np.pi/180)**2) * (elevation_angle**2))) / ((1 + (28.9344 * (np.pi/180) * elevation_angle)) + (277.3971 * ((np.pi/180)**2) * (elevation_angle**2)))))
        true_elevation_angle = elevation_angle + delta_elevation_angle
        M = np.real((np.exp((-altitude)/8434.5))/(np.sin(true_elevation_angle*(np.pi/180))+(0.50572*((6.07995 + true_elevation_angle)**-1.6364))))
        # CALCULO DO Aer: IS THE OPTICAL THICKNESS OF RAYLEIGH
        if M <= 20:
            Aer = ((1)/(6.6296 + 1.7513*(M) - 0.1202*(M**2) + 0.0065*(M**3) - 0.00013*(M**4)))
        elif M > 20:
            Aer = ((1)/(10.4 + (0.718*(M))))
        else:
            Aer = 0
        # CALCULO DA COMPOMENTE DIRETA DA RADIAÇÂO SOLAR
        Ees.append(1367 * e0 * np.sin(elevation_angle*(np.pi/180)) * np.exp(-0.8662 * link_turbidity_minute[i] * M * Aer))
        if Ees[i] < 0:
            Ees[i] = 0
        # CALCULO DA COMPOMENTE DIFUSSA DA RADIAÇÃO SOLAR
        Eed.append(1367 * e0 * (0.0065 + (-0.045 + (0.0646 * link_turbidity_minute[i] * np.sin(elevation_angle*(np.pi/180)) - (-0.014 + (0.0327 * link_turbidity_minute[i] * (np.sin(elevation_angle*(np.pi/180)) * (np.sin(elevation_angle*(np.pi/180))))))))))
        if Eed[i] < 0 or Eed[i] > 1367:
            Eed[i] = 0
        # CALCULO DA RADIAÇÃO SOLAR GLOBAL
        IRg.append(Ees[i] + Eed[i])

        # SALVANDO O CLEAR_SKY PARA CADA MINUTO DO ANO
        data_array = [year_minutes[i], month_minute[i], day_minute[i], day_jul_minutes[i], minutes[i], TOA[i], Ees[i], Eed[i], IRg[i]]
        clear_sky_minute.append(data_array)

    # SALVANDO O CLEAR_SKY PARA CADA HORA DO ANO
    for i in range(len(year_hours)):
        data_array = [year_hours[i], month_hour[i], day_hour[i], day_jul_hours[i], hours[i]]
        clear_sky_hour.append(data_array)

    # CALCULANDO A MÉDIA PARA CADA HORA
    zeit_ref_min = np.arange(1, (day_jul_minutes[-1]*1440)+1)
    starthour = np.arange(60, (day_jul_minutes[-1]*1440)+1, 60)

    for i in range(hour_year):
        #[zl,sl] = np.where(starthour[i] == zeit_ref_min)
        zl = np.where(starthour[i] == zeit_ref_min)
        zl_min = max(1, zl[0][0]-60)
        zl_max = min(zl[0][0], day_jul_minutes[-1]*1440)
        TOA_mean = np.mean(TOA[zl_min:zl_max])
        Ees_mean = np.mean(Ees[zl_min:zl_max])
        Eed_mean = np.mean(Eed[zl_min:zl_max])
        IRg_mean = np.mean(IRg[zl_min:zl_max])
        clear_sky_hour[i].append(TOA_mean)
        clear_sky_hour[i].append(Ees_mean)
        clear_sky_hour[i].append(Eed_mean)
        clear_sky_hour[i].append(IRg_mean)

    return clear_sky_minute, clear_sky_hour
