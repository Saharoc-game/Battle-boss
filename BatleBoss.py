import random
print("Привет, игрок. Ты играешь в игру Batle Boss. ")
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
list_mag_hp = [50, 55, 60, 65, 70]
magia_mag_boss = 6
list_voi_hp = [60, 65, 70, 75, 80]
magia_voi_boss = random.randint(2, 3)
list_ob_hp = [50, 55, 60]
magia_ob_boss = random.randint(3, 4)
hp_igrok = 20
max_hp_igrok = 20
magia_igrok = 1000
max_magia_igrok = 5
money = 3
raynd = 0
kol_boss = 0
boss = random.randint(0, 2)

if boss == 0 :
    hp_boss = random.choice(list_mag_hp)
    magia_boss = magia_mag_boss
    print("Вам попался босс-маг")
elif boss == 1 :
    hp_boss = random.choice(list_voi_hp)
    magia_boss = magia_voi_boss
    print("Вам попался босс-воин")
else :
    hp_boss = random.choice(list_ob_hp)
    magia_boss = magia_ob_boss
    print("Вам попался обычный босс")
max_hp_boss = hp_boss - 5
str_1 = "0"
print("Ваше здоровье ",hp_igrok,". Ваша магия ",magia_igrok,". Ваши деньги ", money )
print("Здоровье босса ",hp_boss,". Магия босса ",magia_boss,".")
print("1 чтобы атакавать. 2 чтобы восполнить здоровье. 3 чтобы восполнить магию. 4 чтобы открыть инвентарь. 0 чтобы пропустить ход.")
while (hp_igrok > 0):

# убийство босса + характеристики
    if hp_boss <= 0 :
        kol_boss = kol_boss + 1
        boss = random.randint(0, 2)
        if boss == 0 :
            hp_boss = random.choice(list_mag_hp)
            magia_boss = magia_mag_boss
            print("Вам попался босс-маг")
        elif boss == 1 :
            hp_boss = random.choice(list_voi_hp)
            magia_boss = magia_voi_boss
            print("Вам попался босс-воин")
        else :
            hp_boss = random.choice(list_ob_hp)
            magia_boss = magia_ob_boss
            print("Вам попался обычный босс")
        hp_igrok = hp_igrok + 5
        magia_igrok = magia_igrok + 1
        money = money + 3
        max_hp_igrok = max_hp_igrok + 5
        max_magia_igrok = max_magia_igrok + 1
        sa = random.randint(0,1)
        if item_sword == 3 :
            if item_armor == 3 :
                sa = 4
        if sa == 0 :
            item_sword = item_sword + 1
            x = random.randint(5, 23) + kol_boss
            inventory_sword.append(x)
            print("Вы нашли меч и его урон ", x)
        else :
            item_armor = item_armor + 1
            x = random.randint(1, 50)
            inventory_armor.append(x)
            print("Вы нашли броню и её защита ",x,"%")
        print("Поздравлю, игрок! Вы смогли победить босса под номером ",kol_boss)
        print("Ваша максимальное здоровье теперь",max_hp_igrok," Максимальное количество магии",max_magia_igrok)
        print("Магия увеличена на 1, здоровье на 5. Также вы нашли 3 монеты!")
        print("Ваше здоровье ",hp_igrok,". Ваша магия ",magia_igrok,". Ваши деньги ", money )
        print("Здоровье босса ",hp_boss,". Магия босса ",magia_boss,". Этот босс бьет сильнее предыдущего на 1 урон.")
        max_hp_boss = hp_boss - 5
    hod_igroka = 9
    print("Сейчас ",raynd, "раунд") 
# защита от дураков (цифры)
    while (hod_igroka >= 6)and (hod_igroka >= 0) :
        hod_igroka = int(input("Ваш ход от 0 до 5\n"))

# лечение игрока
    if (hod_igroka == 2) and (magia_igrok > 0) :
        print("Вы восполнили здоровье. Но потратили магию")
        hp_igrok = hp_igrok  + (10 + kol_boss)
        if (hp_igrok > max_hp_igrok):
            hp_igrok = max_hp_igrok 
        magia_igrok = magia_igrok - 1

# восполнение магии игрока
    if (hod_igroka == 3) and (money > 0 ):
        print("Вы восполнили магию. Но потратили деньги")
        magia_igrok =  magia_igrok + 3  
        money = money - 1
        if (magia_igrok > max_magia_igrok) :
            magia_igrok = max_magia_igrok
# удар игрока  
    if hod_igroka == 1 :
        str_i = input("1 чтобы нанести обычный удар. 2 чтобы нанести СУПЕР удар ")
        ataka = int(str_i)
        if (ataka == 2)and (magia_igrok > 1):
           igrok_uron = random.randint(10, 15)
           hp_boss = hp_boss - igrok_uron
           if (sword == 1) or (sword == 2) or (sword == 3):
                hp_boss = hp_boss - yron_sword
           magia_igrok = magia_igrok - 2
           print ("Вы нанесли боссу урона - ",igrok_uron + yron_sword,". Но потратили магию")
        else :
            if random.randint(0, 3) == 0 :
                print ("Босс поставил блок")
            else:
                igrok_uron = random.randint(1, 10)
                hp_boss = hp_boss - igrok_uron
                if item_sword > 1 :
                    hp_boss = hp_boss - yron_sword
                print ("Вы нанесли боссу урона - ",igrok_uron + yron_sword)
