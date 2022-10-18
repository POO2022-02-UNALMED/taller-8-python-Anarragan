class Persona():

#Constructors

    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo



#Getters and setters

    def getNombre(self):
        return self._nombre
        
    def setNombre(self, j):
        self._nombre = j

    def getEdad(self):
        return self._edad
        
    def setEdad(self, j):
        self._edad = j

    def getAltura(self):
        return self._altura
        
    def setAltura(self, j):
        self._altura = j

    def getSexo(self):
        return self._sexo
        
    def setSexo(self, j):
        self._sexo = j