import os
from platform import platform, system
from robot import fighterRobot, medicalRobot, Robot
import main

# print(os.name)

# print(system())

listaRobots = list()
    
m = Robot("l")
a = fighterRobot('trot')
b = medicalRobot('saosao')
listaRobots.append(m)
listaRobots.append(a)
listaRobots.append(b)

for i in range(len(listaRobots)):
    print(listaRobots[i].__class__)

    if listaRobots[i].__class__ == Robot:
        print("DEU CERTO")