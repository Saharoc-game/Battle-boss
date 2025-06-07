import random


class Sword() :

    def __init__(self, kolboss, damage=None, cost=None, name="Обычный меч", 
                 description="Простой, надежный меч с хорошим балансом и удобной рукоятью.", 
                 weight=2):
        self.damage = random.randint(5, 23) + kolboss if damage is None else damage
        self.cost = self.damage // 5 if cost is None else cost
        self.name = name
        self.description = description
        self.weight = weight
        self.type = "sword"
    
    def create(self) :
        x = {"type": self.type,
            "cost": self.cost, 
            "damage": self.damage, 
            "name": self.name, 
            "description": self.description ,
            "weight": self.weight}
        return x

