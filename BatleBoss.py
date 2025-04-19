import random

print("Привет, игрок. Ты играешь в игру Batle Boss.")
x = ''
sell = 0
sword = 0
armor = 0
item_armor = 0
magia_igrok = 5

class Player:
    def __init__(self):
        self.hp = 20
        self.max_hp = 20
        self.magic = 5
        self.max_magic = 5
        self.money = 3
        self.sword_damage = 0  
        self.armor_defense = 0  
        self.inventory_swordss = []  
        self.inventory_armor = []   
        self.rounds = 0             
        self.bosses_killed = 0

    def healfh_add(self) :
        print("Вы восполнили здоровье. Но потратили магию")
        self.hp += (10 + self.bosses_killed)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.magic -= 1

    def magic_add(self) :
        print("Вы восполнили магию. Но потратили деньги")
        self.magic += 3
        money -= 1
        if self.magic > self.max_magic:
            self.magic = self.max_magic


P1 = Player()

class Boss: # Класс Босс

    def __init__(self): # Задаём параметры
        self.hp = random.choice([50, 55, 60])
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

def drop_item_sword(bosses_killed): # Выдача случайного меча
    x = random.randint(5, 23) + bosses_killed
    print("Вы нашли меч и его урон ", x)
    return x

def drop_item_armor(bosses_killed) : # Выдача случайной брони
    x = random.randint(1, 50)
    print("Вы нашли броню и её защита ", x, "%")
    return x

B1 = random_boss() # Создание Босса

# Инициализация переменных босса
hp_boss = B1.hp
magia_boss = B1.magic

print("Ваше здоровье ", P1.hp, ". Ваша магия ", P1.magic, ". Ваши деньги ", P1.money)
print("Здоровье босса ", B1.hp, ". Магия босса ", B1.magic, ".")
print("1 чтобы атаковать. 2 чтобы восполнить здоровье. 3 чтобы восполнить магию. 4 чтобы открыть инвентарь. 5 чтобы продать предмет. 0 чтобы пропустить ход.")

