class Animal:
    def __init__(self,nombre,raza): 
        self.nombre = nombre
        self.raza = raza
    def pasear(self):
        pass
    def alimentar(self):
        pass
    def dar_info(self):
        return self.nombre + " de raza: " + self.raza + ". De propietario: "  + self.propietario

class Mascota(Animal):
    def __init__(self,nombre,raza,propietario):
        super().__init__( nombre,raza) #super llama al metodo init y agrega la nueva clase
        self.propietario = propietario

class Gato(Mascota):
    def pasear(self):
        print("Paseando al gato " + self.dar_info() )
    def alimentar(self):
        print("Alimentando al gato " + self.dar_info())

class Lagarto(Mascota):
    def pasear(self):
        print("Paseando al lagarto "+ self.dar_info())
    def alimentar(self):
        print("Alimentando al lagarto "+ self.dar_info())

class Perro(Mascota):
    def pasear(self):
        print("Paseando al perro " + self.dar_info())
    
    def alimentar(self):
        print("Alimentando al perro " + self.dar_info())

if __name__ =='__main__':
    mascotas=[Perro("neron","bulldog","juan"), Gato("fifi","naranja","maria"),Lagarto("Rayo mcqueen","verde","laura")]
    
    for m in mascotas:
        m.pasear() 
        m.alimentar()
        print(" ")