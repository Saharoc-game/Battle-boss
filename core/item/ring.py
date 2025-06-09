import random


class Ring():
    def __init__(self):
        self.heal = random.randint(1,3)
        self.cost = self.heal+ 1
        self.name = "Кольцо регенерации"
        self.description = "Красивое железное кольцо с зелёным камнем"
        self.weight = 0.5
        self.type = "ring"
    def create(self):
        x = {"type": self.type,
            "cost": self.cost,
            "heal": self.effect,
            "name": self.name,
            "description": self.description,
            "weight": self.weight}
        return x
