import random
from robot import Robot

class medicalRobot(Robot):
    def __init__(self, nome: int) -> None:
        super().__init__(nome)
        self.__poderDeCura = random.random()
    
    def __repr__(self) -> str:
        return f"Tipo do robô: Robô Médico\n" + super().__repr__() + f"\nPoder de cura: {self.__poderDeCura:.2f}"

    def __add__(self, parceiro: Robot) -> Robot:
        return medicalRobot(self.__nome + parceiro.__nome)

    def curar(self, precisaCura: Robot):
        precisaCura.__vida += self.__poderDeCura

if __name__ == "__main__":
    m = medicalRobot("m1")
    # print(m.poderDeCura, m.vida)
    #print(f"Reduzindo para 4 casas decimais a vida {m.vida:.2f} e o poder de cura {m.poderDeCura:.2f}")
    print(m)
    m2 = medicalRobot('saosao')
    print(m2)

    print(m + m2)
