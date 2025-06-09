import random


class Ring():

    def __init__(self, heal=None, cost=None, name="Кольцо регенерации", 
                 description="Красивое железное кольцо с зелёным камнем", 
                 weight=0.5):
        self.heal = random.randint(1,3) if heal is None else heal
        self.cost = self.heal + 1 if cost is None else cost
        self.name = name
        self.description = description
        self.weight = weight
        self.type = "ring"

    def create(self):
        x = {"type": self.type,
            "cost": self.cost,
            "heal": self.heal,
            "name": self.name,
            "description": self.description,
            "weight": self.weight}
        return x
