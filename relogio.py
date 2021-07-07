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
        horario = f'{self.__horas:02d}:{self.__minutos:02d}'
        return f'''
        {"Agora são:":>15}
        {horario:>14},
        {self.diaDaSemana():>15}'''
    
    def avancaTempo(self, horas = 0, minutos = 0):
        self.__horas += horas
        self.__minutos += minutos
        while self.__minutos >= 60:
            self.__minutos -= 60
            self.__horas += 1
        while self.__horas >= 24:
            self.__horas -= 24
            self.__dia += 1
    
    def diaDaSemana(self):
        semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
        diaSemana = semana[self.__dia % 7]
        return diaSemana
