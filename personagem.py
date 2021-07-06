class Personagem:
    def __init__(self, nome='Thiago'):
        self.name = nome
        self.saude = 100
        self.relacionamento = 100
        self.dinheiro = 150
        self.estresse = 0
        self.xp = 0
    
    def __str__(self):
        return f'Saúde: {self.saude}\nRelacionamento: {self.relacionamento}\nDinheiro: {self.dinheiro}\nEstresse: {self.estresse}\n Experiência: {self.xp}'

    def _avaliar(self, valor):
        if valor > 100:
            return 100
        elif valor < 0:
            return 0
        else:
            return valor

    def dormir(self):
        self.saude += 20
        self.saude = self._avaliar(self.saude)
        self.estresse -= 50
        if self.estresse < 0:
            self.estresse = 0

    def passear(self):
        self.relacionamento += 20
        if self.relacionamento > 100:
            self.relacionamento = 100
        self.estresse -= 20
        if self.estresse < 0:
            self.estresse = 0
        self.saude -= 30
        if self.saude < 0:
            self.saude = 0
    
    def netflix(self):
        self.estresse -= 20
        if self.estresse < 0:
            self.estresse = 0
        self.relacionamento -= 20
        if self.relacionamento < 0:
            self.relacionamento = 0