import random


class Sword() :

    def __init__(self, kolboss):
        self.damage = random.randint(5, 23) + kolboss
        self.cost = self.damage // 5
        self.name = "Обычный меч"
        self.description = "Простой, надежный меч с хорошим балансом и удобной рукоятью."
        self.weight = 2
        self.type = "sword"
    
    def create(self) :
        x = {"type": self.type,
            "cost": self.cost, 
            "damage": self.damage, 
            "name": self.name, 
            "description": self.description ,
            "weight": self.weight}
        return x

