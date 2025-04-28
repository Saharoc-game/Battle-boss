import arcade
from core import boss, player
from core.boss import random_boss
from core import inventory as inv
import BattleBoss

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



class BattleBoss(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height, title="BattleBoss"):
        super().__init__(width, height, title)
        self.player = player.choose_playerclass()
        self.boss = boss.random_boss()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Настроить игру здесь
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
         # Отображение информации об игроке
        arcade.draw_text(f"Здоровье игрока: {self.player.hp}", 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Магия игрока: {self.player.magic}", 10, SCREEN_HEIGHT - 40, arcade.color.WHITE, 14)
        arcade.draw_text(f"Деньги игрока: {self.player.money}", 10, SCREEN_HEIGHT - 60, arcade.color.WHITE, 14)
        # Отображение информации о боссе
        arcade.draw_text(f"Здоровье босса: {self.boss.hp}", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Магия босса: {self.boss.magic}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)



    def update(self, delta_time):
        """ Здесь вся игровая логика"""
        pass


def main():
    game = BattleBoss(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main() 