import os
from platform import system

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
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(Robot(name))
    elif tipo == 2:
        print("Tipo escolhido: ROBÔ LUTADOR")
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(fighterRobot(name))
    elif tipo == 3:
        print("Tipo escolhido: ROBÔ MÉDICO")
        name = str(input("Digite o nome do seu novo robô: "))
        listaRobots.append(medicalRobot(name))

def listaRobot() -> None:
    for i in range(len(listaRobots)):
        print(f"ID: {i}\n{listaRobots[i]}\n")

def casamentoRobot() -> None:
    listaRobot()

    idParceiro1 = int(input("Digite o ID do primeiro robô para o casamento: "))
    idParceiro2 = int(input("Digite o ID do parceiro para o casamento: "))

    listaRobots.append(listaRobots[idParceiro1] + listaRobots[idParceiro2])


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
        elif menu == 3:
            casamentoRobot()
        elif menu == 4:
            pass
        elif menu == 0:
            conditionWhile = False
    
    

    # print(len(listaRobots))
    # m = fighterRobot('fg')
    # listaRobots.append(fighterRobot('s'))
    # listaRobot()

    # print(listaRobots[3])
