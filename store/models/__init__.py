# models/__init__.py

# Definição da classe de modelo Product
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Description: {self.description}, Price: {self.price}"
