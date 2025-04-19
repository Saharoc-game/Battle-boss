import random
import boss
import player
import inventory as inv

print("Привет, игрок. Ты играешь в игру Batle Boss.")
x = ''
sell = 0
sword = 0
armor = 0
item_armor = 0
magia_igrok = 5

P1 = player.Player()

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
        money += 3
        P1.max_hp += 5
        P1.max_magic += 1

        # Выдача предметов

        if item_armor < 3 or item_sword < 3 :
            x = random.randint(0, 1)

            if x == 0 and item_armor < 3: # Выдача брони
                P1.inventory_armor.append(inv.drop_item_armor(P1.bosses_killed))
                item_armor += 1

            if x == 1 and item_sword < 3 : # Выдача меча
                item_sword += 1
                P1.inventory_swords.append(inv.drop_item_sword(P1.bosses_killed))

        print("Поздравлю, игрок! Вы смогли победить босса под номером ", P1.bosses_killed)
        print("Ваша максимальное здоровье теперь", P1.max_hp, " Максимальное количество магии", P1.max_magic)
        print("Магия увеличена на 1, здоровье на 5. Также вы нашли 3 монеты!")
        print("Ваше здоровье ", P1.hp, ". Ваша магия ", P1.magic, ". Ваши деньги ", money)
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