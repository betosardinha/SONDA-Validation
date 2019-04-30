import numpy as np

from tqdm import *

from Loader import Loader


class ScreeningController:
    def __init__(self, input1=None, input2=None):
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

        if input1 is not None and input2 is not None:
            self.loader = Loader.Loader()
            self.loader.buildsMatrixData(input1)
            self.loader.buildsMatrixCode(input1)

    def progressBar(self):
        self.pb = tqdm(total=self.rows, desc="Validação")



