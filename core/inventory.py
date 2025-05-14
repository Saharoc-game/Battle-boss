import random

class Inventory:
    def __init__(self):

        self.inventory = {
            "swords": [],  # список мечей 
            "armor": []    # список брони 
        }

    def choose_item(self):
        x = int(input("Введите 1, чтобы просмотреть мечи, или 2, чтобы просмотреть броню: "))

        # Мечи
        if x == 1:
            swords = self.inventory.get("swords", [])
            if len(swords) > 0:
                for i, sword in enumerate(swords, start=1):
                    print(f"{i}: Меч с уроном {sword}")
                sword_choice = int(input("Выберите номер меча: "))
                if 1 <= sword_choice <= len(swords):
                    return swords[sword_choice - 1]
                else:
                    print("Неверный выбор!")
            else:
                print("У вас нет мечей.")
        
        elif x == 2:
            armor = self.inventory.get("armor", [])
            if len(armor) > 0:
                for i, piece in enumerate(armor, start=1):
                    print(f"{i}: Броня с защитой {piece}")
                armor_choice = int(input("Выберите номер брони: "))
                if 1 <= armor_choice <= len(armor):
                    return armor[armor_choice - 1]
                else:
                    print("Неверный выбор!")
            else:
                print("У вас нет брони.")
        
        else:
            print("Неверный выбор типа предмета.")

    def sell_item(self):
        x = int(input("Введите 1, чтобы продать меч, или 2, чтобы продать броню: "))
        
        # Мечи
        coins = 0
        if x == 1:
            swords = self.inventory.get("swords", [])
            if len(swords) > 0:
                for i, sword in enumerate(swords, start=1):
                    print(f"{i}: Меч с уроном {sword}")
                sell_choice = int(input("Выберите номер меча для продажи: "))
                if 1 <= sell_choice <= len(swords):
                    # Удаляем выбранный меч из списка методом pop, чтобы получить его значение.
                    sword_damage = swords.pop(sell_choice - 1)
                    coins = sword_damage // 5
                    print(f"Вы продали меч и получили {coins} монет.")
                else:
                    print("Неверный выбор!")
            else:
                print("У вас нет мечей.")
        
        # Обработка продажи брони
        elif x == 2:
            armor = self.inventory.get("armor", [])
            if len(armor) > 0:
                for i, piece in enumerate(armor, start=1):
                    print(f"{i}: Броня с защитой {piece}")
                sell_choice = int(input("Выберите номер брони для продажи: "))
                if 1 <= sell_choice <= len(armor):
                    armor_defense = armor.pop(sell_choice - 1)
                    coins = armor_defense // 20
                    print(f"Вы продали броню и получили {coins} монет.")
                else:
                    print("Неверный выбор!")
            else:
                print("У вас нет брони.")
        else:
            print("Неверный выбор типа предмета.")
        return coins

    def drop_item_sword(self, bosses_killed):
        # Выдаём случайный меч. Значение урона вычисляется случайно + бонус за убийство босса.
        x = random.randint(5, 23) + bosses_killed
        print("Вы нашли меч с уроном", x)
        # Добавляем этот меч в список мечей.
        self.inventory.setdefault("swords", []).append(x)

    def drop_item_armor(self, bosses_killed):
        # Выдаём случайную броню. Защита рассчитывается случайно.
        x = random.randint(1, 50)
        print("Вы нашли броню с защитой", x, "%")
        # Добавляем эту броню в список брони.
        self.inventory.setdefault("armor", []).append(x)
