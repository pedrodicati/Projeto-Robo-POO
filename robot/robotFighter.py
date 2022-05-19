import random

from .robot import Robot

class fighterRobot(Robot):
    __danoMaximo = 0.30

    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poder = random.uniform(self.__danoMaximo, 1)

    def __repr__(self) -> str:
        return f"{super().__repr__()}\nPoder = {self.__poder:.3f}"

    @property
    def poder(self) -> float:
        return self.__poder

    def atacar(self, atacado: Robot) -> None:
        descontaVida = 1 - self.poder

        novaVida = atacado.vida * descontaVida

        atacado.vida = novaVida

    def contraAtaque(self, quemAtacou: Robot) -> None:
        pass

if __name__ == "__main__":
    r = Robot("paranaue")
    r2 = fighterRobot("sasa")

    print(f"{r}\n\n{r2}")

    r2.atacar(r)

    print(f"\n{r}\n\n{r2}")