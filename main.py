from typing import List
from robot import Robot, fighterRobot, medicalRobot
# from robotFighter import fighterRobot
# from robotMedical import medicalRobot

def criaRobo() -> None:
    print("Existem 3 tipos de robôs:")
    print("1 - Robô")
    print("2 - Robô Lutador")
    print("3 - Robô Médico")

    tipo = int(input("Digite o número do tipo do robô que deseja criar: "))

    if tipo == 1:
        print("Tipo escolhido: ROBÔ")
        name = str(input("Digite o nome do sue novo robô: "))
        listaRobots.append(Robot(name))
    elif tipo == 2:
        print("Tipo escolhido: ROBÔ LUTADOR")
        name = str(input("Digite o nome do sue novo robô: "))
        listaRobots.append(fighterRobot(name))
    elif tipo == 3:
        print("Tipo escolhido: ROBÔ MÉDICO")
        name = str(input("Digite o nome do sue novo robô: "))
        listaRobots.append(medicalRobot(name))

def listaRobot() -> None:
    for i in range(len(listaRobots)):
        print(f"ID: {i}\n{listaRobots[i]}\n")

if __name__ == "__main__":
    conditionWhile = True
    listaRobots = list()
    
    m = Robot("l")
    a = fighterRobot('trot')
    b = medicalRobot('saosao')
    listaRobots.append(m)
    listaRobots.append(a)
    listaRobots.append(b)
    
    while (conditionWhile == True):
        listaRobot()
        print("MENU")
        print("1 - Criar robôs")
        print("2 - Lista robôs")
        print("3 - Casamento de robôs (gera um filho robô)")
        print("4 - Luta")
        print("0 - Sair do programa")

        menu = int(input("Digite o número da operação que deseja realizar: "))

        if menu == 1:
            criaRobo()
        elif menu == 2:
            listaRobot()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 0:
            conditionWhile = False
    
    

    # print(len(listaRobots))
    # m = fighterRobot('fg')
    # listaRobots.append(fighterRobot('s'))
    # listaRobot()

    # print(listaRobots[3])

    criaRobo()
    listaRobot()
