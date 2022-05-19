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

    print(f"\nCasamento realizado com sucesso. O robô gerado tem nome: {listaRobots[idParceiro1].nome}-{listaRobots[idParceiro2].nome}")

def lutaRobot() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

    print("===== BATALHA =====")
    print("Chegou a hora da batalha!!\n")
    sleep(2.0)

    for i in range(len(listaRobots)):
        if listaRobots[i].__class__ == fighterRobot:
            print(f"ID = {i}\n{listaRobots[i]}")

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
 
    listaRobots[idAtacante].atacar(listaRobots[idAtacado])

    if listaRobots[idAtacado].__class__ == fighterRobot: # se o robô que foi atacado for lutador também
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:")
        print(f"{listaRobots[idAtacado]}\n")
        
        print("Porém a vítima é do tipo lutador também, então haverá contra-ataque")
        sleep(2.0)

        listaRobots[idAtacado].atacar(listaRobots[idAtacante])

        sleep(2.0)

        print("Atualização das informações após contra-ataque:")
        print(f"{listaRobots[idAtacante]}\n\n")

        sleep(2.0)
    else:
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:")
        print(f"{listaRobots[idAtacado]}\n\n")

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

        menu = int(input("\nDigite o número da operação que deseja realizar: "))

        if menu == 1:
            criaRobo()
        elif menu == 2:
            listaRobot()
            if system() == 'Windows':
                os.system("cls")
            else:
                os.system("clear")

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
