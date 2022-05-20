import random

class Robot:
    __nivelCritico = 0.10

    def __init__(self, nome: str) -> None:
        self.__nome         = nome
        self.__vida         = random.random()

    def __repr__(self) -> str:
        return f"{self.__class__}\nNome do robô: {self.__nome}\nVida: {self.__vida:.3f}"

    def __add__(self, parceiro: 'Robot') -> 'Robot':
        nomePai      = self.__nome.split("-")[0]
        nomeParceiro = parceiro.__nome.split("-")[0]

        # retornar uma nova instância do tipo atual do objeto, em vez de manter tudo como Robot
        return type(self)(nomePai + '-' + nomeParceiro)

    def precisaDeMedico(self):
        if self.vida < self.__nivelCritico:
            return True
        else:
            return False
    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida: float):
        if vida > 1.0:
            vida = 1.0
        elif vida <= 0.00:
            vida = 0.01

        self.__vida = vida
    
    @property
    def nome(self):
        return self.__nome