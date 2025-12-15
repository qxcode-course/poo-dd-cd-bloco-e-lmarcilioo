from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo:str, horaEntrada:int):
        self.__id = id
        self.tipo = tipo
        self.__horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self):    
        pass

    def getId(self):
        return self.__id
    
    def setEntrada(self, horaEntrada: int) -> None:
        self.horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.__horaEntrada

class Estacionamento(Veiculo):
    def __init__ (self, horaEntrada:int, id:str, tipo: str ):
        super().__init__(id, tipo, horaEntrada)
        self.veiculos: list [Veiculo]= []
        self.horaAtual = 0

    def procurarVeiculo(self, id:str):
        for i in self.veiculos:
            if i.getId == id:
                return i
            
    def estacionar(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)
        veiculo.setEntrada(self.horaAtual)

    def pagar(self, id: str):
        for i in self.veiculos:
            if i.getId() == id:
                valor = i.calcularValor()
                return valor
            
    def sair (self, id:str):
        for i in self.veiculos:
            if i.getId() == id:
                self.veiculos.remove(i)
    
    def passarTempo(self, tempo:int):
        self.horaAtual += tempo

