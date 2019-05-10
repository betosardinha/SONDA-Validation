import os
import numpy as np

from tqdm import *

from Loader import Loader


class ScreeningController:
    def __init__(self, input1=None):
        # Constant values used to get solar geometry data
        self.d0 = 0.006918
        self.dc1 = 0.399912
        self.dc2 = 0.006758
        self.dc3 = 0.002697
        self.ds1 = 0.070257
        self.ds2 = 0.000907
        self.ds3 = 0.001480
        self.et0 = 0.000075
        self.tc1 = 0.001868
        self.tc2 = 0.014615
        self.ts1 = 0.032077
        self.ts2 = 0.040890

        self.e1 = 1.000110
        self.e2 = 0.034221
        self.e3 = 0.001280
        self.e4 = 0.000719
        self.e5 = 0.000077

        # Threshold values used to qualify solar and meteorological data  - level 1
        self.HUMI_MX = 100
        self.HUMI_MI = 0

        self.PRES_MX = None
        self.PRES_MI = None

        self.TEMP_MX = None
        self.TEMP_MI = None

        self.PREC_MX = None
        self.PREC_MI = 0

        self.WS10_MX = 25
        self.WS10_MI = 0

        self.WD10_MX = 360
        self.WD10_MI = 0

        # BSRN criteria for solar data qualification
        self.LWDN_MX = 700
        self.LWDN_MI = 40

        self.GLOBAL_MX = None
        self.GLOBAL_MI = -4

        self.DIFUSE_MX = None
        self.DIFUSE_MI = -4

        self.DIRECT_MX = None
        self.DIRECT_MI = -4

        self.PAR_MX = None
        self.PAR_MI = -4

        self.LUX_MX = None
        self.LUX_MI = -4

        # Variables used to validate meteorological data  - levels 2 and  3
        self.temp_max = 0
        self.temp_min = 999
        self.temp1h = 59
        self.temp12h = 719
        self.variation_temp1h = None
        self.variation_temp12h = None

        self.pres_max = 0
        self.pres_min = 999
        self.pres3h = 179
        self.variation_pres3h = None

        self.prec_max = 0
        self.prec_min = 999
        self.prec1h = 59
        self.prec24h = 1439
        self.variation_prec1h = None
        self.variation_prec24h = None

        self.ws10_max = 0
        self.ws10_min = 999
        self.ws103h = 179
        self.ws1012h = 719
        self.variation_ws103h = None
        self.variation_ws1012h = None

        self.wd10_max = 0
        self.wd10_min = 999
        self.wd103h = 179
        self.wd1018h = 1079
        self.variation_wd103h = None
        self.variation_wd1018h = None

        # Variables used to get solar geometry data
        self.e0 = None
        self.u0 = None              # Cosine of solar zenith angle
        self.zenith_angle = None    # Zenith angle
        self.rtoa = None            # Solar Irradiation at the top of atmosphere
        self.sa = None
        self.day_angle = None       # Diary angle
        self.dec = None             # Declination angle
        self.eqtime = None          # Equation time
        self.tcorr = None           # Time correction
        self.hour_angle = None      # Hour angle

        # Other variables
        self.CDR = np.pi / 180
        self.rows = None        # total file lines
        self.cont = 0           # Count rows number
        self.num = None         # Measurement time in minutes
        self.dia_jul = None     # Day number
        self.horacorr = None    # Time correction considering longitude data for the measurement site
        self.div = None         # Measurement time in decimal hours
        self.i = None
        self.cont_std = 0

        self.pb = None
        self.dialog = None

        # Variables used to count meteorological data valid - level 2 and 3
        self.contTempValid = 0
        self.contPresValid = 0
        self.contPrecValid = 0
        self.contWspdValid = 0
        self.contWdirValid = 0

        # Variables used to save the last valid meteorological data - level 2 and 3
        self.lastTempValid = None
        self.lastPresValid = None
        self.lastPrecValid = None
        self.lastWs10Valid = None
        self.lastWd10Valid = None

        self.kt = None
        self.kn = None

        self.loader = None

        if input1 is not None:
            self.loader = Loader.Loader()
            self.loader.buildsMatrixData(input1)
            self.loader.buildsMatrixCode(input1)

    def progressBar(self):
        self.pb = tqdm(total=self.rows, desc="Validação")

    def validate(self, latitude, longitude, station, month):
        self.rows = self.loader.getRows() - 1
        self.progressBar()

        for i in range(self.rows+1):
            self.num = self.loader.data[i][3]
            self.div = self.num / 60    # Measurement time in utc time
            self.dia_jul = self.loader.data[i][2]

            # Calculating astronomical data
            self.day_angle = (2 * np.pi / 365.25 * self.dia_jul)
            self.dec = (self.d0 - self.dc1 * np.cos(self.day_angle) + self.ds1 * np.sin(self.day_angle) - self.dc2 * np.cos(2 * self.day_angle) + self.ds2 * np.sin(2 * self.day_angle) - self.dc3 * np.cos(3 * self.day_angle) + self.ds3 * np.sin(3 * self.day_angle))
            self.eqtime = (self.et0 + self.tc1 * np.cos(self.day_angle) - self.ts1 * np.sin(self.day_angle) - self.tc2 * np.cos(2 * self.day_angle) - self.ts2 * np.sin(2 * self.day_angle)) * 229.18
            self.tcorr = (self.eqtime + 4 * (longitude - 0)) / 60
            self.horacorr = self.tcorr + self.div   # Local time obtained from utc time
            self.hour_angle = (12.00 - self.horacorr) * 15
            self.e0 = self.e1 + self.e2 * np.cos(self.day_angle) + self.e3 * np.sin(self.day_angle) + self.e4 * np.cos(2 * self.day_angle) + self.e5 * np.sin(2 * self.day_angle)
            self.u0 = np.sin(self.dec) * np.sin(latitude * self.CDR) + np.cos(self.dec) * np.cos(latitude * self.CDR) * np.cos(self.hour_angle * self.CDR)
            self.zenith_angle = np.arccos(self.u0) * 180 / np.pi

            # Start level 1

            # Routine to check the misalignment of the tracker
            if self.zenith_angle < 87:
                if self.loader.data[i][4] != 3333 and self.loader.data[i][4] != -5555 and self.loader.data[i][4] != -6999:
                    if self.loader.data[i][28] != 3333 and self.loader.data[i][28] != -5555 and self.loader.data[i][28] != -6999:
                        if self.loader.data[i][4] > 50:
                            self.rtoa = self.sa * self.u0
                            self.kt = self.loader.data[i][4] / self.rtoa
                            self.kn = self.loader.data[i][28] / self.loader.data[i][4]
                            if self.kt >= 0.50:
                                if self.kn > 0.30:
                                    self.loader.code[i][8] = 9
                                    self.loader.code[i][28] = 9
                                else:
                                    self.loader.code[i][8] = 552
                                    self.loader.code[i][28] = 552
                            elif self.kt >= 0.40 and self.kt < 0.50:
                                if self.kn > 0.10:
                                    self.loader.code[i][8] = 9
                                    self.loader.code[i][28] = 9
                                else:
                                    self.loader.code[i][8] = 552
                                    self.loader.code[i][28] = 552

            # End of routine to check the misalignment of the tracker

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Global Radiation (W/m²) level 1

            if self.loader.data[i][4] != 3333:
                if self.loader.data[i][4] != -5555:
                    if self.loader.data[i][4] != -6999:
                        if self.loader.data[i][5] != 0:
                            if self.u0 > 0:
                                self.GLOBAL_MX = (self.sa * 1.5 * (self.u0**1.2) + 100)
                            else:
                                self.GLOBAL_MX = 100

                            if self.loader.data[i][4] > self.GLOBAL_MI and self.loader.data[i][4] < self.GLOBAL_MX:
                                self.loader.code[i][4] = 9
                            else:
                                self.loader.code[i][4] = 552
                        else:
                            if self.zenith_angle > 90:
                                if self.u0 > 0:
                                    self.GLOBAL_MX = (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                else:
                                    self.GLOBAL_MX = 100

                                if self.loader.data[i][4] > self.GLOBAL_MI and self.loader.data[i][4] < self.GLOBAL_MX:
                                    self.loader.code[i][4] = 9
                                else:
                                    self.loader.code[i][4] = 552
                            else:
                                self.cont_std += 1
                                if self.loader.data[i][4] != self.loader.data[i-1][4] and self.loader.data[i][4] != self.loader.data[i+1][4]:
                                    if self.u0 > 0:
                                        self.GLOBAL_MX = (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                    else:
                                        self.GLOBAL_MX = 100

                                    if self.loader.data[i][4] > self.GLOBAL_MI and self.loader.data[i][
                                        4] < self.GLOBAL_MX:
                                        self.loader.code[i][4] = 9
                                    else:
                                        self.loader.code[i][4] = 552
                                else:
                                    self.loader.code[i][4] = 552
                    else:
                        self.loader.code[i][4] = -6999
                else:
                    self.loader.code[i][4] = -5555
            else:
                self.loader.code[i][4] = 3333

            # End of the routine validation: Global Radiation (W/m²) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Diffuse Radiation (W/m²) level 1

            if self.loader.data[i][8] != 333:
                if self.loader.data[i][8] != -5555:
                    if self.loader.data[i][8] != -6999:
                        if self.loader.data[i][8] != 552:
                            if self.loader.data[i][9] != 0:
                                if self.u0 > 0:
                                    self.DIFUSE_MX = (self.sa * 0.95 * (self.u0 **1.2) + 50)
                                else:
                                    self.DIFUSE_MX = 50

                                if self.loader.data[i][8] > self.DIFUSE_MI and self.loader.data[i][8] < self.DIFUSE_MX:
                                    self.loader.code[i][8] = 9
                                else:
                                    self.loader.code[i][8] = 552
                            else:
                                if self.zenith_angle > 90:
                                    if self.u0 > 0:
                                        self.DIFUSE_MX = (self.sa * 0.95 * (self.u0 ** 1.2) + 50)
                                    else:
                                        self.DIFUSE_MX = 50

                                    if self.loader.data[i][8] > self.DIFUSE_MI and self.loader.data[i][
                                        8] < self.DIFUSE_MX:
                                        self.loader.code[i][8] = 9
                                    else:
                                        self.loader.code[i][8] = 552
                                else:
                                    self.cont_std += 1
                                    if self.loader.data[i][8] != self.loader.data[i-1][8] and  self.loader.data[i][8] != self.loader.data[i+1][8]:
                                        if self.u0 > 0:
                                            self.DIFUSE_MX = (self.sa * 0.95 * (self.u0 ** 1.2) + 50)
                                        else:
                                            self.DIFUSE_MX = 50

                                        if self.loader.data[i][8] > self.DIFUSE_MI and self.loader.data[i][
                                            8] < self.DIFUSE_MX:
                                            self.loader.code[i][8] = 9
                                        else:
                                            self.loader.code[i][8] = 552
                                    else:
                                        self.loader.code[i][8] = 552
                    else:
                        self.loader.code[i][8] = -6999
                else:
                    self.loader.code[i][8] = -5555
            else:
                self.loader.code[i][8] = 3333

            # End of the routine validation: Diffuse Radiation (W/m²) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Par Radiation (�mols s� m�) level 1

            if self.loader.data[i][12] != 3333:
                if self.loader.data[i][12] != -5555:
                    if self.loader.data[i][12] != -6999:
                        if self.loader.data[i][13] != 0:
                            if self.u0 > 0:
                                self.PAR_MX = 2.07 * (self.sa * 1.5 * (self.u0**1.2) + 100)
                            else:
                                self.PAR_MX = 2.07 * 100

                            if self.loader.data[i][12] > self.PAR_MI and self.loader.data[i][12] < self.PAR_MX:
                                self.loader.code[i][12] = 9
                            else:
                                self.loader.code[i][12] = 552
                        else:
                            if self.zenith_angle > 90:
                                if self.u0 > 0:
                                    self.PAR_MX = 2.07 * (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                else:
                                    self.PAR_MX = 2.07 * 100

                                if self.loader.data[i][12] > self.PAR_MI and self.loader.data[i][12] < self.PAR_MX:
                                    self.loader.code[i][12] = 9
                                else:
                                    self.loader.code[i][12] = 552
                            else:
                                self.cont_std += 1
                                if self.loader.data[i][12] != self.loader.data[i-1][12] and self.loader.data[i][12] != self.loader.data[i+1][12]:
                                    if self.u0 > 0:
                                        self.PAR_MX = 2.07 * (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                    else:
                                        self.PAR_MX = 2.07 * 100

                                    if self.loader.data[i][12] > self.PAR_MI and self.loader.data[i][12] < self.PAR_MX:
                                        self.loader.code[i][12] = 9
                                    else:
                                        self.loader.code[i][12] = 552
                                else:
                                    self.loader.code[i][12] = 552
                    else:
                        self.loader.code[i][12] = -6999
                else:
                    self.loader.code[i][12] = -5555
            else:
                self.loader.code[i][12] = 3333


            # End of the routine validation: Par Radiation (�mols s� m�) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Lux Radiation (kLux) level 1

            if self.loader.data[i][16] != 3333:
                if self.loader.data[i][16] != -5555:
                    if self.loader.data[i][16] != -6999:
                        if self.loader.data[i][17] != 0:
                            if self.u0 > 0:
                                self.LUX_MX = 0.115 * (self.sa * 1.5 * (self.u0**1.2) + 100)
                            else:
                                self.LUX_MX = 0.115 * 100

                            if self.loader.data[i][16] > self.LUX_MI and self.loader.data[i][16] < self.LUX_MX:
                                self.loader.code[i][16] = 9
                            else:
                                self.loader.code[i][16] = 552
                        else:
                            if self.zenith_angle > 90:
                                if self.u0 > 0:
                                    self.LUX_MX = 0.115 * (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                else:
                                    self.LUX_MX = 0.115 * 100

                                if self.loader.data[i][16] > self.LUX_MI and self.loader.data[i][16] < self.LUX_MX:
                                    self.loader.code[i][16] = 9
                                else:
                                    self.loader.code[i][16] = 552
                            else:
                                self.cont_std += 1
                                if self.loader.data[i][16] != self.loader.data[i-1][16] and self.loader.data[i][16] != self.loader.data[i+1][16]:
                                    if self.u0 > 0:
                                        self.LUX_MX = 0.115 * (self.sa * 1.5 * (self.u0 ** 1.2) + 100)
                                    else:
                                        self.LUX_MX = 0.115 * 100

                                    if self.loader.data[i][16] > self.LUX_MI and self.loader.data[i][16] < self.LUX_MX:
                                        self.loader.code[i][16] = 9
                                    else:
                                        self.loader.code[i][16] = 552
                                else:
                                    self.loader.code[i][16] = 552
                    else:
                        self.loader.code[i][16] = -6999
                else:
                    self.loader.code[i][16] = -5555
            else:
                self.loader.code = 3333

            # End of the routine validation: Lux Radiation (kLux) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Air Temperature (°C) level 1

            if self.loader.data[i][20] != 3333:
                if self.loader.data[i][20] != -5555:
                    self.TEMP_MX = self.loader.getTempMax("." + os.path.sep + "limits" + os.path.sep + "temp.max", station, month)
                    self.TEMP_MI = self.loader.getTempMax("." + os.path.sep + "limits" + os.path.sep + "temp.min", station, month)
                    if self.loader.data[i][20] > self.TEMP_MI and self.loader.data[i][20] < self.TEMP_MX:
                        self.loader.code[i][20] = 9
                    else:
                        self.loader.code[i][20] = 552
                else:
                    self.loader.code[i][20] = -5555
            else:
                self.loader.code[i][20] = 3333

            # End of the routine validation: Air Temperature (°C) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Relative Air Humidity (%) level 1

            if self.loader.data[i][21] != 3333:
                if self.loader.data[i][21] != -5555:
                    if self.loader.data[i][21] > self.HUMI_MI and self.loader.data[i][21] <= self.HUMI_MX:
                        self.loader.code[i][21] = 9
                    else:
                        self.loader.code[i][21] = 552
                else:
                    self.loader.code[i][21] = -5555
            else:
                self.loader.code[i][21] = 3333

            # End of the routine validation: Relative Air Humidity (%) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Atmospheric Pressure (mbar) level 1

            if self.loader.data[i][22] != 3333:
                if self.loader.data[i][22] != -5555:
                    self.PRES_MX = self.loader.getPresMax("." + os.path.sep + "limits" + os.path.sep + "pres.max", station)
                    self.PRES_MI = self.loader.getPresMin("." + os.path.sep + "limits" + os.path.sep + "pres.min", station)
                    if self.loader.data[i][22] > self.PRES_MI and self.loader.data[i][22] < self.PRES_MX:
                        self.loader.code[i][22] = 9
                    else:
                        self.loader.code[i][22] = 552
                else:
                    self.loader.code[i][22] = -5555
            else:
                self.loader.code[i][22] = 3333

            # End of the routine validation: Atmospheric Pressure (mbar) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Accumulated Precipitation (mm) level 1

            if self.loader.data[i][23] != 3333:
                if self.loader.data[i][23] != -5555:
                    self.PREC_MX = self.loader.getPrecMax("." + os.path.sep + "limits" + os.path.sep + "prec.max", station, month)
                    if self.loader.data[i][23] >= self.PREC_MI and self.loader.data[i][23] < self.PREC_MX:
                        self.loader.code[i][23] = 9
                    else:
                        self.loader.code[i][23] = 552
                else:
                    self.loader.code[i][23] = -5555
            else:
                self.loader.code[i][23] = 3333

            # End of the routine validation: Accumulated Precipitation (mm) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Wind Speed 10m (m/s) level 1

            if self.loader.data[i][24] != 3333:
                if self.loader.data[i][24] != -5555:
                    if self.loader.data[i][24] > self.WS10_MI and self.loader.data[i][24] < self.WS10_MX:
                        self.loader.code[i][24] = 9
                    else:
                        self.loader.code[i][24] = 552
                else:
                    self.loader.code[i][24] = -5555
            else:
                self.loader.code[i][24] = 3333

            # End of the routine validation: Wind Speed 10m (m/s) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Wind Direction 10m (°) level 1

            if self.loader.data[i][25] != 3333:
                if self.loader.data[i][25] != -5555:
                    if self.loader.data[i][26] != 0:
                        if self.loader.data[i][25] > self.WD10_MI and self.loader.data[i][25] < self.WD10_MX:
                            self.loader.code[i][25] = 9
                        else:
                            self.loader.code[i][25] = 552
                    else:
                        self.loader.code[i][25] = 552
                else:
                    self.loader.code[i][25] = -5555
            else:
                self.loader.code[i][25] = 3333

            # End of the routine validation: Wind Direction 10m (°) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Direct Radiation (W/m²) level 1

            if self.loader.data[i][28] != 3333:
                if self.loader.data[i][28] != -5555:
                    if self.loader.data[i][28] != -6999:
                        if self.loader.code[i][28] != 552:
                            if self.loader.data[i][29] != 0:
                                if self.u0 > 0:
                                    self.DIRECT_MX = self.sa
                                else:
                                    self.DIRECT_MX = 50

                                if self.loader.data[i][28] > self.DIFUSE_MI and self.loader.data[i][28] < self.DIRECT_MX:
                                    self.loader.code[i][28] = 9
                                else:
                                    self.loader.code[i][28] = 552
                            else:
                                if self.zenith_angle > 90:
                                    if self.u0 > 0:
                                        self.DIRECT_MX = self.sa
                                    else:
                                        self.DIRECT_MX = 50

                                    if self.loader.data[i][28] > self.DIFUSE_MI and self.loader.data[i][28] < self.DIRECT_MX:
                                        self.loader.code[i][28] = 9
                                    else:
                                        self.loader.code[i][28] = 552
                                else:
                                    self.cont_std+=1

                                    if self.loader.data[i][28] != self.loader.data[i-1][28] and self.loader.data[i][28] != self.loader.data[i+1][28]:
                                        if self.u0 > 0:
                                            self.DIRECT_MX = self.sa
                                        else:
                                            self.DIRECT_MX = 50

                                        if self.loader.data[i][28] > self.DIRECT_MI and self.loader.data[i][28] < self.DIRECT_MX:
                                            self.loader.code[i][28] = 9
                                        else:
                                            self.loader.code[i][28] = 552
                                    else:
                                        self.loader.code[i][28] = 552
                    else:
                        self.loader.code[i][28] = -6999
                else:
                    self.loader.code[i][28] = -5555
            else:
                self.loader.code[i][28] = 3333

            # End of the routine validation: Direct Radiation (W/m²) level 1

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Long Wave Radiation (W/m²) level 1

            if self.loader.data[i][32] != 3333:
                if self.loader.data[i][32] != -5555:
                    if self.loader.data[i][32] != -6999:
                        if self.loader.data[i][33] != 0:
                            if self.loader.data[i][32] > self.LWDN_MI and self.loader.data[i][32] < self.LUX_MX:
                                self.loader.code[i][32] = 9
                            else:
                                self.loader.code[i][32] = 552
                        else:
                            if self.zenith_angle > 90:
                                if self.loader.data[i][32] > self.LWDN_MI and self.loader.data[i][32] < self.LWDN_MX:
                                    self.loader.code[i][32] = 9
                                else:
                                    self.loader.code[i][32] = 552
                            else:
                                self.cont_std+=1

                                if self.loader.data[i][32] != self.loader.data[i-1][32] and self.loader.data[i][32] != self.loader.data[i+1][32]:
                                    if self.loader.data[i][32] > self.LWDN_MI and self.loader.data[i][32] < self.LWDN_MX:
                                        self.loader.code[i][32] = 9
                                    else:
                                        self.loader.code[i][32] = 552
                                else:
                                    self.loader.code[i][32] = 552
                    else:
                        self.loader.code[i][32] = -6999
                else:
                    self.loader.code[i][32] = -5555
            else:
                self.loader.code[i][32] = 3333

            # End of the routine validation: Long Wave Radiation (W/m²) level 1

            # ----------------------------------------------------------------------------------------------------------------------

    	    # End of loop level 1

        # Start level 2

        for i in range(self.rows + 1):
            self.num = self.loader.data[i][3]
            self.div = self.num / 60
            self.dia_jul = int(self.loader.data[i][2])

            # Calculating astronomical data
            self.day_angle = (2 * np.pi / 365.25 * self.dia_jul)
            self.dec = (self.d0 - self.dc1 * np.cos(self.day_angle) + self.ds1 * np.sin(self.day_angle) - self.dc2 * np.cos(2*self.day_angle) + self.ds2 * np.sin(2*self.day_angle) - self.dc3 * np.cos(3*self.day_angle) + self.ds3 * np.sin(3*self.day_angle))
            self.eqtime = (self.et0 + self.tc1 * np.cos(self.day_angle) - self.ts1 *np.sin(self.day_angle) - self.tc2 * np.cos(2*self.day_angle) - self.ts2 * np.sin(2*self.day_angle)) * 229.18
            self.tcorr = (self.eqtime + 4 * (longitude - 0)) / 60
            self.horacorr = self.tcorr + self.div
            self.hour_angle = (12.00 - self.horacorr) * 15
            self.e0 = self.e1 + self.e2 * np.cos(self.day_angle) + self.e3 * np.sin(self.day_angle) + self.e4 * np.cos(2*self.day_angle) + self.e5 * np.sin(2*self.day_angle)
            self.u0 = np.sin(self.dec) * np.sin(latitude * self.CDR) + np.cos(self.dec) * np.cos(latitude * self.CDR) * np.cos(self.hour_angle * self.CDR)
            self.zenith_angle = (np.arccos(self.u0)) * 180 / np.pi
            self.sa = 1368 * self.e0

            # BSRN criteria used to qualify solar data as RARE events
            self.GLOBAL_MI = -2
            self.DIFUSE_MI = -2
            self.DIRECT_MI = -2
            self.PAR_MI = -2
            self.LUX_MI = -2
            self.LWDN_MX = 500
            self.LWDN_MI = 60

            # Variables used to validate meteorological data - level 2
            totalTemp1h_1 = self.rows - self.temp1h
            totalTemp1h_2 = self.rows - self.temp1h + 1

            totalPres3h_1 = self.rows - self.pres3h
            totalPres3h_2 = self.rows - self.pres3h + 1

            totalPrec1h_1 = self.rows - self.prec1h
            totalPrec1h_2 = self.rows - self.prec1h + 1

            totalWs103h_1 = self.rows - self.ws103h
            totalWs103h_2 = self.rows - self.ws103h

            totalWd103h_1 = self.rows - self.wd103h
            totalWd103h_2 = self.rows - self.wd103h + 1

            # Start of the routine validation: Global Radiation (W/m²) level 2

            if self.loader.code[i][4] != 3333 and self.loader.code[i][4] != -5555 and self.loader.code[i][4] != -6999 and self.loader.code[i][4] != 552:
                if self.u0 > 0:
                    self.GLOBAL_MX = (self.sa * 1.2 * (self.u0**1.2) + 50)
                else:
                    self.GLOBAL_MX = 50

                if self.loader.data[i][4] > self.GLOBAL_MI and self.loader.data[i][4] < self.GLOBAL_MX:
                    self.loader.code[i][4] = 99
                else:
                    self.loader.code[i][4] = 29

            # End of the routine validation: Global Radiation (W/m²) level 2

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Diffuse Radiation (W/m²) level 2

            if self.loader.code[i][8] != 3333 and self.loader.code[i][8] != -5555 and self.loader.code[i][8] != -6999 and self.loader.code[i][8] != 552:
                if self.u0 > 0:
                    self.DIFUSE_MX = (self.sa * 0.75 * (self.u0**1.2) + 30)
                else:
                    self.DIFUSE_MX = 30

                if self.loader.data[i][8] > self.DIFUSE_MI and self.loader.data[i][8] < self.DIFUSE_MX:
                    self.loader.code[i][8] = 99
                else:
                    self.loader.code[i][8] = 29

            # End of the routine validation: Diffuse Radiation (W/m²) level 2

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Par Radiation (�mols s� m�) level 2

            if self.loader.code[i][12] != 3333 and self.loader.code[i][12] != -5555 and self.loader.code[i][12] != -6999 and self.loader.code[i][12] != 552:
                if self.u0 > 0:
                    self.PAR_MX = 2.07 * (self.sa * 1.2 * (self.u0**1.2) + 50)
                else:
                    self.PAR_MX = 2.07 * 50

                if self.loader.data[i][12] > self.PAR_MI and self.loader.data[i][12] < self.PAR_MX:
                    self.loader.code[i][12] = 99
                else:
                    self.loader.code[i][12] = 29

            # End of the routine validation: Par Radiation (�mols s� m�) level 2

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Lux Radiation (kLux) level 2

            if self.loader.code[i][16] != 3333 and self.loader.code[i][16] != -5555 and self.loader.code[i][16] != -6999 and self.loader.code[i][16] != 552:
                if self.u0 > 0:
                    self.LUX_MX = 0.115 * (self.sa * 1.2 * (self.u0**1.2) + 50)
                else:
                    self.LUX_MX = 0.115 * 50

                if self.loader.data[i][16] > self.LUX_MI and self.loader.data[i][16] < self.LUX_MX:
                    self.loader.code[i][16] = 99
                else:
                    self.loader.code[i][16] = 29

            # End of the routine validation: Lux Radiation (kLux) level 2

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Air Temperature (°C) level 2

            if self.loader.code != 3333 and self.loader.code[i][20] != -5555 and self.loader.code[i][20] != 552:
                if i <= totalTemp1h_1:
                    j = 0
                    while j <= self.temp1h:
                        if self.loader.code[i+j][20] != 3333 and self.loader.code[i+j][20] != 552:
                            self.contTempValid += 1

                            if self.loader.data[i+j][20] > self.temp_max:
                                self.temp_max = self.loader.data[i+j][20]

                            if self.loader.data[i+j][20] < self.temp_min:
                                self.temp_min = self.loader.data[i+j][20]

                            self.variation_temp1h = self.temp_max - self.temp_min
                        j += 1

                    if self.contTempValid >= 40:
                        if self.variation_temp1h < 5:
                            self.loader.code[i][20] = 99
                            self.lastTempValid = self.loader.code[i][20]
                        else:
                            self.loader.code[i][20] = 529
                    else:
                        l = 0
                        while l <= self.temp1h:
                            if self.loader.code[i+l][20] != 3333 and self.loader.code[i+l][20] != 552:
                                if i == 0:
                                    self.loader.code[i][20] = 559
                                else:
                                    self.loader.code[i][20] = self.lastTempValid
                            l += 1

                    self.contTempValid = 0
                    self.temp_max = 0
                    self.temp_min = 999

                if i >= totalTemp1h_2:
                    self.loader.code[i][20] = self.loader.code[totalTemp1h_1][20]

            # End of the routine validation: Air Temperature (°C) level 2

            # ----------------------------------------------------------------------------------------------------------------------

            # Start of the routine validation: Atmospheric Pressure (mbar) level 2

            if self.loader.code[i][22] != 3333 and self.loader.code[i][22] != -5555 and self.loader.code[i][22] != 552:
                if i <= totalPres3h_1:
                    j = 0
                    while j <= self.pres3h:
                        if self.loader.code[i+j][22] != 3333 and self.loader.code[i+j][22] != 552:
                            self.contPresValid += 1

                            if self.loader.data[i+j][22] > self.pres_max:
                                self.pres_max = self.loader.data[i+j][22]

                            if self.loader.data[i+j][22] < self.pres_min:
                                self.pres_min = self.loader.data[i+j][22]

                            self.variation_pres3h = self.pres_max - self.pres_min
                        j += 1

                    if self.contPresValid >= 40:
                        if self.variation_pres3h < 6:
                            self.loader.code[i][22] = 99
                            self.lastPresValid = self.loader.code[i][22]
                        else:
                            self.loader.code[i][22] = 529
                    else:
                        l = 0
                        while l <= self.pres3h:
                            if self.loader.code[i+l][22] != 3333 and self.loader[i+l][22] != 552:
                                if i == 0:
                                    self.loader.code[i][22] = 59
                                else:
                                    self.loader.code[i][22] = self.lastPresValid
                            l += 1

                    self.contPresValid = 0
                    self.pres_max = 0
                    self.pres_min = 999

                if i >= totalPres3h_2:
                    self.loader.code[i][22] = self.loader.code[totalPres3h_1][22]





