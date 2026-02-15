class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print("Guau guau!")

class Gato(Animal):
        def maullar(self):
            print("Miau!")

if __name__ == "__main__":
    perro = Perro("Firulais")
    perro.comer()
    perro.ladrar()
