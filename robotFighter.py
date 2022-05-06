from robot import Robot

class fighterRobot(Robot):
    __danoMaximo: float

    def __init__(self, nome: int) -> None:
        super().__init__(nome)

    def __repr__(self) -> str:
        return super().__repr__()

    def __add__(self, parceiro: Robot) -> Robot:
        return fighterRobot(self.__nome + parceiro.__nome)

r1 = fighterRobot("a")
r2 = fighterRobot("b")
print(r1 + r2)