from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

#Constructor

    def __init__(self, nombre, edad, altura, sexo, años, goles, tarjetas, habil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,'Futbol',años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = habil
        Futbolista._listaFutbolistas.append(self)


#Getters

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def getListaFutolistas(cls):
        return cls._listaFutbolistas

    
#Setters

    def setGolesMarcados(self, j):
        self._golesMarcados = j

    def setTarjetasRojas(self, j):
        self._tarjetasRojas = j

    def setPiernaHabil(self, j):
        self._piernaHabil = j


    def __str__(self):
        return f'Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte'

