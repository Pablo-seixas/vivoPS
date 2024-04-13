# core/__init__.py

# Definição da classe principal CoreApp
class CoreApp:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name} Core Application")


# Função auxiliar para calcular a média de uma lista de números
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Função auxiliar para verificar se um número é primo
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
