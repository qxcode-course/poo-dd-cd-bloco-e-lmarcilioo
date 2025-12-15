from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__ (self, valor:float, descrição: str):
        self.valor:float = valor
        self.descrição = descrição

    def resumo (self) -> str:
        return f"Pagamento de R${self.valor}:{self.descrição}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
        
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor:float, nome:str,num:str,descrição:str,limite:float):
        super().__init__(valor,descrição)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo (self):
        return "Cartão de credito" + super().resumo()
    
    def get_limite(self):
        return self.limite
    
    def processar (self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

class Pix(Pagamento):
    def __init__(self, valor: float, descrição:str, chave: str, banco: str):
        super().__init__(valor,descrição)
        self.chave = chave
        self.banco = banco
    
    def processar(self):
        if self.valor <= 0:
            print('Pix não aprovado')
            return
        print(f'PIX enviado via {self.banco} usando chave {self.chave}')


class Boleto(Pagamento):
    def __init__(self, valor: float, descrição:str,codigoBarras:str, vencimento: str):
        super().__init__(valor,descrição)
        self.vencimento = vencimento
        self.codigoBarras= codigoBarras

    def processar(self):
        print ('Boleto gerado. Aguardando pagamento...')

pagamentos: list[Pagamento] = [Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
              CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
              Boleto(89.90,"Livro de Python", "1234567890000", "2025-01-10"),]

processar_pagamentos(pagamentos)

