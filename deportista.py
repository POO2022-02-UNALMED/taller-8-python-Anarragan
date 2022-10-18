class Deportista():

#Constructors 
    def __init__(self, deporte, años):
        self._deporte = deporte
        self._añosPracticando = años


#Getters and setters

    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, j):
        self._deporte = j

    def getAñosPracticando (self):
        return self._añosPracticando

    def setAñosPracticando(self, j):
        self._añosPracticando



