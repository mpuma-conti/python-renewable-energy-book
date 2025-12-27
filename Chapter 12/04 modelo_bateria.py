class Bateria:
    def __init__(self, capacidad_total, soc_inicial, eficiencia):
        self.capacidad_total = capacidad_total  # kWh
        self.soc = soc_inicial  # Estado de carga inicial (%)
        self.eficiencia = eficiencia

    def cargar(self, energia):
        energia_real = energia * self.eficiencia
        self.soc += energia_real / self.capacidad_total * 100
        if self.soc > 100:
            self.soc = 100

    def descargar(self, demanda):
        energia_disponible = self.soc / 100 * self.capacidad_total
        if demanda > energia_disponible:
            energia_suministrada = energia_disponible
            self.soc = 0
        else:
            energia_suministrada = demanda
            self.soc -= (energia_suministrada / self.capacidad_total) * 100
        return energia_suministrada
