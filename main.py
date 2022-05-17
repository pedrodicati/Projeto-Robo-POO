import os

from time import sleep
from platform import system

from robot.robot import Robot
from robot.robotMedical import medicalRobot
from robot.robotFighter import fighterRobot

def criaRobo() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    print("Existem 3 tipos de robôs:")
    print("1 - Robô")
    print("2 - Robô Lutador")
    print("3 - Robô Médico")

    tipo = int(input("\nDigite o número do tipo do robô que deseja criar: "))

    if tipo == 1:
        print("\nTipo escolhido: ROBÔ")
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(Robot(name))
    elif tipo == 2:
        print("\nTipo escolhido: ROBÔ LUTADOR")
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(fighterRobot(name))
    elif tipo == 3:
        print("\nTipo escolhido: ROBÔ MÉDICO")
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(medicalRobot(name))

    print("\nRobô criado! Confira na lista para verificar suas informações\n\n")

def listaRobot() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    for i in range(len(listaRobots)):
        print(f"ID: {i}\n{listaRobots[i]}\n")

def casamentoRobot() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    listaRobot()

    idParceiro1 = int(input("Digite o ID do primeiro robô para o casamento: "))
    idParceiro2 = int(input("Digite o ID do parceiro para o casamento: "))

    listaRobots.append(listaRobots[idParceiro1] + listaRobots[idParceiro2])

    print("\nCasamento realizado com sucesso. O robô gerado possui por conta do casamento tem nome da forma descrita abaixo:")
    print(f"{listaRobots[idParceiro1].getNome()}-{listaRobots[idParceiro1].getNome()}\n\n")

def lutaRobot() -> None:
    for i in range(len(listaRobots)):
        if listaRobots[i].__class__ == fighterRobot:
            print(listaRobots[i])

    print("Para atacar o robô só pode ser do tipo LUTADOR")    
    # idLutador1 = int(input("Escolha um robô lutador para atacar"))


if __name__ == "__main__":
    conditionWhile = True
    listaRobots = list()
    
    m = Robot("l")
    a = fighterRobot('trot')
    b = medicalRobot('saosao')
    listaRobots.append(m)
    listaRobots.append(a)
    listaRobots.append(b)
    
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    while (conditionWhile == True):

        print("MENU")
        print("1 - Criar robôs")
        print("2 - Listar robôs existentes")
        print("3 - Casamento de robôs (gera um filho robô)")
        print("4 - Luta")
        print("0 - Sair do programa")

        menu = int(input("Digite o número da operação que deseja realizar: "))

        if menu == 1:
            criaRobo()
        elif menu == 2:
            listaRobot()
            print("\n")
        elif menu == 3:
            casamentoRobot()
        elif menu == 4:
            lutaRobot()
        elif menu == 0:
            conditionWhile = False
    
    

    # print(len(listaRobots))
    # m = fighterRobot('fg')
    # listaRobots.append(fighterRobot('s'))
    # listaRobot()

    # print(listaRobots[3])
