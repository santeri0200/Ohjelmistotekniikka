class Maksukortti:
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f'Kortilla on rahaa {self.saldo_euroina():.2f} euroa'

    def saldo_euroina(self):
        return self.saldo / 100

    def lataa_rahaa(self, saldo):
        self.saldo = min(self.saldo + saldo, 150 * 100)

    def syo_maukkaasti(self):
        if 400 <= self.saldo:
            self.saldo -= 400

    def syo_edullisesti(self):
        if 250 <= self.saldo:
            self.saldo -= 250
