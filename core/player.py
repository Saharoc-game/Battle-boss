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
        self.inventory = inv.Inventory() # Создаём инвентарь
        self.skill = 0
        self.buff = 0
        self.super_punch = "Супер удар" # Супер удар
        self.crit = 0 
        self.effects = []
        self.advantage = 0
        self.name_ability = None # Способность

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
    
    def attack(self): # Когда игрок атакует
        x = get_valid_int_input(
            "[blue]1[/blue] чтобы нанести обычный удар.\n[blue]2[/blue] чтобы нанести СУПЕР удар.\n[blue]3[/blue] чтобы использовать способность ",
            [1, 2, 3]
        )       # Получаем что хочет сделать игрок

        if x == 2 and self.magic >=2:  # Супер удар
            if self.buff > 0 :
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
            print(f"Вы использовали [cyan]{self.super_punch}[/cyan] Нанесли боссу урона - [red]{total_damage}[/red]")
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
        
        else: # Способности
            ability_result = self.player_abilities()
            if "damage" in ability_result:
                return ability_result["damage"]  # Вернуть урон
            elif "buff" in ability_result:
                self.buff += ability_result["buff"]  # Применить бафф
                return 0 
            elif "self_damage" in ability_result:
                self.hp -= ability_result["self_damage"]  # Потеря HP
                return 0 
            else : # Если не хватает магии
                print(f"У вас недочтаточно магии для способности [yellow]{self.name_ability}[/yellow]!")
                return 0
            
    def player_choose_item(self) : # Экипируем предмет
        choose = self.inventory.choose_item() # Получаем предмет, который экипировал игрок

        if 'sword_damage' in choose: # Если меч
            self.sword_damage = choose['sword_damage']

        if 'armor_defence' in choose: # Если броня
            self.armor_defense = choose['armor_defence']
     
    def player_abilites(self) : # Способность
        """Просто пустышка. Так как у всех подклассов игроков разные способности"""
        print("У вас нет особых способностей.")
        pass

    def effect_update(self) : # Обновляем все эффекты
        for effect in self.effects[:]:  
            effect.apply(self)
            if not effect.update():
                self.effects.remove(effect)
        if self.inventory.mass > 10 : # Если вес всех предметов больше 10, добавляем эффект перевеса
            Adv = AdvantageEffect()
            self.add_effect(Adv)

    def add_effect(self, effect): # Добавляем жффект
        self.effects.append(effect)

    def has_effect(self, effect_type): # Проверяем есть ли у игрока эффект
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
        self.super_punch = "Громовой удар" #Название супер удара
        self.name_ability = 'Сердце Бури' # Название способности

    def player_abilities (self) : # Способность
        if self.magic >= 2 :
            self.magic -= 2
            self.buff = 2
            print(f"Вы использовали способность [yellow]{self.name_ability}[/yellow]. Ваш урон увеличен на [blue]2[/blue] удара.")
            return {"buff": 2}  # Возвращаем данные об усилении
        else :
            return None

class PlayerWiz (Player): #Маг

    def __init__(self):
        super().__init__()
        self.magic = 7
        self.max_magic = self.magic
        self.skill = 2
        self.super_punch = "Водяной хлыст" #Название супер удара
        self.name_ability = 'Аэромантия' # Название способности

    def player_abilities (self) : # Спосбность
        if self.magic >= 2 :
            self.magic -= 2
            total_damage = 20
            print(f"Вы использовали заклинание [yellow]{self.name_ability}[/yellow]. Нанесли боссу урона - [red]{total_damage}[/red]")
            return {"damage": total_damage}  # Возвращаем урон
        else :
            return None            

class PlayerFort (Player): #Везунчик

    def __init__(self):
        super().__init__()
        self.crit = 1
        self.skill = 3
        self.super_punch = "Счастливый удар" #Название супер удар
        self.name_ability = 'Смертельная удача' # Название способности

    def player_abilities (self) : # Способность
        if self.magic >= 2 :
            self.magic -= 2
            chance = random.randint(1, 2)
            if chance == 1:
                total_damage = 20
                print(f"Вы использовали способность [yellow]{self.name_ability}[yellow]. Нанесли урона - [red]{total_damage}[/red]")
                return {"damage": total_damage} # Возвращаем данные об уроне по боссу
            else:
                self.hp -= 10
                print(f"Вы неудачно использовали способность [yellow]{self.name_ability}[yellow]. Нанесли себе урона - [red]10[/red]")
                return {"self_damage": 10} # Возвращаем данные об урону по себе
        else :
            return None
        
class PlayerBand(Player): #Разбойник
    def __init__(self):
        super().__init__()
        self.skill = 4
        self.ability_name = "Керсель"
        self.magic = 2
        self.max_magic = self.magic
        self.dodge = 1
    def player_abilities(self):
        if self.magic >= 1:
            self.hp -= 2
            total_damage = 20
            self.money += 2
            self.magic -= 2
            print(f"Вы использовали способность 'Джинада' и украли 2 монеты у босса. Нанесли урона - {total_damage}")
            return {"damage": total_damage}
        else:
            print("Маны нет")
            return None
        
def choose_playerclass() :
    x = get_valid_int_input(
        "Выберите свой класс.\n[blue]1[/blue] - класс Воин.\n[blue]2[/blue] - класс Маг.\n[blue]3[/blue] - класс Везунчик.\n[blue]4[/blue] - класс Разбойник.\n",
        [1, 2, 3, 4]
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
    elif x == 4:
        print("Вы выбрали класс разбойник")
        return PlayerBand() #Выбор класса разбойник
