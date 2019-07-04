import os
import sys
from InfoData import InfoData
from Controller import Controller
from Loader import Loader

class Validation:
    def __init__(self, args):
        if len(args) == 0:
            args = ["."]
        self.ext = ".dat"
        self.infodata = InfoData.InfoData()
        self.pathNames = args[0]
        self.cont_std = 0

    def accept(self, name):
        lowercaseName = name.lower()
        if lowercaseName.endswith(self.ext):
            return True
        else:
            return False

    def validate(self):
        fileNames = os.listdir(self.pathNames)
        for fileName in fileNames:
            if fileName[-4:] == self.ext:
                # Tirar atribuições iguais fora dos IFs
                if fileName[:3] == "BAB":
                    self.infodata.setId("03")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7]+"ED.csv")
                    self.infodata.setOutputCode(fileName[:7]+"ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7]+".csv")
                    self.infodata.setStation("Balbina")
                    self.infodata.setLatitudeOfStation(-1.9311)
                    self.infodata.setLongitudeOfStation(-59.4197)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20"+fileName[3:5])
                elif fileName[:3] == "BJL":
                    self.infodata.setId("47")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Bom Jesus da Lapa")
                    self.infodata.setLatitudeOfStation(-13.2335)
                    self.infodata.setLongitudeOfStation(-43.3760)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "BRB":
                    self.infodata.setId("10")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Brasília")
                    self.infodata.setLatitudeOfStation(-15.6008)
                    self.infodata.setLongitudeOfStation(-47.7131)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CPA":
                    self.infodata.setId("30")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Cachoeira Paulista")
                    self.infodata.setLatitudeOfStation(-22.6896)
                    self.infodata.setLongitudeOfStation(-45.0062)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CAI":
                    self.infodata.setId("20")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Caicó")
                    self.infodata.setLatitudeOfStation(-6.4669)
                    self.infodata.setLongitudeOfStation(-37.0847)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CGR":
                    self.infodata.setId("12")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Campo Grande")
                    self.infodata.setLatitudeOfStation(-20.4383)
                    self.infodata.setLongitudeOfStation(-54.5383)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CHP":
                    self.infodata.setId("06")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Chapecó")
                    self.infodata.setLatitudeOfStation(-27.0800)
                    self.infodata.setLongitudeOfStation(-52.6144)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CBA":
                    self.infodata.setId("21")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Cuiabá")
                    self.infodata.setLatitudeOfStation(-15.5553)
                    self.infodata.setLongitudeOfStation(-56.0700)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "CTB":
                    self.infodata.setId("60")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Curitiba")
                    self.infodata.setLatitudeOfStation(-25.4954)
                    self.infodata.setLongitudeOfStation(-49.3312)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "FLN":
                    self.infodata.setId("01")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Florianópolis")
                    self.infodata.setLatitudeOfStation(-27.6017)
                    self.infodata.setLongitudeOfStation(-48.5178)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "JOI":
                    self.infodata.setId("04")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Joinville")
                    self.infodata.setLatitudeOfStation(-26.2525)
                    self.infodata.setLongitudeOfStation(-48.8578)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "LEB":
                    self.infodata.setId("02")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Lebon Régis")
                    self.infodata.setLatitudeOfStation(-26.9886)
                    self.infodata.setLongitudeOfStation(-50.7150)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "MCL":
                    self.infodata.setId("45")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Montes Claros")
                    self.infodata.setLatitudeOfStation(-16.6864)
                    self.infodata.setLongitudeOfStation(-43.8688)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "NAT":
                    self.infodata.setId("17")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Natal")
                    self.infodata.setLatitudeOfStation(-5.8367)
                    self.infodata.setLongitudeOfStation(-35.2064)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "ORN":
                    self.infodata.setId("28")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Ourinhos")
                    self.infodata.setLatitudeOfStation(-22.9486)
                    self.infodata.setLongitudeOfStation(-49.8942)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "PMA":
                    self.infodata.setId("19")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Palmas")
                    self.infodata.setLatitudeOfStation(-10.1778)
                    self.infodata.setLongitudeOfStation(-48.3619)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "PTR":
                    self.infodata.setId("11")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Petrolina")
                    self.infodata.setLatitudeOfStation(-9.0689)
                    self.infodata.setLongitudeOfStation(-40.3197)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "RLM":
                    self.infodata.setId("27")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Rolim de Moura")
                    self.infodata.setLatitudeOfStation(-11.5817)
                    self.infodata.setLongitudeOfStation(-61.7736)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "SLZ":
                    self.infodata.setId("16")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("São Luiz")
                    self.infodata.setLatitudeOfStation(-2.5933)
                    self.infodata.setLongitudeOfStation(-44.2122)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "SMS":
                    self.infodata.setId("08")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("São Martinho da Serra")
                    self.infodata.setLatitudeOfStation(-29.4428)
                    self.infodata.setLongitudeOfStation(-53.8231)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "SBR":
                    self.infodata.setId("05")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Sombrio")
                    self.infodata.setLatitudeOfStation(-29.0956)
                    self.infodata.setLongitudeOfStation(-49.8133)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "TMA":
                    self.infodata.setId("44")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Termoaçu")
                    self.infodata.setLatitudeOfStation(-5.3829)
                    self.infodata.setLongitudeOfStation(-36.8191)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "TLG":
                    self.infodata.setId("48")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Três Lagoas")
                    self.infodata.setLatitudeOfStation(-20.7507)
                    self.infodata.setLongitudeOfStation(-51.6642)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])
                elif fileName[:3] == "UBE":
                    self.infodata.setId("46")
                    self.infodata.setInputData(os.path.abspath(fileName))
                    self.infodata.setOutputData(fileName[:7] + "ED.csv")
                    self.infodata.setOutputCode(fileName[:7] + "ED_DQC.csv")
                    self.infodata.setOutputReport(fileName[:7] + ".csv")
                    self.infodata.setStation("Uberaba")
                    self.infodata.setLatitudeOfStation(-19.998)
                    self.infodata.setLongitudeOfStation(-47.900)
                    self.infodata.setMonth(fileName[5:7])
                    self.infodata.setYear("20" + fileName[3:5])

                controller = Controller.Controller(os.path.abspath(fileName), fileName)
                loader = Loader.Loader()
                loader.buildsMatrixData(os.path.abspath(fileName))
                loader.code = controller.validate(self.infodata.getLatitudeOfStation(), self.infodata.getLongitudeOfStation(), int(self.infodata.getId()), int(self.infodata.getMonth()))
                loader.writeData(self.infodata.getOutputData(), loader.data, self.infodata.getId())
                loader.writeCode(self.infodata.getOutputCode(), loader.data, loader.code, self.infodata.getId())
                loader.writeReportData(self.infodata.getOutputReport(), self.infodata.getStation(), int(self.infodata.getYear()), int(self.infodata.getMonth()), self.infodata.getId(), loader.code, self.infodata.getLatitudeOfStation(), self.infodata.getLongitudeOfStation())
                self.cont_std = controller.cont_std
                if self.cont_std > 0:
                    print("\nValidação Concluída com Sucesso!!! - Obs: Existem dados com desvio padrão 0\n")
                else:
                    print("Validação Concluida com Sucesso!!!\n")


# ----------------------------------------------------------------------
# Main
# Função para ler da pasta input e escrever em output
validation = Validation(".")
validation.validate()

