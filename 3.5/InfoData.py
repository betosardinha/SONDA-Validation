# Importar struct para conversão Double para LongBits
import struct


# Função de conversão de Double para LongBits
def doubleToLongBits(double):
    return int.from_bytes(struct.pack('d', double), 'little')


# Classe principal InfoData
class InfoData:

    # Função de inicialização, setando os argumentos a seus respectivos atributos passados ou None
    def __init__(self, id=None, inputData=None, outputData=None, outputCode=None, outputReport=None, station=None,
                 observation=None, dateOfValidation=None, latitudeOfStation=None, longitudeOfStation=None, month=None,
                 year=None):
        self.id = id
        self.inputData = inputData
        self.outputData = outputData
        self.outputCode = outputCode
        self.outputReport = outputReport
        self.station = station
        self.observation = observation
        self.dateOfValidation = dateOfValidation
        self.latitudeOfStation = latitudeOfStation
        self.longitudeOfStation = longitudeOfStation
        self.month = month
        self.year = year

    # Gets e Sets específicos de cada atributo (retornos e atribuições)
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getInputData(self):
        return self.inputData

    def setInputData(self, inputData):
        self.inputData = inputData

    def getOutputData(self):
        return self.outputData

    def setOutputData(self, outputData):
        self.outputData = outputData

    def getOutputCode(self):
        return self.outputCode

    def setOutputCode(self, outputCode):
        self.outputCode = outputCode

    def getOutputReport(self):
        return self.outputReport

    def setOutputReport(self, outputReport):
        self.outputReport = outputReport

    def getStation(self):
        return self.station

    def setStation(self, station):
        self.station = station

    def getObservation(self):
        return self.observation

    def setObservation(self, observation):
        self.observation = observation

    def getDateOfValidation(self):
        return self.dateOfValidation

    def setDateOfValidation(self, dateOfValidation):
        self.dateOfValidation = dateOfValidation

    def getLatitudeOfStation(self):
        return self.latitudeOfStation

    def setLatitudeOfStation(self, latitudeOfStation):
        self.latitudeOfStation = latitudeOfStation

    def getLongitudeOfStation(self):
        return self.longitudeOfStation

    def setLongitudeOfStation(self, longitudeOfStation):
        self.longitudeOfStation = longitudeOfStation

    def getMonth(self):
        return self.month

    def setMonth(self, month):
        self.month = month

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    # Função que cria Hash da instância com base em seus atributos
    def hashCode(self):
        PRIME = 31
        RESULT = 1
        temp1 = doubleToLongBits(self.latitudeOfStation)
        temp2 = doubleToLongBits(self.longitudeOfStation)

        RESULT = PRIME * RESULT + (0 if self.id is None else hash(self.id))
        RESULT = PRIME * RESULT + (0 if self.inputData is None else hash(self.inputData))
        RESULT = PRIME * RESULT + (0 if self.outputData is None else hash(self.outputData))
        RESULT = PRIME * RESULT + (0 if self.outputCode is None else hash(self.outputCode))
        RESULT = PRIME * RESULT + (0 if self.outputReport is None else hash(self.outputReport))
        RESULT = PRIME * RESULT + (0 if self.observation is None else hash(self.observation))
        RESULT = PRIME * RESULT + (0 if self.station is None else hash(self.station))
        RESULT = PRIME * RESULT + (0 if self.dateOfValidation is None else hash(self.dateOfValidation))

        RESULT = PRIME * RESULT + int(temp1 ^ ((temp1 % 0x100000000) >> 32))
        RESULT = PRIME * RESULT + int(temp2 ^ ((temp2 % 0x100000000) >> 32))

        RESULT = PRIME * RESULT + (0 if self.month is None else hash(self.month))
        RESULT = PRIME * RESULT + (0 if self.year is None else hash(self.year))

        return RESULT

    # Função que compara dois objetos retornando True se iguais ou False se diferentes em qualquer nível
    def equals(self, obj):
        try:
            obj
        except NameError:
            obj = None

        if self == obj:
            return True

        if obj is None:
            return False

        if type(self) != type(obj):
            return False

        if self.id is None:
            if obj.id is not None:
                return False
        elif self.id != obj.id:
            return False

        if self.inputData is None:
            if obj.inputData is not None:
                return False
        elif self.inputData != obj.inputData:
            return False

        if self.outputData is None:
            if obj.outputData is not None:
                return False
        elif self.outputData != obj.outputData:
            return False

        if self.outputCode is None:
            if obj.outputCode is not None:
                return False
        elif self.outputCode != obj.outputCode:
            return False

        if self.outputReport is None:
            if obj.outputReport is not None:
                return False
        elif self.outputReport != obj.outputReport:
            return False

        if self.station is None:
            if obj.station is not None:
                return False
        elif self.station != obj.station:
            return False

        if self.observation is None:
            if obj.observation is not None:
                return False
        elif self.observation != obj.observation:
            return False

        if self.dateOfValidation is None:
            if obj.dateOfValidation is not None:
                return False
        elif self.dateOfValidation != obj.dateOfValidation:
            return False

        if doubleToLongBits(self.latitudeOfStation) == doubleToLongBits(obj.latitudeOfStation):
            return False

        if doubleToLongBits(self.longitudeOfStation) == doubleToLongBits(obj.longitudeOfStation):
            return False

        if self.month is None:
            if obj.month is not None:
                return False
        elif self.month != obj.month:
            return False

        if self.year is None:
            if obj.year is not None:
                return False
        elif self.year != obj.year:
            return False

        return True

    # Função para criar String com os atributos da instância específica
    def toString(self):
        builder = "InfoData [Id= " + str(self.id)
        + ", Arquivo de Entrada= " + str(self.inputData)
        + ", Nome da Estação= " + str(self.station)
        + ", Data de Validação= " + str(self.dateOfValidation)
        + ", Latitude da Estação= " + str(self.latitudeOfStation)
        + ", Longitude da Estação= " + str(self.longitudeOfStation)
        + ", Observação= " + str(self.observation)
        + "]"

        return builder
