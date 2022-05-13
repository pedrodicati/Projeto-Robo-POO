from abc import abstractmethod
from curses import panel
import random

class Robot:
    __nivelCritico: float

    def __init__(self, nome: int) -> None:
        self.__nome = nome
        self.__nivelCritico = 0.20
        self.__vida = random.random()

    def __repr__(self) -> str:
        return f"{self.__class__}\nNome do robô: {self.__nome}\nVida: {self.__vida:.2f}"

    def __add__(self, parceiro: 'Robot') -> 'Robot':
        # retornar uma nova instância do tipo atual do objeto, em vez de manter tudo como Robot
        return type(self)(self.__nome + '-' + parceiro.__nome)

    def precisaDeMedico(self):
        if self.getVida() < self.__nivelCritico:
            return True
        else:
            return False
    
    def getVida(self):
        return self.__vida
    
    def setVida(self, vida):
        if vida > 1.0:
            vida = 1.0
        self.__vida = vida


class medicalRobot(Robot):
    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poderDeCura = random.random()
    
    def __repr__(self) -> str:
        return f"{super().__repr__()}\nPoder de cura: {self.__poderDeCura:.2f}"

    # def __add__(self, parceiro: Robot) -> Robot:
    #     return super().__add__(self, parceiro)

    def curar(self, precisaCura: Robot) -> bool:
        if self.getVida() >= precisaCura.getVida():
            vida = precisaCura.getVida()
            vida += self.__poderDeCura
            precisaCura.setVida(vida)
            return True
        else:
            print("Impossível curar, vida do médico é pouca para curar")
            return False

class fighterRobot(Robot):
    __danoMaximo = 0.30

    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poder = random.uniform(self.__danoMaximo, 1)

    def __repr__(self) -> str:
        return f"{super().__repr__()}\nPoder = {self.__poder:.2f}"

    def atacar(self, atacado: 'Robot'):
        atacado.setVida(atacado.getVida() * (1 - self.__poder))

    def contraAtaque(self, quemAtacou: Robot):
        pass

if __name__ == "__main__":
    # r1 = medicalRobot('roto')
    # print(r1)
    # r2 = Robot('alia')
    # r3 = r1 + r2
    # print(r3, r3.__class__)
    m1 = medicalRobot('m1')
    print(m1)
    f1 = fighterRobot('pp')
    print(f1)
    f2 = fighterRobot('al')
    print(f2)

    print('\n')

    f1.atacar(f2)
    print(f"{f1}\n\n{f2}")

    print(f"\n{f1.precisaDeMedico()}\n")

    if(f1.precisaDeMedico()):
        m1.curar(f2)
        

    print(f2)
    