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
        self.ability_name = "Супер удар"
        self.skill = 0
        self.buff = 0

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
                x = int(input("1 чтобы нанести обычный удар. 2 чтобы нанести СУПЕР удар. 3 чтобы использовать способность "))
                if x not in (1, 2, 3):
                    print("Пожалуйста, введите 1 или 2")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите число")
                
        if x == 2 and self.magic >=2:  # Супер удар
            if self.buff >0:
                self.buff -=1
                self.magic -=2
                igrok_uron = random.randint(20,21)
            else:
                igrok_uron = random.randint(10,15)
                self.magic -= 2
            total_damage = igrok_uron + self.sword_damage
            print(f"Вы использовали" , self.ability_name, f"Нанесли боссу урона - {total_damage}")
            return total_damage
        elif x == 1:  # Обычный удар
            if random.randint(0, 3) == 0 and self.buff == 0:
                print("Босс поставил блок")
                return 0  # Возвращаем 0 вместо None
            elif self.buff >0:
                igrok_uron = random.randint(5, 15)
                self.buff -=1
            else:
                igrok_uron = random.randint(1,10)
            total_damage = igrok_uron + self.sword_damage
            print(f"Вы ударили обычным ударом. Нанесли боссу урона - {total_damage}")
            return total_damage
        else: #Способности
            if self.skill == 1 and self.magic >= 2: #Способность воина
                self.magic -= 2
                self.buff = 2
                print("Вы использовали способность Сердце Бури. Ваш урон увеличен на 2 удара.")
            elif self.skill == 2 and self.magic >= 2: #Способность мага
                self.magic -= 2
                total_damage = 20
                print(f"Вы использовали заклинание Аэромантия. Нанесли боссу урона - {total_damage}")
                return total_damage
        
class Warrior (Player): #Дядя Володя
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.hp_max = self.hp
        self.ability_name = "Штормовой удар"
        self.skill = 1

class Mage (Player): #Маг
    def __init__(self):
        super().__init__()
        self.magic = 7
        self.max_magic = self.magic
        self.ability_name = "Заклинание Пирокинетик"
        self.skill = 2
def random_player(): #Пока что, случайный класс игрока
    x = random.randint(0, 1)
    if x == 0:
        return Warrior()
    else:
        return Mage()
