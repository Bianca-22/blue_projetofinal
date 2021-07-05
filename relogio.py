class Relogio:
    def __init__(self):
        self.dia = 1
        self.horas = 0
        self.minutos = 0
    
    def __str__(self):
        return f'{self.horas:02d}:{self.minutos:02d}\nDia {self.dia}'
    
    def avancaTempo(self, horas = 0, minutos = 0):
        self.horas += horas
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
        while self.horas >= 24:
            self.horas -= 24
            self.dia += 1