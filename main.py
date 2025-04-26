import arcade
from core import boss, player
from core.boss import random_boss
from core import inventory as inv
import BatleBoss

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1080


class BatleBoss(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Настроить игру здесь
        B1 = boss(random_boss())
        P1 = playr
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика"""
        pass


def main():
    game = BatleBoss(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main() 