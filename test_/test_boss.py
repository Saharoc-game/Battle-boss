import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import boss

class TestBoss(unittest.TestCase):
    @patch('core.boss.random.randint') 
    @patch('core.boss.random.choice')  
    def test_init(self, mock_choice, mock_randint):
        mock_choice.return_value = 55  # Boss.hp = 55
        mock_randint.return_value = 4  # Boss.magic = 4
        boss1 = boss.Boss()
        # Проверяем атрибуты
        self.assertEqual(boss1.hp, 55)
        self.assertEqual(boss1.magic, 4)
        self.assertEqual(boss1.hp_max, 55)

        mock_choice.assert_called_once_with([50, 55, 60])
        mock_randint.assert_called_once_with(3, 4)

    @patch('core.boss.random.randint')
    def test_attack_no_armor(self, mock_randint):
        boss_instance = boss.Boss()
        mock_randint.return_value = 3  # x = 3

        bosses_killed = 0
        armor_defense = 0
        expected_damage = 3

        actual_damage = boss_instance.attack(bosses_killed, armor_defense)
        self.assertEqual(actual_damage, expected_damage)
        mock_randint.assert_called_with(0, 5)

    @patch('core.boss.random.randint')
    def test_attack_with_armor(self, mock_randint):
        boss_instance = boss.Boss()
        mock_randint.return_value = 4  # x = 4

        bosses_killed = 0
        armor_defense = 50  # 50% защиты
        expected_damage = 2  # Исправлено с 4 на 2

        actual_damage = boss_instance.attack(bosses_killed, armor_defense)
        self.assertEqual(actual_damage, expected_damage)
        mock_randint.assert_called_with(0, 5)

if __name__ == '__main__':
    unittest.main()