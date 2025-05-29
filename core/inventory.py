import random
from core.item.sword import Sword
from core.item.armor import Armor

class Inventory:
    def __init__(self):

        self.max_ID = 0

        self.INVENTORY_STATS = {
            "swords": {"type": "sword",
                    "cost":3, 
                    "damage":5, 
                    "name": "Обычный меч", 
                    "description": "Простой, надежный меч с хорошим балансом и удобной рукоятью.",
                    "weight": 2
                    },

            "armor": {  "cost":3, 
                        "defense": 3, 
                        "name": "Кожаная броня", 
                        "description": "Легкая, удобная, немного снижает урон.",
                        "weight": 4.5
                       }
        }

        self.inventory = []

    def choose_item(self):
        print("Выберите предмет, который вы экипируете")
        for index, item in enumerate(self.inventory, start=1):
            if item['type'] == 'sword':
                print(f"{index}. {item['name']}: Урон {item['damage']}")
            elif item['type'] == 'armor':
                print(f"{index}. {item['name']}: Защита {item['defence']}")

        ans = int(input("Введите номер предмета: ")) - 1  # Преобразуем в индекс списка
        if 0 <= ans < len(self.inventory):  # Проверяем, что индекс в пределах списка
            selected_item = self.inventory[ans]
            if selected_item['type'] == 'sword':
                print(f"Вы экипировали меч {selected_item['name']} с уроном {selected_item['damage']}")
                return {'sword_damage': selected_item['damage']}
            elif selected_item['type'] == 'armor':
                print(f"Вы экипировали броню {selected_item['name']} с защитой {selected_item['defence']}")
                return {'armor_defence': selected_item['defence']}
        else:
            print("Некорректный выбор")

    def sell_item(self) :
        print("Выберите предмет, который вы продадите")
        for index, item in enumerate(self.inventory, start=1):
            if item['type'] == 'sword':
                print(f"{index}. {item['name']}: Урон {item['damage']} Цена: {item['cost']}")
            elif item['type'] == 'armor':
                print(f"{index}. {item['name']}: Защита {item['defence']} Цена: {item['cost']}")
        ans = int(input("Введите номер предмета: ")) - 1  # Преобразуем в индекс списка
        if 0 <= ans < len(self.inventory):  # Проверяем, что индекс в пределах списка
            selected_item = self.inventory[ans]
            if selected_item['type'] == 'sword':
                print(f"Вы продали меч {selected_item['name']} за {selected_item['cost']} монет")
                coins = selected_item['cost']
                self.inventory.pop(ans)
                return coins
            elif selected_item['type'] == 'armor':
                print(f"Вы продали броню {selected_item['name']} за {selected_item['cost']} монет")
                coins = selected_item['cost']
                self.inventory.pop(ans)
                return coins
        else:
            print("Некорректный выбор")


    def drop_item_sword(self, bosses_killed):
        sword = Sword(bosses_killed)
        self.inventory.append(sword.create())
 

    def drop_item_armor(self):
        armor = Armor()
        self.inventory.append(armor.create())