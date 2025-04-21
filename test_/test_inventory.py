import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
    
    def test_initial_state(self):
        self.assertEqual(len(self.inv.inventory_swordss), 0)
        self.assertEqual(len(self.inv.inventory_armor), 0)
    
    @patch('builtins.input', side_effect=['1', '1'])
    def test_choose_item_sword(self, mock_input):
        self.inv.inventory_swordss = [15, 20]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = self.inv.choose_item()
            self.assertEqual(result, 15)
            self.assertIn("1 меч", fake_out.getvalue())
    
    @patch('builtins.input', side_effect=['2', '1'])
    def test_choose_item_armor(self, mock_input):
        self.inv.inventory_armor = [30, 40]
        result = self.inv.choose_item()
        self.assertEqual(result, 30)
    
    @patch('builtins.input', side_effect=['1', '3'])
    def test_choose_item_invalid_index(self, mock_input):
        self.inv.inventory_swordss = [10]
        result = self.inv.choose_item()
        self.assertIsNone(result)
    
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sell_item_sword(self, mock_out, mock_input):
        self.inv.inventory_swordss = [15]
        self.inv.sword_damage = 0
        self.inv.sell_item()
        self.assertEqual(len(self.inv.inventory_swordss), 0)
        self.assertIn("Вы продали меч", mock_out.getvalue())
    
    @patch('builtins.input', side_effect=['2', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sell_item_armor(self, mock_out, mock_input):
        self.inv.inventory_armor = [30]
        self.inv.armor_defense = 0
        self.inv.sell_item()
        self.assertEqual(len(self.inv.inventory_armor), 0)
        self.assertIn("Вы продали броню", mock_out.getvalue())
    
    @patch('random.randint', return_value=20)
    def test_drop_item_sword(self, mock_randint):
        result = self.inv.drop_item_sword(3)
        self.assertEqual(result, 23)  # 20 (random) + 3 (bosses_killed)
        mock_randint.assert_called_once_with(5, 23)
    
    @patch('random.randint', return_value=35)
    @patch('sys.stdout', new_callable=StringIO)
    def test_drop_item_armor(self, mock_out, mock_randint):
        result = self.inv.drop_item_armor(2)
        self.assertEqual(result, 35)
        self.assertIn("Вы нашли броню", mock_out.getvalue())
        mock_randint.assert_called_once_with(1, 50)
    
    @patch('builtins.input', side_effect=['3', '1'])  # Неверный первый ввод
    def test_invalid_first_input(self, mock_input):
        self.inv.inventory_swordss = [10]
        result = self.inv.choose_item()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()