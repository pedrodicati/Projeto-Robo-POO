class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        print("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")
    
    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1
    
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


pedro = Funcionario('Pedro', 'Gerente de Vendas', 50)
print(pedro.salario)