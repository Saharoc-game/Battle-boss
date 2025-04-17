import random

print("Привет, игрок. Ты играешь в игру Batle Boss.")
x = ''
sell = 0
sword = 0
armor = 0
yron_sword = 0
zach_armor = 0
inventory_sword = []
item_sword = 0
inventory_armor = []
item_armor = 0

hp_igrok = 20
max_hp_igrok = 20
magia_igrok = 5
max_magia_igrok = 5
money = 3
raynd = 0
kol_boss = 0

class Boss: # Класс Босс

    def __init__(self): # Задаём параметры
        self.hp = random.choice([50, 55, 60])
        self.magic = random.randint(3, 4)
        self.hp_max = self.hp

    def attack(self, kol_boss, zach_armor): # Атака Босса
        x = random.randint(0, 5)
        self.damage = ((x - x * (zach_armor / 100)) + kol_boss) // 1
        print("Босс нанёс вам урон - ", ((self.damage - self.damage * (zach_armor / 100)) + kol_boss) // 1)
        return self.damage  # Возвращаем урон

    def health_add(self): # Лечение Босса
        self.hp += 10
        print("Босс лечится")

B1 = Boss() # Создаём Босса

def drop_item_sword(kol_boss): # Выдача случайного меча
    x = random.randint(5, 23) + kol_boss
    print("Вы нашли меч и его урон ", x)
    return x

def drop_item_armor(kol_boss) : # Выдача случайной брони
    x = random.randint(1, 50)
    print("Вы нашли броню и её защита ", x, "%")
    return x

# Инициализация переменных босса
hp_boss = B1.hp
magia_boss = B1.magic

print("Ваше здоровье ", hp_igrok, ". Ваша магия ", magia_igrok, ". Ваши деньги ", money)
print("Здоровье босса ", B1.hp, ". Магия босса ", B1.magic, ".")
print("1 чтобы атаковать. 2 чтобы восполнить здоровье. 3 чтобы восполнить магию. 4 чтобы открыть инвентарь. 0 чтобы пропустить ход.")

while hp_igrok > 0:

    if B1.hp <= 0:
        kol_boss += 1

        # Улучшения характеристик

        hp_igrok += 5
        magia_igrok += 1
        money += 3
        max_hp_igrok += 5
        max_magia_igrok += 1


        # Выдача предметов

        if item_armor < 3 or item_sword < 3 :
            x = random.randint(0, 1)

            if x == 0 and item_armor < 3: # Выдача брони
                inventory_armor.append(drop_item_armor(kol_boss))
                item_armor += 1

            if x == 1 and item_sword < 3 : # Выдача меча
                item_sword += 1
                inventory_sword.append(drop_item_sword(kol_boss))

        print("Поздравлю, игрок! Вы смогли победить босса под номером ", kol_boss)
        print("Ваша максимальное здоровье теперь", max_hp_igrok, " Максимальное количество магии", max_magia_igrok)
        print("Магия увеличена на 1, здоровье на 5. Также вы нашли 3 монеты!")
        print("Ваше здоровье ", hp_igrok, ". Ваша магия ", magia_igrok, ". Ваши деньги ", money)
        print("Здоровье босса ", B1.hp, ". Магия босса ", B1.magic, ". Этот босс бьет сильнее предыдущего на 1 урон.")
        
        B1 = Boss() # Создаём нового босса

    hod_igroka = -1  # Инициализация переменной для хода игрока
    print("Сейчас ", raynd, "раунд")

    # Защита от дураков (цифры)
    while hod_igroka < 0 or hod_igroka > 5:
        try:
            hod_igroka = int(input("Ваш ход от 0 до 5\n"))
        except ValueError:
            print("Пожалуйста, введите число от 0 до 5.")

    # Лечение игрока
    if hod_igroka == 2 and magia_igrok > 0:
        print("Вы восполнили здоровье. Но потратили магию")
        hp_igrok += (10 + kol_boss)
        if hp_igrok > max_hp_igrok:
            hp_igrok = max_hp_igrok
        magia_igrok -= 1

    # Восполнение магии игрока
    if hod_igroka == 3 and money > 0:
        print("Вы восполнили магию. Но потратили деньги")
        magia_igrok += 3
        money -= 1
        if magia_igrok > max_magia_igrok:
            magia_igrok = max_magia_igrok

    # Удар игрока
    if hod_igroka == 1:
        str_i = input("1 чтобы нанести обычный удар. 2 чтобы нанести СУПЕР удар ")
        ataka = int(str_i)

        if ataka == 2 and magia_igrok > 1: # Супер удар
            igrok_uron = random.randint(10, 15)
            B1.hp -= (igrok_uron + yron_sword)
            magia_igrok -= 2
            print("Вы нанесли боссу урона - ", igrok_uron+yron_sword)

        else: # Обычный удар
            if random.randint(0, 3) == 0:
                print("Босс поставил блок")
            else:
                igrok_uron = random.randint(1, 10)
                B1.hp -= (igrok_uron + yron_sword)
                print("Вы нанесли боссу урона - ", igrok_uron+yron_sword)

    # Инвентарь
    if hod_igroka == 4:
        ans = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню "))

        # Мечи

        if ans == 1:
            if item_sword > 0:
                for i in range(item_sword):
                    print(inventory_sword[i], f"{i + 1} меч")
                sword = int(input("Выберите меч "))
                if sword <= item_sword:
                    yron_sword = inventory_sword[sword - 1]

        # Броня

        else:
            if item_armor > 0:
                for i in range(item_armor):
                    print(inventory_armor[i], f"{i + 1} броня")
                armor = int(input("Выберите броню "))
                if armor <= item_armor:
                    zach_armor = inventory_armor[armor - 1]

    # Продажа

    if hod_igroka == 5:
        sora = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню"))

        if sora == 1:

            if item_sword > 0: # Мечи
                for i in range(item_sword):
                    print(inventory_sword[i], f"{i + 1} меч")
                sell = int(input("Выберите меч "))
                if sell <= item_sword:
                    yron_sword = inventory_sword[sell - 1]
                    money += yron_sword // 5
                    del inventory_sword[sell - 1]
                    item_sword -= 1
                    print("Вы продали меч, и получили ", yron_sword // 5, " монет")
                    yron_sword = 0

        else:

            if item_armor > 0: # Броня
                for i in range(item_armor):
                    print(inventory_armor[i], f"{i + 1} броня")
                sell = int(input("Выберите броню "))
                if sell <= item_armor:
                    zach_armor = inventory_armor[sell - 1]
                    money += zach_armor // 20
                    del inventory_armor[sell - 1]
                    item_armor -= 1
                    print("Вы продали броню, и получили ", zach_armor // 20, " монет")
                    zach_armor = 0

    # Удар или лечение босса
    if hp_boss > 0:
        if hp_boss < B1.hp_max and magia_boss > 0:
            if random.randint(0, 1) == 0:
                B1.health_add()  # Вызов метода лечения босса
            else:
                hp_igrok -= B1.attack(kol_boss, zach_armor)
        else:
            hp_igrok -= B1.attack(kol_boss, zach_armor)

    print("Ваше здоровье ",hp_igrok,". Ваша магия ",magia_igrok,". Ваши деньги ", money )
    print("Здоровье босса ",B1.hp,". Магия босса ",B1.magic,".") 
    raynd = raynd + 1

# Проигрышь игрока, записываем рекорд

else :
    print("Вы погибли! Но вы смогли убить ",kol_boss," боссов!")
    f = open("BatleBossrecords.txt", "r+")
    last_line = int(f.readlines()[-1])
    print(last_line)
    if last_line < raynd :
        x = str(raynd)
        f.write(x)
        print("Вы поставили новый рекорд: ",x, " раундов")
    else :
        print("Рекорд: ",last_line, " раундов")
    f.close()
