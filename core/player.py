import random
from rich import print

from core import inventory as inv
from utils.input_until import get_valid_int_input
from core.effect.advantage import AdvantageEffect


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
        self.skill = 0
        self.buff = 0
        self.ability_name = "Супер удар"
        self.crit = 0 
        self.effects = []
        self.advantage = 0

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
        x = get_valid_int_input(
            "[blue]1[/blue] чтобы нанести обычный удар.\n[blue]2[/blue] чтобы нанести СУПЕР удар.\n[blue]3[/blue] чтобы использовать способность ",
            [1, 2, 3]
        )       
        if x == 2 and self.magic >=2:  # Супер удар
            if self.buff >0:
                self.buff -=1
                self.magic -=2
                igrok_uron = random.randint(20,21)
            else:
                igrok_uron = random.randint(10,15)
                self.magic -= 2
            if self.advantage > 0 :
                total_damage = int((igrok_uron + self.sword_damage) - (igrok_uron + self.sword_damage*0.3))
            else :
                total_damage = igrok_uron + self.sword_damage
            print(f"Вы использовали [yellow]{self.ability_name}[/yellow] Нанесли боссу урона - [red]{total_damage}[/red]")
            return total_damage
    
        elif x == 1:  # Обычный удар
            if random.randint(0, 3) == 0 and self.buff == 0:
                print("Босс поставил блок")
                return 0  
            elif self.buff > 0:
                igrok_uron = random.randint(5, 15)
                self.buff -=1
            else:
                if self.crit == 1:
                    chance = random.randint(1,10)
                    if chance == 3:
                        igrok_uron = 12
                    else:
                        igrok_uron = random.randint(1,10)
                    chance = random.randint(1,100)
                    if chance == 42:
                        igrok_uron = 50
                else:
                    igrok_uron = random.randint(1,10)
            if self.advantage > 0 :
                total_damage = int((igrok_uron + self.sword_damage) - (igrok_uron + self.sword_damage*0.3))
            else :
                total_damage = igrok_uron + self.sword_damage
            print(f"Вы ударили обычным ударом. Нанесли боссу урона - [red]{total_damage}[/red]")
            return total_damage
        
        else: #Способности
            ability_result = self.player_abilities()
    
            if "damage" in ability_result:
                return ability_result["damage"]  # Вернуть урон
            if "buff" in ability_result:
                self.buff += ability_result["buff"]  # Применить бафф
                return 0 
            if "self_damage" in ability_result:
                self.hp -= ability_result["self_damage"]  # Потеря HP
                return 0 
            
    def player_choose_item(self) :
        choose = self.inventory.choose_item()
        if 'sword_damage' in choose:
            self.sword_damage = choose['sword_damage']

        if 'armor_defence' in choose:
            self.armor_defense = choose['armor_defence']
     
    def player_abilites(self) :
        print("У вас нет особых способностей.")
        pass

    def effect_update(self) :
        for effect in self.effects[:]:  
            effect.apply(self)
            if not effect.update():
                self.effects.remove(effect)
        if self.inventory.mass > 10 :
            Adv = AdvantageEffect()
            self.add_effect(Adv)

    def add_effect(self, effect):
        self.effects.append(effect)

    def has_effect(self, effect_type):
        for effect in self.effects:
            if isinstance(effect, effect_type):
                return True  # Найден нужный эффект
        return False  # Эффекта нет
                
                            
class PlayerWar (Player): #Воин
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.hp_max = self.hp
        self.skill = 1
        self.ability_name = "Громовой удар" #Название супер удара
    def player_abilities (self) :
        self.magic -= 2
        self.buff = 2
        print("Вы использовали способность [yellow]'Сердце Бури'[/yellow]. Ваш урон увеличен на [blue]2[/blue] удара.")
        return {"buff": 2}  # Возвращаем данные об усилении

class PlayerWiz (Player): #Маг
    def __init__(self):
        super().__init__()
        self.magic = 7
        self.max_magic = self.magic
        self.skill = 2
        self.ability_name = "Водяной хлыст" #Название супер удара

    def player_abilities (self) :
        self.magic -= 2
        total_damage = 20
        print(f"Вы использовали заклинание [yellow]'Аэромантия'[/yellow]. Нанесли боссу урона - [red]{total_damage}[/red]")
        return {"damage": total_damage}  # Возвращаем урон
                    

class PlayerFort (Player): #Везунчик
    def __init__(self):
        super().__init__()
        self.crit = 1
        self.skill = 3
        self.ability_name = "Счастливый удар" #Название супер удар

    def player_abilities (self) :
        self.magic -= 2
        chance = random.randint(1, 2)
        if chance == 1:
            total_damage = 20
            print(f"Вы использовали способность [yellow]'Смертельная удача'[yellow]. Нанесли урона - [red]{total_damage}[/red]")
            return {"damage": total_damage}
        else:
            self.hp -= 10
            print(f"Вы неудачно использовали способность [yellow]'Смертельная удача'[yellow]. Нанесли себе урона - [red]10[/red]")
            return {"self_damage": 10}
        
def choose_playerclass() :
    x = get_valid_int_input(
        "Выберите свой класс.\n[blue]1[/blue] - класс Воин.\n[blue]2[/blue] - класс Маг.\n[blue]3[/blue] - класс Везунчик.\n",
        [1, 2, 3]
    )
    if x == 1:
        print("Вы выбрали класс воин")
        return PlayerWar() #Выбор класса воин
    elif x == 2:
        print("Вы выбрали класс маг")
        return PlayerWiz() #Выбор класса маг
    elif x == 3:
        print("Вы выбрали класс везунчик")
        return PlayerFort() #Выбор класса везунчик