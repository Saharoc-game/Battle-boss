import random
class Inventory() :
    def __init__(self):
        self.inventory_swordss = []  
        self.inventory_armor = [] 

    def choose_item(self):
            x = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню "))
            # Мечи
            if x == 1 :
                if len(self.inventory_swordss) > 0:
                    for i in range(len(self.inventory_swordss)):
                        print(self.inventory_swordss[i], f"{i + 1} меч")
                    sword = int(input("Выберите меч "))
                    if sword <= len(self.inventory_swordss):
                        return self.inventory_swordss[sword - 1]

            # Броня
            else :
                if len(self.inventory_armor) > 0:
                    for i in range(len(self.inventory_armor)):
                        print(self.inventory_armor[i], f"{i + 1} броня")
                    armor = int(input("Выберите броню "))
                    if armor <= len(self.inventory_armor):
                        return self.inventory_armor[armor - 1]
    
    def sell_item(self):
        x = int(input("1 чтобы просмотреть мечи 2 чтобы просмотреть броню"))

        if x == 1:

            if len(self.inventory_swordss) > 0: # Мечи
                for i in range(len(self.inventory_swordss)):
                    print(self.inventory_swords[i], f"{i + 1} меч")
                sell = int(input("Выберите меч "))
                if sell <= len(self.inventory_swordss):
                    self.sword_damage = self.inventory_swords[sell - 1]
                    del self.inventory_swords[sell - 1]
                    print("Вы продали меч, и получили ", self.sword_damage // 5, " монет")
                    self.sword_damage = 0

        else:

            if len(self.inventory_armor) > 0: # Броня
                for i in range(len(self.inventory_armor)):
                    print(self.inventory_armor[i], f"{i + 1} броня")
                sell = int(input("Выберите броню "))
                if sell <= len(self.inventory_armor):
                    self.armor_defense = self.inventory_armor[sell - 1]
                    del self.inventory_armor[sell - 1]
                    print("Вы продали броню, и получили ", self.armor_defense // 20, " монет")
                    self.armor_defense = 0

    def drop_item_sword(self, bosses_killed): # Выдача случайного меча
        x = random.randint(5, 23) + bosses_killed
        print("Вы нашли меч и его урон ", x)
        return x

    def drop_item_armor(self, bosses_killed) : # Выдача случайной брони
        x = random.randint(1, 50)
        print("Вы нашли броню и её защита ", x, "%")
        return x
