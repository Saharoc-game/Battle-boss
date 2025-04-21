import random
class Boss: # Класс Босс

    def __init__(self): # Задаём параметры
        self.hp = int(random.choice([50, 55, 60]))
        self.magic = random.randint(3, 4)
        self.hp_max = self.hp

    def attack(self, bosses_killed, armor_defense): # Атака Босса
        x = random.randint(0, 5)
        self.damage = ((x - x * (armor_defense / 100)) + bosses_killed) // 1
        print("Босс нанёс вам урон - ", self.damage)
        return self.damage  # Возвращаем урон

    def health_add(self): # Лечение Босса
        self.magic -= 1
        self.hp += 10
        print("Босс лечится")

class BossWar (Boss) : # Класс Босс. Подкласс воин

    def __init__(self): # Задаём параметры
        super().__init__()
        self.hp = random.choice([60, 65, 70])
        self.hp_max = self.hp

class BossWiz (Boss) : # Класс Босс. Подкласс маг

    def __init__(self): # Задаём параметры
        super().__init__()
        self.magic = random.randint(6, 7)

        
def random_boss() : # Создание  случайного Босса
    x = random.randint(0, 1)
    if x == 0 :
        return BossWar() # Воин
    else :
        return BossWiz() # Маг