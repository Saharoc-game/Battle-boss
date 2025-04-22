import random
from core import boss 
from core import player
from core import inventory as inv

print("Привет, игрок. Ты играешь в игру Batle Boss.")
x = ''
sell = 0
sword = 0
armor = 0
magia_igrok = 5

P1 = player.Player() # Создаем Игрока

B1 = boss.random_boss() # Создание Босса

print("Ваше здоровье ", P1.hp, ". Ваша магия ", P1.magic, ". Ваши деньги ", P1.money)
print("Здоровье босса ", B1.hp, ". Магия босса ", B1.magic, ".")
print("1 чтобы атаковать. 2 чтобы восполнить здоровье. 3 чтобы восполнить магию. 4 чтобы открыть инвентарь. 5 чтобы продать предмет. 0 чтобы пропустить ход.")

while P1.hp > 0:

    if B1.hp <= 0:
        P1.bosses_killed += 1

        # Улучшения характеристик

        P1.hp += 5
        P1.magic += 1
        P1.max_hp += 5
        P1.max_magic += 1
        
        # Выдача предметов

        if len(P1.inventory.inventory_armor) < 3 or len(P1.inventory.inventory_swordss) < 3 :
            x = random.randint(0, 1)

            if x == 0 and len(P1.inventory.inventory_armor) < 3: # Выдача брони
                x = P1.inventory.drop_item_armor(P1.bosses_killed)
                P1.inventory.inventory_armor.append(x)

            if x == 1 and len(P1.inventory.inventory_swordss) < 3 : # Выдача меча
                x = P1.inventory.drop_item_sword(P1.bosses_killed)
                P1.inventory.inventory_swordss.append(x)

        print("Поздравлю, игрок! Вы смогли победить босса под номером ", P1.bosses_killed)
        print("Ваша максимальное здоровье теперь", P1.max_hp, " Максимальное количество магии", P1.max_magic)
        print("Магия увеличена на 1, здоровье на 5. Также вы нашли 3 монеты!")
        print("Ваше здоровье ", P1.hp, ". Ваша магия ", P1.magic, ". Ваши деньги ", P1.money)
        B1 = boss.random_boss() # Создание Босса
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
        P1.healf()

    # Восполнение магии игрока
    if hod_igroka == 3 and P1.money > 0:
        P1.magic_add()

    # Удар игрока
    if hod_igroka == 1:
        B1.hp -= P1.attack()

    # Инвентарь
    if hod_igroka == 4:
        P1.inventory.choose_item()

    # Продажа

    if hod_igroka == 5:
        print("Pofiksit potom")
      
    # Удар или лечение босса
    if B1.hp > 0:
        if B1.hp_max and B1.magic > 0:
            if random.randint(0, 1) == 0:
                B1.health_add()  # Вызов метода лечения босса
            else:
                P1.hp -= B1.attack(P1.bosses_killed, P1.armor_defense)
        else:
            P1.hp -= B1.attack(P1.bosses_killed, P1.armor_defense)


    print("Ваше здоровье ",P1.hp,". Ваша магия ",P1.magic,". Ваши деньги ", P1.money )
    print("Здоровье босса ",B1.hp,". Магия босса ",B1.magic,".") 
    P1.rounds = P1.rounds + 1

# Проигрыш игрока, записываем рекорд

else:
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
print("1")
