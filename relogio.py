class Relogio:
    def __init__(self):
        self.__dia = 1
        self.__horas = 7
        self.__minutos = 0
    
    @property
    def dia(self):
        return self.__dia
    
    @property
    def horas(self):
        return self.__horas
    
    @property
    def minutos(self):
        return self.__minutos
    
    def __str__(self):
        return f'{self.__horas:02d}:{self.__minutos:02d}\nDia {self.__dia}'
    
    def avancaTempo(self, horas = 0, minutos = 0):
        self.__horas += horas
        self.__minutos += minutos
        while self.__minutos >= 60:
            self.__minutos -= 60
            self.__horas += 1
        while self.__horas >= 24:
            self.__horas -= 24
            self.__dia += 1