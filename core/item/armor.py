import random


class Armor() :

    def __init__(self):
        self.defence = random.randint(10, 50)
        self.cost = self.defence // 10
        self.name = "Кожаная броня"
        self.description = "Легкая, удобная, немного снижает урон."
        self.weight = 4.5
        self.type = "armor"
    
    def create(self) :
        x = {"type": self.type,
            "cost": self.cost, 
            "defence": self.defence, 
            "name": self.name, 
            "description": self.description ,
            "weight": self.weight}
        return x
