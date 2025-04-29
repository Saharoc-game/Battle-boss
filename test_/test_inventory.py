import unittest
from unittest.mock import patch
import random

# Мы копируем класс Inventory сюда для тестирования.
# В реальном проекте можно импортировать класс из основного модуля.
class Inventory:
    def __init__(self):
        # Словарь с двумя списками: один для мечей, другой для брони.
        self.inventory = {
            "swords": [],
            "armor": []
        }

    def choose_item(self):
        x = int(input("Введите 1, чтобы просмотреть мечи, или 2, чтобы просмотреть броню: "))
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
        return None

    def sell_item(self):
        x = int(input("Введите 1, чтобы продать меч, или 2, чтобы продать броню: "))
        if x == 1:
            swords = self.inventory.get("swords", [])
            if len(swords) > 0:
                for i, sword in enumerate(swords, start=1):
                    print(f"{i}: Меч с уроном {sword}")
                sell_choice = int(input("Выберите номер меча для продажи: "))
                if 1 <= sell_choice <= len(swords):
                    sword_damage = swords.pop(sell_choice - 1)
                    coins = sword_damage // 5
                    print(f"Вы продали меч и получили {coins} монет.")
                else:
                    print("Неверный выбор!")
            else:
                print("У вас нет мечей.")
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

    def drop_item_sword(self, bosses_killed):
        x = random.randint(5, 23) + bosses_killed
        print("Вы нашли меч с уроном", x)
        self.inventory.setdefault("swords", []).append(x)
        return x

    def drop_item_armor(self, bosses_killed):
        x = random.randint(1, 50)
        print("Вы нашли броню с защитой", x, "%")
        self.inventory.setdefault("armor", []).append(x)
        return x


class TestInventory(unittest.TestCase):
    def setUp(self):
        # Создаем инстанс инвентаря для каждого теста.
        self.inv = Inventory()

    def test_drop_item_sword(self):
        # Чтобы тест был предсказуемым, фиксируем случайное число.
        bosses_killed = 10
        with patch('random.randint', return_value=8):
            # Ожидаем: x = 8 + bosses_killed = 18
            result = self.inv.drop_item_sword(bosses_killed)
            self.assertEqual(result, 18)
            # Проверяем, что элемент добавлен в список мечей.
            self.assertIn(18, self.inv.inventory["swords"])

    def test_drop_item_armor(self):
        bosses_killed = 0  # bosses_killed здесь не влияет
        with patch('random.randint', return_value=25):
            result = self.inv.drop_item_armor(bosses_killed)
            self.assertEqual(result, 25)
            self.assertIn(25, self.inv.inventory["armor"])

    def test_choose_item_with_swords(self):
        # Заполним список мечей.
        self.inv.inventory["swords"] = [15, 20, 25]
        # Порядок ввода: сначала выбираем тип (1 для мечей), затем выбираем второй меч (ввод "2").
        user_inputs = ["1", "2"]
        with patch('builtins.input', side_effect=user_inputs):
            chosen = self.inv.choose_item()
            self.assertEqual(chosen, 20)

    def test_choose_item_no_swords(self):
        # Если мечей нет, функция должна вернуть None.
        self.inv.inventory["swords"] = []
        user_inputs = ["1"]
        with patch('builtins.input', side_effect=user_inputs):
            chosen = self.inv.choose_item()
            self.assertIsNone(chosen)

    def test_sell_item_with_swords(self):
        # Заполним мечи. Пусть два меча с уроном 30 и 45.
        self.inv.inventory["swords"] = [30, 45]
        # Порядок ввода: сначала "1" для выбора мечей, затем "2" для продажи второго меча.
        user_inputs = ["1", "2"]
        with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
            self.inv.sell_item()
            # После продажи меча с уроном 45 должен остаться меч с уроном 30.
            self.assertEqual(self.inv.inventory["swords"], [30])
            # Убедимся, что вывод содержит информацию о полученных монетах (45 // 5 == 9 монет)
            printed = " ".join(arg for call in mock_print.call_args_list for arg in call.args if isinstance(arg, str))
            self.assertIn("9 монет", printed)

    def test_sell_item_with_armor(self):
        # Заполним броню, например [40, 20].
        self.inv.inventory["armor"] = [40, 20]
        # Порядок ввода: "2" для выбора брони, затем "1" для продажи первого броневого элемента.
        user_inputs = ["2", "1"]
        with patch('builtins.input', side_effect=user_inputs), patch('builtins.print') as mock_print:
            self.inv.sell_item()
            # После продажи должна остаться броня со значением 20.
            self.assertEqual(self.inv.inventory["armor"], [20])
            printed = " ".join(arg for call in mock_print.call_args_list for arg in call.args if isinstance(arg, str))
            # 40 // 20 == 2 монеты
            self.assertIn("2 монет", printed)


if __name__ == '__main__':
    unittest.main()
