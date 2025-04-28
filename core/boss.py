import random
class Boss: # Класс Босс

    def __init__(self): # Задаём параметры
        self.hp = int(random.choice([50, 55, 60]))
        self.magic = random.randint(3, 4)
        self.hp_max = self.hp
        self.recharge_max = 10
        self.recharge = self.recharge_max
        self.name_ability = "Супер удар"
        self.vampiric = 0
        
    def attack(self, bosses_killed, armor_defense): # Атака Босса
        if self.recharge >= self.recharge_max :
            self.damage = random.randint(10, 15)
            if self.vampiric == 1:
                self.hp += 5
            print("Босс использует ", self.name_ability," и наносит - ", self.damage, " урона")
            self.recharge = 0
            return self.damage
        else :
            x = random.randint(0, 5)
            self.damage = int(x - x * (armor_defense / 100) + bosses_killed)
            if self.vampiric == 1:
                self.hp += 2
            print("Босс нанёс вам урон - ", self.damage)
            return self.damage  # Возвращаем урон

    def health_add(self): # Лечение Босса
        self.magic -= 1
        self.hp += 10
        print("Босс использовал заклинание <Исцеление>")
    
    def add_recharge(self) :
        self.recharge += 2.5
        print("Босс копит супер удар")

class BossWar (Boss) : # Класс Босс. Подкласс воин

    def __init__(self): # Задаём параметры
        super().__init__()
        self.hp = random.choice([60, 65, 70])
        self.hp_max = self.hp
        self.name_ability = "Гнев Титана"

class BossWiz (Boss) : # Класс Босс. Подкласс маг

    def __init__(self): # Задаём параметры
        super().__init__()
        self.magic = random.randint(6, 7)
        self.name_ability = "Пламя Затмений"

class BossArc (Boss): # Класс Босс. Подкласс лучник

    def __init__(self): # Задаём параметры
        super().__init__()
        self.hp = random.choice([40, 45, 50])
        self.hp_max = self.hp
        self.magic = random.randint(5,6)
        self.name_ability = "Дождь Призрачных Стрел"
"""
class BossVam (Boss): # Класс Босс. Покдласс вампир
    def __init__(self): # Задаём параметры
        super().__init__()
        self.hp = random.choice([50, 60, 65])
        self.hp_max = self.hp
        self.vampiric = 1
        self.name_ability = "Парализующий страх"
"""
        
def random_boss() : # Создание  случайного Босса
    x = random.randint(0, 2)
    if x == 0 :
        return BossWar() # Воин
    elif x == 1 :
        return BossWiz() # Маг
    else:
        return BossArc() # Лучник
    """"
    elif x == 3:
        return BossVam() # Вампир
    """
