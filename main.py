import os

from random import randint
from secrets import choice
from time import sleep
from platform import system

from robot.robot import Robot
from robot.robotMedical import medicalRobot
from robot.robotFighter import fighterRobot

def clear(): # função para limpar a tela
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def criaRobo() -> None:
    clear()

    print("Existem 3 tipos de robôs:")
    print("1 - Robô")
    print("2 - Robô Lutador")
    print("3 - Robô Médico")

    tipo = int(input("\nDigite o número do tipo do robô que deseja criar: "))

    # seleciona o tipo do robo, cria o nome e coloca na lista dos robôs
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

def listaRobot() -> None: # listar todos os robôs
    for i in range(len(robots)):
        print(f"ID: {i}\n{robots[i]}\n")

def casamentoRobot() -> None:
    clear()
    listaRobot()

    idParceiro1 = int(input("Digite o ID do primeiro robô para o casamento: "))
    idParceiro2 = int(input("Digite o ID do parceiro para o casamento: "))

    novoRobo = robots[idParceiro1] + robots[idParceiro2] # cria um novo robô com o nome definido dos pais
    robots.append(novoRobo) # coloca o novo robo na lista

    print(f"\nCasamento realizado com sucesso. O robô gerado tem nome: {novoRobo.nome}\n\n")

def lutaRobot() -> None:
    clear()

    print("===== BATALHA =====")
    print("Chegou a hora da batalha!!\n")
    sleep(2.0)

    for i in range(len(robots)):    # imprime só os fighterRobots
        if robots[i].__class__ == fighterRobot:
            print(f"ID = {i}\n{robots[i]}\n")

    print("Para atacar, o robô deve ser do tipo fighterRobot!")
    idAtacante = int(input("Escolha o ID de um robô lutador para atacar: ")) # guarda o id de quem vai atacar

    clear()

    print("===== BATALHA =====")
    print("Agora é a hora de escolher quem será a vítima, pode ser qualquer tipo de robô!\n")    
    sleep(2.0)

    listaRobot()
    idAtacado  = int(input("\nEscolha o ID de quem o lutador irá atacar: "))
 
    robots[idAtacante].atacar(robots[idAtacado]) # o atacante ataca

    if robots[idAtacado].__class__ == fighterRobot: # contra-ataque caso o atacado for lutador também
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:\n")
        print(f"{robots[idAtacado]}\n")
        
        print("\nPorém a vítima é do tipo lutador também, então haverá contra-ataque")
        sleep(2.0)

        robots[idAtacado].atacar(robots[idAtacante]) # contra-ataque

        sleep(2.0)

        print("\nAtualização das informações após contra-ataque:\n")
        print(f"{robots[idAtacante]}\n\n")
    else:   # caso não for do tipo lutador só mostra a atualização da vida
        print("\nA vítima foi atacada e aqui está a atualização da vida dela:\n")
        print(f"{robots[idAtacado]}\n\n")


def doctorHeal() -> None:
    listaIdDoctor = list()  # cria uma lista dos médicos vazia
    for i in range(len(robots)):
        if robots[i].__class__ == medicalRobot:
            listaIdDoctor.append(i) # cria uma lista com todos os IDs dos robôs médicos

    for i in range(0, len(robots)):
        if robots[i].precisaDeMedico(): # se o robô precisar de médico retorna NULL
            if(randint(0, 1) == 1):     # 50% de chance de ser atendido ou não
                robots[choice(listaIdDoctor)].curar(robots[i]) # choice sorteia um robô aleatório da 


if __name__ == "__main__":
    robots = list()
    
    m = Robot("Rob")
    a = fighterRobot('Falcon')
    b = medicalRobot('Saosao')
    robots.append(m)
    robots.append(a)
    robots.append(b)
    
    clear()

    while(True):
        doctorHeal() # sempre verifica se um robô precisa ser curado e cura automaticamente

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
            clear()
            listaRobot()
        elif menu == 3:
            casamentoRobot()
        elif menu == 4:
            lutaRobot()
        elif menu == 0:
            break