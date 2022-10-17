class Deportista():

#Constructors 
    def __init__(self, añosPracticando):
        self._deporte = "Futbol"
        self._aniosPracticando = añosPracticando


#Getters and setters

    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAñosPracticando (self):
        return self.añosPracticando

    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando



