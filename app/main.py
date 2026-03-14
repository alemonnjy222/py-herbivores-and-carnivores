class Animal:
    alive = []

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
        if animal.health <= 0:
            animal.health = 0
        if animal in Animal.alive:
            Animal.alive.remove(animal)
print(Animal.alive)
