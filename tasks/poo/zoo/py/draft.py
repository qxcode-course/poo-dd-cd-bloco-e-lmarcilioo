from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name : str) :
        self.__name : str = name
    
    @abstractmethod
    def fazer_som (self):
        pass

    @abstractmethod
    def mover(self):
        pass

    def getName (self) -> str :
        return self.__name
    
    def setName (self, name : str) :
        self.__name = name

    def apresentarNome (self) -> str :
        return f"Eu sou um(a) {self.getName()}"
    
class Leao(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def fazer_som(self):
        print("ROARRRRRR")

    def mover(self):
        print("TUM-TUM-TUM. O LEÃO ANDA PELA SELVA!!!!!")

class Elefante(Animal):
    def __init__(self, name: str) :
        super().__init__(name)

    def fazer_som(self) :
        print ("fummmmmmmm")

    def mover(self) :
        print("BUM! BUM! BUM!. O ELEFANTE ANDA PELA SELVA!!!!!!")

class Snake(Animal) :
    def __init__(self, name: str) :
        super().__init__(name)

    def fazer_som(self) :
        print("SSSSSSSSSSSSSS")

    def mover(self) :
        print("SSSSSSSSSSSSSSSSS. A COBRA RASTEJA PELA SELVA!!!!!!")

def apresentar_animal(animal: Animal):
    animal.apresentarNome()
    animal.fazer_som()
    animal.mover()

listaAnimal: list[Animal]= [Leao('Simba'), Elefante("Dumbo"), Snake('DJ')]
for i in listaAnimal:
    apresentar_animal(i)


