import random
from core import inventory as inv
class Player(): # Класс игрок
    def __init__(self):
        self.hp = 20
        self.max_hp = 20
        self.magic = 5
        self.money = 3
        self.max_magic = 5
        self.sword_damage = 0  
        self.armor_defense = 0    
        self.rounds = 0             
        self.bosses_killed = 0
        self.inventory = inv.Inventory()

    def healf(self) : # Лечение
        print("Вы восполнили здоровье. Но потратили магию")
        self.hp += (10 + self.bosses_killed)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.magic -= 1

    def magic_add(self) : # Добавление магии
        print("Вы восполнили магию. Но потратили деньги")
        self.magic += 3
        self.money -= 1
        if self.magic > self.max_magic:
            self.magic = self.max_magic
    
    def attack(self):
    while True:
        try:
            x = int(input("1 чтобы нанести обычный удар. 2 чтобы нанести СУПЕР удар "))
            if x not in (1, 2):
                print("Пожалуйста, введите 1 или 2")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число")

    if x == 2 and self.magic > 1:  # Супер удар
        igrok_uron = random.randint(10, 15)
        self.magic -= 2
        total_damage = igrok_uron + self.sword_damage
        print(f"Вы нанесли боссу урона - {total_damage}")
        return total_damage
    else:  # Обычный удар
        if random.randint(0, 3) == 0:
            print("Босс поставил блок")
            return 0  # Возвращаем 0 вместо None
        else:
            igrok_uron = random.randint(1, 10)
            total_damage = igrok_uron + self.sword_damage
            print(f"Вы нанесли боссу урона - {total_damage}")
            return total_damage 
