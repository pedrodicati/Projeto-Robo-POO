import os
from random import random, randint
from secrets import choice

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
        robots.append(Robot(name))
    elif tipo == 2:
        print("\nTipo escolhido: ROBÔ LUTADOR")
        name = str(input("Digite o nome do seu novo robô: "))
        robots.append(fighterRobot(name))
    elif tipo == 3:
        print("\nTipo escolhido: ROBÔ MÉDICO")
        name = str(input("Digite o nome do seu novo robô: "))
        robots.append(medicalRobot(name))

    print("\nRobô criado! Confira na lista para verificar suas informações\n\n")

def listaRobot() -> None:
    for i in range(len(robots)):
        print(f"ID: {i}\n{robots[i]}\n")

def casamentoRobot() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    listaRobot()

    idParceiro1 = int(input("Digite o ID do primeiro robô para o casamento: "))
    idParceiro2 = int(input("Digite o ID do parceiro para o casamento: "))

    robots.append(robots[idParceiro1] + robots[idParceiro2])

    print(f"\nCasamento realizado com sucesso. O robô gerado tem nome: {robots[idParceiro1].nome}-{robots[idParceiro2].nome}")

def lutaRobot() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    print("===== BATALHA =====")
    print("Chegou a hora da batalha!!\n")
    sleep(2.0)

    for i in range(len(robots)):
        if robots[i].__class__ == fighterRobot:
            print(f"ID = {i}\n{robots[i]}")

    print("\nPara atacar, o robô deve ser do tipo fighterRobot!")
    idAtacante = int(input("Escolha o ID de um robô lutador para atacar: "))

    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    print("===== BATALHA =====")
    print("Agora é a hora de escolher quem será a vítima, pode ser qualquer tipo de robô!\n")    
    sleep(2.0)

    listaRobot()
    idAtacado  = int(input("\nEscolha o ID de quem o lutador irá atacar: "))
 
    robots[idAtacante].atacar(robots[idAtacado])

    if robots[idAtacado].__class__ == fighterRobot: # se o robô que foi atacado for lutador também
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:")
        print(f"{robots[idAtacado]}\n")
        
        print("Porém a vítima é do tipo lutador também, então haverá contra-ataque")
        sleep(2.0)

        robots[idAtacado].atacar(robots[idAtacante])

        sleep(2.0)

        print("Atualização das informações após contra-ataque:")
        print(f"{robots[idAtacante]}\n\n")

    else:
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:")
        print(f"{robots[idAtacado]}\n\n")


def doctorHeal() -> None:
    listaIdDoctor = list()    
    for i in range(len(robots)):
        if robots[i].__class__ == medicalRobot:
            listaIdDoctor.append(i) # cria uma lista com todos os IDs dos robôs médicos

    print(f"{listaIdDoctor}\n")

    for i in range(0, len(robots)):
        if robots[i].precisaDeMedico():
            print(robots[i].precisaDeMedico(), "\n", robots[i])

            if(randint(0, 1) == 1): # 50% de chance de ser atendido ou não
                robots[choice(listaIdDoctor)].curar(robots[i]) # choice sorteia um valor aleatório da lista
                print("\nFoi 1\nCurado com sucesso porra\n")
            else:
                print(f"\nFoi zero\n")
        else:   
            print("\nNenhum robô precisa de médico")


if __name__ == "__main__":
    robots = list()
    
    m = Robot("l")
    m.vida = 0.01
    a = fighterRobot('trot')
    b = medicalRobot('saosao')
    robots.append(m)
    robots.append(a)
    robots.append(b)
    
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    while(True):
        print("MENU")
        print("1 - Criar robôs")
        print("2 - Listar robôs existentes")
        print("3 - Casamento de robôs (gera um filho robô)")
        print("4 - Luta")
        print("0 - Sair do programa")

        menu = int(input("\nDigite o número da operação que deseja realizar: "))

        if menu == 1:
            criaRobo()
        elif menu == 2:
            if system() == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
            listaRobot()
        elif menu == 3:
            casamentoRobot()
        elif menu == 4:
            lutaRobot()
        elif menu == 0:
            break
        elif menu == 5:
            doctorHeal()
