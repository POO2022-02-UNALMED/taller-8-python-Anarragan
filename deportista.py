class Deportista():

#Constructors 
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
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



