class Equipo:
    
    def __init__(self,nome):
        self.__nome = nome
        self.__ganhados = 0
        self.__perdidos = 0
        self.__empatados = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ganhados(self):
        return self.__ganhados

    @property
    def perdidos(self):
        return self.__perdidos

    @property
    def empatados(self):
        return self.__empatados

    def add_victoria (self):
        self.__ganhados += 1

    def add_perdido (self):
        self.__perdidos += 1

    def add_empate (self):
        self.__empates += 1

    def get_puntos(self):
        return self.__ganhados*3 + self.__empatados

    def get_encontros_xogados (self):
        return self.__ganhados + self.__empatados + self.__perdidos

    def __str__(self):
        return self.__nome + (' -V:')+ str(self.__ganhados) + " -E:" + str(self.__empatados) + " -D:" + str(self.__perdidos)+ "'(Puntos: " + str(self.get_puntos()) +')'
