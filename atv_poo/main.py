# Classe Funcionario com encapsulamento no atributo de salário
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario  # Atributo privado, acessível só pela própria classe
    
    def get_salario(self):
        return self.__salario
    
    def aumentar_salario(self, aumento):
        self.__salario += aumento

# Classe Gerente que herda de Funcionario e adiciona um bônus ao salário
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus
    
    def get_salario(self):
        return super().get_salario() + self.bonus

# Código de teste
funcionario = Funcionario("João", "Assistente", 3000)
gerente = Gerente("Maria", "Gerente", 5000, 2000)

# Aumentar salário
funcionario.aumentar_salario(500)
gerente.aumentar_salario(1000)

# Exibir salários atualizados
print("Salário do Funcionário:", funcionario.get_salario())
print("Salário do Gerente:", gerente.get_salario())
