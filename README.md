# Projeto de Jogo de Robôs 

<p style="text-align: center;">  
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=Python&message=3.8&color=blue&style=for-the-badge&logo=python"/>
</p> 

## Tópicos

:small_blue_diamond: [Descrição do Projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-Requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação)

:small_blue_diamond: [Executando o programa](#executando-o-programa)

## Descrição do Projeto

<p style="text-align: justify;">
  Projeto de um jogo de robôs desenvolvido para obtenção de nota no componente de Programação Orientada a Objetos, implementado em python.
</p>

## Funcionalidades

:heavy_check_mark: Classes robô, robô-lutador e robô-médico

:heavy_check_mark: Criação dos robôs

:heavy_check_mark: Listagem dos robôs

:heavy_check_mark: Casamento de robôs

:heavy_check_mark: Batalha entre robôs

## Pré-Requisitos

:warning: [Python 3.x](https://www.python.org/)

## Como rodar a aplicação

Se não possuir o Python instalado, instale, no Linux, com o comando no terminal:

```
sudo apt-get install python
```
Para instalação no Windows, consulte [aqui](https://python.org.br/instalacao-windows/).

No terminal, clone o projeto:

```
git clone https://github.com/pedrodicati/Projeto-Robo-POO.git
```
Após clonado, execute o programa com o comando:

```
python main.py
```
## Executando o programa

Ao executar o [main.py](main.py), irá para o menu:

```
MENU
1 - Criar robôs
2 - Listar robôs existentes
3 - Casamento de robôs (gera um filho robô)
4 - Luta
0 - Sair do programa

Digite o número da operação que deseja realizar: 
```
Após será solicitado para que selecione a operação que deseja realizar.

- 1 - Criar robôs

Será solicitado que digite o número do tipo do robô que quer criar:
```
Existem 3 tipos de robôs:
1 - Robô
2 - Robô Lutador
3 - Robô Médico

Digite o número do tipo do robô que deseja criar: 
```
Em qualquer uma das opções será solicitado um nome para o robô e depois será criado.
```
Tipo escolhido: ROBÔ
Digite o nome do seu novo robô: Robo1 

Robô criado! Confira na lista para verificar suas informações
```

- 2 - Listar robôs existentes

Irá imprimir uma lista com os robôs existentes:
```
ID: 0
<class 'robot.robot.Robot'>
Nome do robô: Rob
Vida: 0.203

ID: 1
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: Falcon
Vida: 0.619
Poder = 0.800

ID: 2
<class 'robot.robotMedical.medicalRobot'>
Nome do robô: Saosao
Vida: 0.657
Poder de cura: 0.633
```

A representação de cada robô varia com seu tipo.
Para o tipo Robô, definida em [robot.py](/robot/robot.py):
```
ID: X
<class 'robot.robot.Robot'>
Nome do robô: "Nome"
Vida: float definido aleatoriamente
```
Para o tipo Robô Lutador, definido em [robotFighter.py](/robot/robotFighter.py):
```
ID: X
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: "Nome"
Vida: float definido aleatoriamente
Poder = float definido aleatoriamente
```
Para o tipo Robô Médico, definido em [robotMedical.py](/robot/robotMedical.py):
```0.633
ID: X
<class 'robot.robotMedical.medicalRobot'>
Nome do robô: "Nome"
Vida: float definido aleatoriamente
Poder de cura: float definido aleatoriamente
```

- 3 - Casamento de robôs (gera um filho robô)

Lista novamente os robôs e solicita o ID de dois robôs para gerar um filho robô.
```
ID: 0
<class 'robot.robot.Robot'>
Nome do robô: Rob
Vida: 0.299

ID: 1
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: Falcon
Vida: 0.710
Poder = 0.786

ID: 2
<class 'robot.robotMedical.medicalRobot'>
Nome do robô: Saosao
Vida: 0.366
Poder de cura: 0.558

Digite o ID do primeiro robô para o casamento: 0
Digite o ID do parceiro para o casamento: 1
```

Depois é gerado um filho novo com a junção do nome dos dois robôs selecionados.
```
Casamento realizado com sucesso. O robô gerado tem nome: Rob-Falcon
```

- 4 - Luta

Será impressa uma lista somente dos robôs lutadores e será solicitado o ID de quem irá atacar.
```
===== BATALHA =====
Chegou a hora da batalha!!

ID = 1
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: Falcon
Vida: 0.710
Poder = 0.786

ID = 4
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: RobTwo
Vida: 0.655
Poder = 0.350

Para atacar, o robô deve ser do tipo fighterRobot!
Escolha o ID de um robô lutador para atacar: 1
```

Após selecionar, será a vez de selecionar a vítima do ataque:
```
===== BATALHA =====
Agora é a hora de escolher quem será a vítima, pode ser qualquer tipo de robô!

ID: 0
<class 'robot.robot.Robot'>
Nome do robô: Rob
Vida: 0.622

ID: 1
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: Falcon
Vida: 0.710
Poder = 0.786

ID: 2
<class 'robot.robotMedical.medicalRobot'>
Nome do robô: Saosao
Vida: 0.366
Poder de cura: 0.558

ID: 3
<class 'robot.robot.Robot'>
Nome do robô: Rob-Falcon
Vida: 0.719

ID: 4
<class 'robot.robotFighter.fighterRobot'>
Nome do robô: RobTwo
Vida: 0.655
Poder = 0.350


Escolha o ID de quem o lutador irá atacar: 4
```
Caso o atacado seja do tipo lutador, existirá contra-ataque:
```
A vítima foi atacada e aqui está a atualização da vida dela:

<class 'robot.robotFighter.fighterRobot'>
Nome do robô: RobTwo
Vida: 0.140
Poder = 0.350

Porém a vítima é do tipo lutador também, então haverá contra-ataque

Atualização das informações após contra-ataque:

<class 'robot.robotFighter.fighterRobot'>
Nome do robô: Falcon
Vida: 0.461
Poder = 0.786
```

Caso seja um robô de outro tipo, somente será mostrada as atualizações da vítima.

A função dos médicos é curar. O atendimento e a cura são efetuados automaticamente a cada repetição.

- 0 - Sair

Encerra o programa