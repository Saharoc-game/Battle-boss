import unittest
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))

from boss import Boss, BossWar, BossWiz, BossArc, random_boss

class TestBoss(unittest.TestCase):

    def test_boss_creation(self):
        boss = Boss()
        self.assertIn(boss.hp, [50, 55, 60])
        self.assertIn(boss.magic, [3, 4])
        self.assertEqual(boss.recharge, 10)

    def test_boss_attack(self):
        boss = Boss()
        dmg = boss.attack(bosses_killed=2, armor_defense=10)
        self.assertIsInstance(dmg, int)
        self.assertGreaterEqual(dmg, 0)  # Урон не должен быть отрицательным

    def test_health_add(self):
        boss = Boss()
        boss.magic = 2
        boss.health_add()
        self.assertGreaterEqual(boss.hp, 50)  # Проверяем, что HP увеличилось
        self.assertEqual(boss.magic, 1)  # Проверяем, что магия уменьшилась

    def test_add_recharge(self):
        boss = Boss()
        boss.recharge = 5
        boss.add_recharge()
        self.assertEqual(boss.recharge, 7.5)  # Проверяем увеличение заряда

class TestBossSubclasses(unittest.TestCase):
    
    def test_boss_war(self):
        boss_war = BossWar()
        self.assertEqual(boss_war.name_ability, "Гнев Титана")

    def test_boss_wiz(self):
        boss_wiz = BossWiz()
        self.assertEqual(boss_wiz.name_ability, "Пламя Затмений")

    def test_boss_arc(self):
        boss_arc = BossArc()
        self.assertEqual(boss_arc.name_ability, "Дождь Призрачных Стрел")

    def test_random_boss(self):
        boss = random_boss()
        self.assertIsInstance(boss, (BossWar, BossWiz, BossArc))  # Проверяем, что босс — один из подклассов

if __name__ == "__main__":
    unittest.main()
