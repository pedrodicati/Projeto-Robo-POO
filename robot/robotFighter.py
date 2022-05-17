import random

from .robot import Robot

class fighterRobot(Robot):
    __danoMaximo = 0.30

    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poder = random.uniform(self.__danoMaximo, 1)

    def __repr__(self) -> str:
        return f"{super().__repr__()}\nPoder = {self.__poder:.2f}"

    def atacar(self, atacado: Robot):
        atacado.setVida(atacado.getVida() * (1 - self.__poder))

    def contraAtaque(self, quemAtacou: Robot):
        pass