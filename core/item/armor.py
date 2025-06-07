import random


class Armor() :

    def __init__(self, defence=None, cost=None, name="Кожаная броня", 
                 description="Легкая, удобная, немного снижает урон.", 
                 weight=4.5):
        
        self.defence = random.randint(10, 50) if defence is None else defence
        self.cost = self.defence // 10 if cost is None else cost
        self.name = name
        self.description = description
        self.weight = weight
        self.type = "armor"
    
    def create(self) :
        x = {"type": self.type,
            "cost": self.cost, 
            "defence": self.defence, 
            "name": self.name, 
            "description": self.description ,
            "weight": self.weight}
        return x