while P1.hp > 0:

    if B1.hp <= 0:
        P1.bosses_killed += 1

        # Улучшения характеристик

        P1.hp += 5
        P1.magic += 1
        money += 3
        P1.max_hp += 5
        max_magia_igrok += 1

        # Выдача предметов

        if item_armor < 3 or item_sword < 3 :
            x = random.randint(0, 1)

            if x == 0 and item_armor < 3: # Выдача брони
                P1.inventory_armor.append(drop_item_armor(P1.bosses_killed))
                item_armor += 1

            if x == 1 and item_sword < 3 : # Выдача меча
                item_sword += 1
                P1.inventory_swords.append(drop_item_sword(P1.bosses_killed))

        print("Поздравлю, игрок! Вы смогли победить босса под номером ", P1.bosses_killed)
        print("Ваша максимальное здоровье теперь", P1.max_hp, " Максимальное количество магии", max_magia_igrok)
        print("Магия увеличена на 1, здоровье на 5. Также вы нашли 3 монеты!")
        print("Ваше здоровье ", P1.hp, ". Ваша магия ", P1.magic, ". Ваши деньги ", money)
        B1 = random_boss() # Создание Босса
        print("Здоровье босса ", B1.hp, ". Магия босса ", B1.magic, ". Этот босс бьет сильнее предыдущего на 1 урон.")
        
    hod_igroka = -1  # Инициализация переменной для хода игрока
    print("Сейчас ", P1.rounds, "раунд")

    # Защита от дураков (цифры)
    while hod_igroka < 0 or hod_igroka > 5:
        try:
            hod_igroka = int(input("Ваш ход от 0 до 5\n"))
        except ValueError:
            print("Пожалуйста, введите число от 0 до 5.")

    # Лечение игрока
    if hod_igroka == 2 and P1.magic > 0:
        P1.healfh_add()

    # Восполнение магии игрока
    if hod_igroka == 3 and P1.money > 0:
        P1.magic_add()

    # Удар игрока
    if hod_igroka == 1:
        str_i = input("1 чтобы нанести обычный удар. 2 чтобы нанести СУПЕР удар ")
        ataka = int(str_i)

        if ataka == 2 and P1.magic > 1: # Супер удар
            igrok_uron = random.randint(10, 15)
            B1.hp -= (igrok_uron + P1.sword_damage)
            P1.magic -= 2
            print("Вы нанесли боссу урона - ", igrok_uron+ P1.sword_damage)

        else: # Обычный удар
            if random.randint(0, 3) == 0:
                print("Босс поставил блок")
            else:
                igrok_uron = random.randint(1, 10)
                B1.hp -= (igrok_uron + P1.sword_damage)
                print("Вы нанесли боссу урона - ", igrok_uron+P1.sword_damage)

    # Инвентарь
    if hod_igroka == 4:
        ans = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню "))

        # Мечи

        if ans == 1:
            if item_sword > 0:
                for i in range(item_sword):
                    print(P1.inventory_swords[i], f"{i + 1} меч")
                sword = int(input("Выберите меч "))
                if sword <= item_sword:
                    P1.sword_damage = P1.inventory_swords[sword - 1]

        # Броня

        else:
            if item_armor > 0:
                for i in range(item_armor):
                    print(P1.inventory_armor[i], f"{i + 1} броня")
                armor = int(input("Выберите броню "))
                if armor <= item_armor:
                    P1.armor_defense = P1.inventory_armor[armor - 1]

    # Продажа

    if hod_igroka == 5:
        sora = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню"))

        if sora == 1:

            if item_sword > 0: # Мечи
                for i in range(item_sword):
                    print(P1.inventory_swords[i], f"{i + 1} меч")
                sell = int(input("Выберите меч "))
                if sell <= item_sword:
                    P1.sword_damage = P1.inventory_swords[sell - 1]
                    money += P1.sword_damage // 5
                    del P1.inventory_swords[sell - 1]
                    item_sword -= 1
                    print("Вы продали меч, и получили ", P1.sword_damage // 5, " монет")
                    P1.sword_damage = 0

        else:

            if item_armor > 0: # Броня
                for i in range(item_armor):
                    print(P1.inventory_armor[i], f"{i + 1} броня")
                sell = int(input("Выберите броню "))
                if sell <= item_armor:
                    P1.armor_defense = P1.inventory_armor[sell - 1]
                    money += P1.armor_defense // 20
                    del P1.inventory_armor[sell - 1]
                    item_armor -= 1
                    print("Вы продали броню, и получили ", P1.armor_defense // 20, " монет")
                    P1.armor_defense = 0

    # Удар или лечение босса
    if hp_boss > 0:
        if hp_boss < B1.hp_max and magia_boss > 0:
            if random.randint(0, 1) == 0:
                B1.health_add()  # Вызов метода лечения босса
            else:
                P1.hp -= B1.attack(P1.bosses_killed, P1.armor_defense)
        else:
            P1.hp -= B1.attack(P1.bosses_killed, P1.armor_defense)


    print("Ваше здоровье ",P1.hp,". Ваша магия ",P1.magic,". Ваши деньги ", P1.money )
    print("Здоровье босса ",B1.hp,". Магия босса ",B1.magic,".") 
    P1.rounds = P1.rounds + 1

# Проигрышь игрока, записываем рекорд

else :
    print("Вы погибли! Но вы смогли убить ",P1.bosses_killed," боссов!")
    f = open("BatleBossrecords.txt", "r+")
    last_line = int(f.readlines()[-1])
    print(last_line)
    if last_line < P1.rounds :
        x = str(P1.rounds)
        f.write(x)
        print("Вы поставили новый рекорд: ",x, " раундов")
    else :
        print("Рекорд: ",last_line, " раундов")
    f.close()
input("")