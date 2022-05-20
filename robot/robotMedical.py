import random

from .robot import Robot

class medicalRobot(Robot):
    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poderDeCura = random.random()
    
    def __repr__(self) -> str:
        return f"{super().__repr__()}\nPoder de cura: {self.__poderDeCura:.3f}"

    def curar(self, precisaCura: Robot) -> bool:
        if self.vida >= precisaCura.vida:
            vida = precisaCura.vida
            vida += self.__poderDeCura
            precisaCura.vida = vida
            return True
        else:
            print("Impossível curar, vida do médico é pouca para curar")
            return False