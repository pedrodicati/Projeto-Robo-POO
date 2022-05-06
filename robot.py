from abc import abstractmethod
import random
# from robotMedical import medicalRobot 

class Robot:
    __nivelCritico: 0.10

    def __init__(self, nome: int) -> None:
        self.__nome = nome
        self.__vida = random.random()

    def __repr__(self) -> str:
        return f"Nome do robô: {self.__nome}\nVida: {self.__vida:.2f}"

    @abstractmethod
    def __add__(self, parceiro: 'Robot') -> 'Robot':
        return Robot(self.__nome + parceiro.__nome)

    # def precisaDeMedico(self, medical: medicalRobot):
    #     pass

if __name__ == "__main__":
    r1 = Robot('nat')
    r2 = Robot('alia')
    r3 = r1 + r2
    print(r3)