# инвентарь
    if hod_igroka == 4 :
        ans = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню"))
        if ans==1 :
            if item_sword > 0 :
                if item_sword == 1 :
                    print(inventory_sword[0]," первый меч")
                    print("Выберите меч ")
                    sword = int(input())
                elif item_sword == 2 :
                    print(inventory_sword[0]," первый меч")
                    print(inventory_sword[1]," второй меч")
                    print("Выберите меч ")
                    sword = int(input())
                else :
                    print(inventory_sword[0]," первый меч")
                    print(inventory_sword[1]," второй меч")
                    print(inventory_sword[2]," третий меч")
                    print("Выберите меч ")
                    sword = int(input())
            if sword == 1 :
                yron_sword = inventory_sword[0]
            elif sword == 2 :
                yron_sword = inventory_sword[1]
            else :
                yron_sword = inventory_sword[2]
        else :
            if item_armor > 0 :
                if item_armor == 1 :
                    print(inventory_armor[0]," первая броня")
                    print("Выберите броню ")
                    armor = int(input())
                elif item_armor == 2 :
                    print(inventory_armor[0]," первая броня")
                    print(inventory_armor[1]," вторая броня")
                    print("Выберите броню ")
                    armor = int(input())
                else :
                    print(inventory_armor[0]," первая броня")
                    print(inventory_armor[1]," вторая броня")
                    print(inventory_armor[2]," третяя броня")
                    print("Выберите броню ")
                    armor = int(input())
            if armor == 1 :
                zach_armor = inventory_armor[0]
            elif armor == 2 :
                zach_armor = inventory_armor[1]
            else :
                zach_armor = inventory_armor[2]



# продажа
    if hod_igroka == 5 :
        sora = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню"))
        if sora==1 :
            if item_sword == 1 :
                print(inventory_sword[0]," первый меч")
                print("Выберите меч ")
                sell = int(input())
            elif item_sword == 2 :
                print(inventory_sword[0]," первый меч")
                print(inventory_sword[1]," второй меч")
                print("Выберите меч ")
                sell = int(input())
            else :
                print(inventory_sword[0]," первый меч")
                print(inventory_sword[1]," второй меч")
                print(inventory_sword[2]," третий меч")
                print("Выберите меч ")
                sell = int(input())

            if sell == 1 :
                yron_sword = inventory_sword[0]
                money = money + yron_sword // 5 
                del inventory_sword[0]
                print("Вы продали меч, и получили ",yron_sword // 5," монет")
                yron_sword = 0
                item_sword = item_sword - 1
            elif sell == 2 :
                yron_sword = inventory_sword[1]
                money = money + yron_sword // 5
                del inventory_sword[1]
                print("Вы продали меч, и получили ",yron_sword // 5," монет")
                yron_sword = 0
                item_sword = item_sword - 1
            else :
                yron_sword = inventory_sword[2]
                money = money + yron_sword // 5
                del inventory_sword[2]
                print("Вы продали меч, и получили ",yron_sword // 5," монет")
                yron_sword = 0
                item_sword = item_sword - 1
        else :
            if item_armor == 1 :
                print(inventory_armor[0]," первая броня")
                print("Выберите броню ")
                sell = int(input())
            elif item_armor == 2 :
                print(inventory_armor[0]," первая броня")
                print(inventory_armor[1]," вторая броня")
                print("Выберите броню ")
                sell = int(input())
            else :
                print(inventory_armor[0]," первая броня")
                print(inventory_armor[1]," вторая броня")
                print(inventory_armor[2]," третяя броня")
                print("Выберите броню ")
                sell = int(input())
            if sell == 1 :
                zach_armor = inventory_armor[0]
                money = money + zach_armor//20
                del inventory_armor[0]
                print("Вы продали броню, и получили ",zach_armor//20," монет")
                zach_armor = 0
                item_armor = item_armor - 1
            elif sell == 2 :
                zach_armor = inventory_armor[1]
                money = money + zach_armor//20
                del inventory_armor[1]
                print("вы продали броню, и получили ",zach_armor//20," монет")
                zach_armor = 0
                item_armor = item_armor - 1
            else :
                zach_armor = inventory_armor[2]
                money = money + zach_armor//20
                del inventory_armor[2]
                print("вы продали броню, и получили ",zach_armor//20," монет")
                zach_armor = 0
                item_armor = item_armor - 1
       
           
# удар или лечение босса
    if (hp_boss > 0) :   
        if (hp_boss < max_hp_boss) and (magia_boss > 0):
            if random.randint(0, 1) == 0 :
                hp_boss = hp_boss + 5
                magia_boss = magia_boss - 1
                print("Босс лечится")
            else :
                boss_uron = random.randint(0, 5) 
                hp_igrok = (hp_igrok - (boss_uron - boss_uron * (zach_armor/100)) - kol_boss)//1
                print("Босс нанёс вам урон - ",((boss_uron - boss_uron * (zach_armor/100)) + kol_boss))
        else :
            boss_uron = random.randint(0, 5) 
            hp_igrok = (hp_igrok - (boss_uron - boss_uron * (zach_armor/100)) - kol_boss)//1
            print("Босс нанёс вам урон - ",((boss_uron - boss_uron * (zach_armor/100)) + kol_boss)//1)
    
    print("Ваше здоровье ",hp_igrok,". Ваша магия ",magia_igrok,". Ваши деньги ", money )
    print("Здоровье босса ",hp_boss,". Магия босса ",magia_boss,".") 
    raynd = raynd + 1
                        
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
        
# Проверка, ПРа