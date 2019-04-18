import numpy as np


class Loader:

    # Init function, setting parameters to the respective attributes (None if not passed)
    def __init__(self, rawData=None, numberOfColumns=None, numberOfRows=None):
        self.rawData = np.array(rawData)
        self.numberOfColumns = numberOfColumns
        self.numberOfRows = numberOfRows
        self.temp = np.array([])
        self.data = np.array([])
        self.limits = np.array([])
        self.code = np.array([])

        self.line = None

        # Object basic variables and constants
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

        self.u0 = None
        self.zenith_angle = None
        self.day_angle = None
        self.dec = None
        self.eqtime = None
        self.tcorr = None
        self.hour_angle = None

        self.CDR = np.pi / 180
        self.num = None
        self.dia_jul = None
        self.horacorr = None
        self.div = None

        self.cont_gl1n = 0
        self.cont_gl2n = 0
        self.cont_gl3n = 0
        self.cont_glna = 0
        self.cont_glv = 0

        self.cont_di1n = 0
        self.cont_di2n = 0
        self.cont_di3n = 0
        self.cont_dina = 0
        self.cont_div = 0

        self.cont_df1n = 0
        self.cont_df2n = 0
        self.cont_df3n = 0
        self.cont_dfna = 0
        self.cont_dfv = 0

        self.cont_lw1n = 0
        self.cont_lw2n = 0
        self.cont_lw3n = 0
        self.cont_lwna = 0
        self.cont_lwv = 0

        self.cont_pa1n = 0
        self.cont_pa2n = 0
        self.cont_pa3n = 0
        self.cont_pana = 0
        self.cont_pav = 0

        self.cont_lx1n = 0
        self.cont_lx2n = 0
        self.cont_lx3n = 0
        self.cont_lxna = 0
        self.cont_lxv = 0

        self.cont_tp1n = 0
        self.cont_tp2n = 0
        self.cont_tp3n = 0
        self.cont_tpna = 0
        self.cont_tpv = 0

        self.cont_hu1n = 0
        self.cont_huna = 0
        self.cont_huv = 0

        self.cont_ps1n = 0
        self.cont_ps2n = 0
        self.cont_psna = 0
        self.cont_psv = 0

        self.cont_pc1n = 0
        self.cont_pc2n = 0
        self.cont_pc3n = 0
        self.cont_pcna = 0
        self.cont_pcv = 0

        self.cont_ws1n = 0
        self.cont_ws2n = 0
        self.cont_ws3n = 0
        self.cont_wsna = 0
        self.cont_wsv = 0

        self.cont_wd1n = 0
        self.cont_wd2n = 0
        self.cont_wd3n = 0
        self.cont_wdna = 0
        self.cont_wdv = 0

        self.cont_vgl = 0
        self.cont_nagl = 0
        self.cont_vdi = 0
        self.cont_nadi = 0
        self.cont_vdf = 0
        self.cont_nadf = 0
        self.cont_vlw = 0
        self.cont_nalw = 0
        self.cont_vpa = 0
        self.cont_napa = 0
        self.cont_vlx = 0
        self.cont_nalx = 0

        self.flag_gl = 0
        self.flag_di = 0
        self.flag_df = 0
        self.flag_lw = 0
        self.flag_pa = 0
        self.flag_lx = 0
        self.flag_tp = 0
        self.flag_hu = 0
        self.flag_ps = 0
        self.flag_pc = 0
        self.flag_ws = 0
        self.flag_wd = 0

        self.med_gl1n = None
        self.med_gl2n = None
        self.med_gl3n = None
        self.med_glna = None
        self.med_glv = None

        self.med_di1n = None
        self.med_di2n = None
        self.med_di3n = None
        self.med_dina = None
        self.med_div = None

        self.med_df1n = None
        self.med_df2n = None
        self.med_df3n = None
        self.med_dfna = None
        self.med_dfv = None

        self.med_lw1n = None
        self.med_lw2n = None
        self.med_lw3n = None
        self.med_lwna = None
        self.med_lwv = None

        self.med_pa1n = None
        self.med_pa2n = None
        self.med_pa3n = None
        self.med_pana = None
        self.med_pav = None

        self.med_lx1n = None
        self.med_lx2n = None
        self.med_lx3n = None
        self.med_lxna = None
        self.med_lxv = None

        self.med_tp1n = None
        self.med_tp2n = None
        self.med_tp3n = None
        self.med_tpna = None
        self.med_tpv = None

        self.med_hu1n = None
        self.med_huna = None
        self.med_huv = None

        self.med_ps1n = None
        self.med_ps2n = None
        self.med_psna = None
        self.med_psv = None

        self.med_pc1n = None
        self.med_pc2n = None
        self.med_pc3n = None
        self.med_pcna = None
        self.med_pcv = None

        self.med_ws1n = None
        self.med_ws2n = None
        self.med_ws3n = None
        self.med_wsna = None
        self.med_wsv = None

        self.med_wd1n = None
        self.med_wd2n = None
        self.med_wd3n = None
        self.med_wdna = None
        self.med_wdv = None

    def extractLines(self, input, output, id):
        try:
            bfIn = open(input, 'r')
            try:
                bfOut = open(output, 'w')
                for line in bfIn:
                    if line[0:3] != id:
                        bfOut.write(line)
                        bfOut.write('\n')
                bfOut.close()
            except IOError:
                raise IOError
            finally:
                bfIn.close()
        except IOError:
            raise IOError

    def read(self, input):
        try:
            bfIn = open(input, 'r')
            for line in bfIn:
                token = line.split(',')
                if self.numberOfColumns is None or self.numberOfColumns == 0:
                    self.numberOfColumns = len(token)
                lines = np.array(token, dtype=float)
                np.append(self.rawData, lines, axis=self.rawData.shape[1])
            self.numberOfRows = self.rawData.shape[1]

            bfIn.close()
        except IOError:
            raise IOError("Erro durante a leitura do arquivo: ", input)
        except ValueError:
            raise ValueError("Arquivo com problema de formatação: ", input)

    def writeData(self, output, dataArray, id):
        try:
            bfOut = open(output, 'w')
            for data in dataArray:
                # Header
                bfOut.write(f"{id};")
                bfOut.write(f"{data[1]:.0f};")
                bfOut.write(f"{data[2]:.0f};")
                bfOut.write(f"{data[3]:.0f};")

                # Print Global Radiation AVG 60s
                if data[4] == 3333 or data[4] == -6999:
                    bfOut.write("N/A;")
                elif data[4] == -5555:
                    bfOut.write("N/S;")
                elif data[4] == 0:
                    bfOut.write(f"{data[4]:.0f};")
                else:
                    bfOut.write(f"{data[4]:5.3f};")

                # Print Direct Radiation AVG 60s
                if data[28] == 3333 or data[28] == -6999:
                    bfOut.write("N/A;")
                elif data[28] == -5555:
                    bfOut.write("N/S;")
                elif data[28] == 0:
                    bfOut.write(f"{data[28]:.0f};")
                else:
                    bfOut.write(f"{data[28]:5.3f};")

                # Print Diffuse Radiation AVG 60s
                if data[8] == 3333 or data[8] == -6999:
                    bfOut.write("N/A;")
                elif data[8] == -5555:
                    bfOut.write("N/S;")
                elif data[8] == 0:
                    bfOut.write(f"{data[8]:.0f};")
                else:
                    bfOut.write(f"{data[8]:5.3f};")

                # Print LongWave Radiation AVG 60s
                if data[32] == 3333 or data[32] == -6999:
                    bfOut.write("N/A;")
                elif data[32] == -5555:
                    bfOut.write("N/S;")
                elif data[32] == 0:
                    bfOut.write(f"{data[32]:.0f};")
                else:
                    bfOut.write(f"{data[32]:.1f};")

                # Print Par Radiation AVG 60s
                if data[12] == 3333 or data[12] == -6999:
                    bfOut.write("N/A;")
                elif data[12] == -5555:
                    bfOut.write("N/S;")
                elif data[12] == 0:
                    bfOut.write(f"{data[12]:.0f};")
                else:
                    bfOut.write(f"{data[12]:5.3f};")

                # Print Lux Radiation AVG 60s
                if data[16] == 3333 or data[16] == -6999:
                    bfOut.write("N/A;")
                elif data[16] == -5555:
                    bfOut.write("N/S;")
                elif data[16] == 0:
                    bfOut.write(f"{data[16]:.0f};")
                else:
                    bfOut.write(f"{data[16]:5.3f};")

                # Print Air Temperature AVG 60s
                if data[20] == 3333 or data[20] == -6999:
                    bfOut.write("N/A;")
                elif data[20] == -5555:
                    bfOut.write("N/S;")
                elif data[20] == 0:
                    bfOut.write(f"{data[20]:.0f};")
                else:
                    bfOut.write(f"{data[20]:5.2f};")

                # Print Relative Humidity AVG 60s
                if data[21] == 3333 or data[21] == -6999:
                    bfOut.write("N/A;")
                elif data[21] == -5555:
                    bfOut.write("N/S;")
                elif data[21] == 0:
                    bfOut.write(f"{data[21]:.0f};")
                else:
                    bfOut.write(f"{data[21]:5.2f};")

                # Print Atmospheric Pressure AVG 60s
                if data[22] == 3333 or data[22] == -6999:
                    bfOut.write("N/A;")
                elif data[22] == -5555:
                    bfOut.write("N/S;")
                elif data[22] == 0:
                    bfOut.write(f"{data[22]:.0f};")
                else:
                    bfOut.write(f"{data[22]:5.2f};")

                # Print Accumulated Precipitation AVG 60s
                if data[23] == 3333 or data[23] == -6999:
                    bfOut.write("N/A;")
                elif data[23] == -5555:
                    bfOut.write("N/S;")
                elif data[23] == 0:
                    bfOut.write(f"{data[23]:.0f};")
                else:
                    bfOut.write(f"{data[23]:.1f};")

                # Print Wind Speed AVG 60s
                if data[24] == 3333 or data[24] == -6999:
                    bfOut.write("N/A;")
                elif data[24] == -5555:
                    bfOut.write("N/S;")
                elif data[24] == 0:
                    bfOut.write(f"{data[24]:.0f};")
                else:
                    bfOut.write(f"{data[24]:5.3f};")

                # Print Wind Direction AVG 60s
                if data[25] == 3333 or data[25] == -6999:
                    bfOut.write("N/A;")
                elif data[25] == -5555:
                    bfOut.write("N/S;")
                elif data[25] == 0:
                    bfOut.write(f"{data[25]:.0f};")
                else:
                    bfOut.write(f"{data[25]:.1f};")

            bfOut.close()
        except IOError:
            raise IOError("Erro durante a escrita do arquivo: ", output)

    def writeCode(self, output, dataArray, codeArray, id):
        try:
            bfOut = open(output, 'w')
            for i in range(len(dataArray)):
                # Header
                bfOut.write(f"{id};")
                bfOut.write(f"{dataArray[i][1]:.0f};")
                bfOut.write(f"{dataArray[i][2]:.0f};")
                bfOut.write(f"{dataArray[i][3]:.0f};")

                # Global Radiation
                if codeArray[i][4] == 9999:
                    bfOut.write(f"{codeArray[i][4]}")
                elif codeArray[i][4] == 599:
                    bfOut.write(f"{codeArray[i][4]}")
                elif codeArray[i][4] == 529:
                    bfOut.write(f"{codeArray[i][4]}")
                elif codeArray[i][4] == 299:
                    bfOut.write(f"{codeArray[i][4]}")
                elif codeArray[i][4] == 552:
                    bfOut.write(f"{codeArray[i][4]}")
                elif codeArray[i][4] == 3333 or codeArray[i][4] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][4] == -5555:
                    bfOut.write("N/S")

                # Direct Radiation
                if codeArray[i][28] == 9999:
                    bfOut.write(f"{codeArray[i][28]}")
                elif codeArray[i][28] == 599:
                    bfOut.write(f"{codeArray[i][28]}")
                elif codeArray[i][28] == 529:
                    bfOut.write(f"{codeArray[i][28]}")
                elif codeArray[i][28] == 299:
                    bfOut.write(f"{codeArray[i][28]}")
                elif codeArray[i][28] == 552:
                    bfOut.write(f"{codeArray[i][28]}")
                elif codeArray[i][28] == 3333 or codeArray[i][28] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][28] == -5555:
                    bfOut.write("N/S")

                # Diffuse Radiation
                if codeArray[i][8] == 9999:
                    bfOut.write(f"{codeArray[i][8]}")
                elif codeArray[i][8] == 599:
                    bfOut.write(f"{codeArray[i][8]}")
                elif codeArray[i][8] == 529:
                    bfOut.write(f"{codeArray[i][8]}")
                elif codeArray[i][8] == 299:
                    bfOut.write(f"{codeArray[i][8]}")
                elif codeArray[i][8] == 552:
                    bfOut.write(f"{codeArray[i][8]}")
                elif codeArray[i][8] == 3333 or codeArray[i][8] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][8] == -5555:
                    bfOut.write("N/S")

                # Long-Wave
                if codeArray[i][32] == 9999:
                    bfOut.write(f"{codeArray[i][32]}")
                elif codeArray[i][32] == 599:
                    bfOut.write(f"{codeArray[i][32]}")
                elif codeArray[i][32] == 529:
                    bfOut.write(f"{codeArray[i][32]}")
                elif codeArray[i][32] == 299:
                    bfOut.write(f"{codeArray[i][32]}")
                elif codeArray[i][32] == 552:
                    bfOut.write(f"{codeArray[i][32]}")
                elif codeArray[i][32] == 3333 or codeArray[i][32] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][32] == -5555:
                    bfOut.write("N/S")

                # Par
                if codeArray[i][12] == 9999:
                    bfOut.write(f"{codeArray[i][12]}")
                elif codeArray[i][12] == 599:
                    bfOut.write(f"{codeArray[i][12]}")
                elif codeArray[i][12] == 529:
                    bfOut.write(f"{codeArray[i][12]}")
                elif codeArray[i][12] == 299:
                    bfOut.write(f"{codeArray[i][12]}")
                elif codeArray[i][12] == 552:
                    bfOut.write(f"{codeArray[i][12]}")
                elif codeArray[i][12] == 3333 or codeArray[i][12] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][12] == -5555:
                    bfOut.write("N/S")

                # Lux
                if codeArray[i][16] == 9999:
                    bfOut.write(f"{codeArray[i][16]}")
                elif codeArray[i][16] == 599:
                    bfOut.write(f"{codeArray[i][16]}")
                elif codeArray[i][16] == 529:
                    bfOut.write(f"{codeArray[i][16]}")
                elif codeArray[i][16] == 299:
                    bfOut.write(f"{codeArray[i][16]}")
                elif codeArray[i][16] == 552:
                    bfOut.write(f"{codeArray[i][16]}")
                elif codeArray[i][16] == 3333 or codeArray[i][16] == -6999:
                    bfOut.write("N/A")
                elif codeArray[i][16] == -5555:
                    bfOut.write("N/S")

                # Temperature
                if codeArray[i][20] == 9999:
                    bfOut.write(f"{codeArray[i][20]}")
                elif codeArray[i][20] == 559:
                    bfOut.write(f"{codeArray[i][20]}")
                elif codeArray[i][20] == 299:
                    bfOut.write(f"{codeArray[i][20]}")
                elif codeArray[i][20] == 552:
                    bfOut.write(f"{codeArray[i][20]}")
                elif codeArray[i][20] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][20] == -5555:
                    bfOut.write("N/S")

                # Humidity
                if codeArray[i][21] == 9:
                    bfOut.write(f"00{codeArray[i][21]}")
                elif codeArray[i][21] == 552:
                    bfOut.write(f"{codeArray[i][21]}")
                elif codeArray[i][21] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][21] == -5555:
                    bfOut.write("N/S")

                # Pressure
                if codeArray[i][22] == 99:
                    bfOut.write(f"0{codeArray[i][22]}")
                elif codeArray[i][22] == 559:
                    bfOut.write(f"{codeArray[i][22]}")
                elif codeArray[i][22] == 529:
                    bfOut.write(f"{codeArray[i][22]}")
                elif codeArray[i][22] == 299:
                    bfOut.write(f"{codeArray[i][22]}")
                elif codeArray[i][22] == 552:
                    bfOut.write(f"{codeArray[i][22]}")
                elif codeArray[i][22] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][22] == -5555:
                    bfOut.write("N/S")

                # Precipitation
                if codeArray[i][23] == 999:
                    bfOut.write(f"{codeArray[i][23]}")
                elif codeArray[i][23] == 559:
                    bfOut.write(f"{codeArray[i][23]}")
                elif codeArray[i][23] == 529:
                    bfOut.write(f"{codeArray[i][23]}")
                elif codeArray[i][23] == 299:
                    bfOut.write(f"{codeArray[i][23]}")
                elif codeArray[i][23] == 552:
                    bfOut.write(f"{codeArray[i][23]}")
                elif codeArray[i][23] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][23] == -5555:
                    bfOut.write("N/S")

                # Speed
                if codeArray[i][24] == 999:
                    bfOut.write(f"{codeArray[i][24]}")
                elif codeArray[i][24] == 559:
                    bfOut.write(f"{codeArray[i][24]}")
                elif codeArray[i][24] == 529:
                    bfOut.write(f"{codeArray[i][24]}")
                elif codeArray[i][24] == 299:
                    bfOut.write(f"{codeArray[i][24]}")
                elif codeArray[i][24] == 552:
                    bfOut.write(f"{codeArray[i][24]}")
                elif codeArray[i][24] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][24] == -5555:
                    bfOut.write("N/S")

                # Direction
                if codeArray[i][25] == 999:
                    bfOut.write(f"{codeArray[i][25]}")
                elif codeArray[i][25] == 559:
                    bfOut.write(f"{codeArray[i][25]}")
                elif codeArray[i][25] == 529:
                    bfOut.write(f"{codeArray[i][25]}")
                elif codeArray[i][25] == 299:
                    bfOut.write(f"{codeArray[i][25]}")
                elif codeArray[i][25] == 552:
                    bfOut.write(f"{codeArray[i][25]}")
                elif codeArray[i][25] == 3333:
                    bfOut.write("N/A")
                elif codeArray[i][25] == -5555:
                    bfOut.write("N/S")

            bfOut.close()
        except IOError:
            raise IOError("Erro durante a escrita do arquivo: ",output)


    def writeReportData(self, output, station, year, month, id, codeArray, latitude, longitude):
        try:
            bfOut = open(output, 'w')
            for i in range(len(codeArray)):
                self.num = self.data[i][3]
                self.div = self.num / 60
                self.dia_jul = int(self.data[i][2])

                self.day_angle = (2 * np.pi) / (365.25 * self.dia_jul)
                self.dec = (self.d0 - self.dc1 * np.cos(self.day_angle) + self.ds1 * np.sin(self.day_angle) - self.dc2 * np.cos(2 * self.day_angle) + self.ds2 * np.sin(2 * self.day_angle) - self.dc3 * np.cos(3 * self.day_angle) + self.ds3 * np.sin(3 * self.day_angle))

                self.eqtime = (self.et0 + self.tc1 * np.cos(self.day_angle) - self.ts1 * np.sin(self.day_angle) - self.tc2 * np.cos(2 * self.day_angle) - self.ts2 * np.sin(2 * self.day_angle)) * 229.18

                self.tcorr = (self.eqtime + 4 * (longitude - 0)) / 60

                self.horacorr = self.tcorr + self.div

                self.hour_angle = (12.00 - self.horacorr) * 15

                self.u0 = np.sin(self.dec) * np.sin(latitude * self.CDR) + np.cos(self.dec) * np.cos(latitude * self.CDR) * np.cos(self.hour_angle * self.CDR)

                self.zenith_angle = (np.arccos(self.u0)) * 180 / np.pi

                #------------------ Código em Java não trata caso zenith_angle == 90 ---------------
                if self.zenith_angle < 90:

                    # Global Radiation
                    if codeArray[i][4] == 999:
                        self.cont_glv += 1
                    elif codeArray[i][4] == 599:
                        self.cont_glv += 1
                    elif codeArray[i][4] == 552:
                        self.cont_gl1n += 1
                    elif codeArray[i][4] == 529:
                        self.cont_gl2n += 1
                    elif codeArray[i][4] == 299:
                        self.cont_gl3n += 1
                    elif codeArray[i][4] == -5555:
                        self.flag_gl = 1
                    elif codeArray[i][4] == 3333 or codeArray[i][4] == -6999:
                        self.cont_glna += 1

                    # Direct Radiation
                    if codeArray[i][28] == 999:
                        self.cont_div += 1
                    elif codeArray[i][28] == 599:
                        self.cont_div += 1
                    elif codeArray[i][28] == 552:
                        self.cont_di1n += 1
                    elif codeArray[i][28] == 529:
                        self.cont_di2n += 1
                    elif codeArray[i][28] == 299:
                        self.cont_di3n += 1
                    elif codeArray[i][28] == -5555:
                        self.flag_di = 1
                    elif codeArray[i][28] == 3333 or codeArray[i][28] == -6999:
                        self.cont_dina += 1

                    # Diffuse Radiation
                    if codeArray[i][8] == 999:
                        self.cont_dfv += 1
                    elif codeArray[i][8] == 599:
                        self.cont_dfv += 1
                    elif codeArray[i][8] == 552:
                        self.cont_df1n += 1
                    elif codeArray[i][8] == 529:
                        self.cont_df2n += 1
                    elif codeArray[i][8] == 299:
                        self.cont_df3n += 1
                    elif codeArray[i][8] == -5555:
                        self.flag_df = 1
                    elif codeArray[i][8] == 3333 or codeArray[i][8] == -6999:
                        self.cont_dfna += 1

                    # Long Wave
                    if codeArray[i][32] == 999:
                        self.cont_lwv += 1
                    elif codeArray[i][32] == 599:
                        self.cont_lwv += 1
                    elif codeArray[i][32] == 552:
                        self.cont_lw1n += 1
                    elif codeArray[i][32] == 529:
                        self.cont_lw2n += 1
                    elif codeArray[i][32] == 299:
                        self.cont_lw3n += 1
                    elif codeArray[i][32] == -5555:
                        self.flag_lw = 1
                    elif codeArray[i][32] == 3333 or codeArray[i][32] == -6999:
                        self.cont_lwna += 1

                    # Par
                    if codeArray[i][12] == 999:
                        self.cont_pav += 1
                    elif codeArray[i][12] == 599:
                        self.cont_pav += 1
                    elif codeArray[i][12] == 552:
                        self.cont_pa1n += 1
                    elif codeArray[i][12] == 529:
                        self.cont_pa2n += 1
                    elif codeArray[i][12] == 299:
                        self.cont_pa3n += 1
                    elif codeArray[i][32] == -5555:
                        self.flag_pa = 1
                    elif codeArray[i][12] == 3333 or codeArray[i][12] == -6999:
                        self.cont_pana += 1

                    # Lux
                    if codeArray[i][16] == 999:
                        self.cont_lxv += 1
                    elif codeArray[i][16] == 599:
                        self.cont_lxv += 1
                    elif codeArray[i][16] == 552:
                        self.cont_lx1n += 1
                    elif codeArray[i][16] == 529:
                        self.cont_lx2n += 1
                    elif codeArray[i][16] == 299:
                        self.cont_lx3n += 1
                    elif codeArray[i][16] == -5555:
                        self.flag_lx = 1
                    elif codeArray[i][16] == 3333 or codeArray[i][16] == -6999:
                        self.cont_lxna += 1

                if self.zenith_angle > 90:

                    # Global Radiation
                    if codeArray[i][4] == 3333 or codeArray[i][4] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][4] != 3333 and codeArray[i][4] != -6999:
                        self.cont_vgl += 1

                    # Direct Radiation
                    if codeArray[i][28] == 3333 or codeArray[i][28] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][28] != 3333 and codeArray[i][28] != -6999:
                        self.cont_vgl += 1

                    # Diffuse Radiation
                    if codeArray[i][8] == 3333 or codeArray[i][8] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][8] != 3333 and codeArray[i][8] != -6999:
                        self.cont_vgl += 1

                    # Long Wave
                    if codeArray[i][32] == 3333 or codeArray[i][32] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][32] != 3333 and codeArray[i][32] != -6999:
                        self.cont_vgl += 1

                    # Par
                    if codeArray[i][12] == 3333 or codeArray[i][12] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][12] != 3333 and codeArray[i][12] != -6999:
                        self.cont_vgl += 1

                    # Lux
                    if codeArray[i][16] == 3333 or codeArray[i][16] == -6999:
                        self.cont_nagl += 1

                    if codeArray[i][16] != 3333 and codeArray[i][16] != -6999:
                        self.cont_vgl += 1


                # Air Temperature
                if codeArray[i][20] == 999:
                    self.cont_tpv += 1
                elif codeArray[i][20] == 559:
                    self.cont_tpv += 1
                elif codeArray[i][20] == 552:
                    self.cont_tp1n += 1
                elif codeArray[i][20] == 529:
                    self.cont_tp2n += 1
                elif codeArray[i][20] == 299:
                    self.cont_tp3n += 1
                elif codeArray[i][20] == -5555:
                    self.flag_tp = 1
                elif codeArray[i][20] == 3333:
                    self.cont_tpna += 1

                # Relative Humidity
                if codeArray[i][21] == 9:
                    self.cont_tpv += 1
                elif codeArray[i][21] == 552:
                    self.cont_tp1n += 1
                elif codeArray[i][21] == -5555:
                    self.flag_tp = 1
                elif codeArray[i][21] == 3333:
                    self.cont_tpna += 1

                # Atmospheric Pressure
                if codeArray[i][22] == 99:
                    self.cont_psv += 1
                elif codeArray[i][22] == 559:
                    self.cont_psv += 1
                elif codeArray[i][22] == 552:
                    self.cont_ps1n += 1
                elif codeArray[i][22] == 529:
                    self.cont_ps2n += 1
                elif codeArray[i][22] == -5555:
                    self.flag_ps = 1
                elif codeArray[i][22] == 3333:
                    self.cont_psna += 1








        except IOError:
            raise IOError("Erro durante a escrita do arquivo: ", output)