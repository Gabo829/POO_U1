class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

def hacer_hablar(animal):
    print(animal.hablar())

if __name__ == "__main__":
    animales = [Perro(), Gato()]
    for a in animales:
        hacer_hablar(a)
