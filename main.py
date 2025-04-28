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
        self

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Настроить игру здесь
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика"""
        pass


def main():
    game = BattleBoss(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main() 