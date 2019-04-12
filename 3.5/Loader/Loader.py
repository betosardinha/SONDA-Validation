import numpy as np


class Loader:

    # Init function, setting parameters to the respective attributes (None if not passed)
    def __init__(self, rawData=None, numberOfColumns=None, numberOfRows=None):
        self.rawData = np.array(rawData)
        self.numberOfColumns = numberOfColumns
        self.numberOfRows = numberOfRows
        self.temp = np.array([])
        self.lines = np.array([])
        self.data = np.array([])
        self.data = np.array([])
        self.limits = np.array([])
        self.code = np.array([])

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
            raise IOError("Erro durante a escrita do arquivo", output)



