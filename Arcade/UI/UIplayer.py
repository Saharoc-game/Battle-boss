import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class HealthBar(arcade.gui.UIWidget):
    def __init__(self, center_x, center_y, width, height, max_health=100):
        super().__init__(center_x=center_x, center_y=center_y)
        self.rect = arcade.rect.XYWH(center_x - width // 2, center_y - height // 2, width, height)
        self.max_health = max_health
        self.current_health = 100

    def do_render(self, surface):
        # Рисуем рамку полоски HP
        arcade.draw_rect_outline(self.rect, arcade.color.WHITE, border_width=2)
        print("do_render вызван!")  # Проверяем, вызывается ли метод


        # Вычисляем ширину заполненной области
        filled_width = self.rect.width * (self.current_health / self.max_health)
        filled_rect = self.rect.resize(width=filled_width)

        # Отрисовка активной полоски
        arcade.draw_rect_filled(filled_rect, arcade.color.RED)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "HP Bar с GUI Arcade")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.health_bar = HealthBar(center_x=100, center_y=50, width=200, height=20, max_health=100)
        print(f"Размер полоски HP: {self.rect.width}x{self.rect.height}")
        self.manager.add(self.health_bar)

    def on_draw(self):
        self.clear()
        self.manager.draw()


    def update(self, delta_time: float):
        print("update выполняется!")  # Проверяем, вызывается ли обновление
        self.health_bar.current_health -= 0.1
        if self.health_bar.current_health < 0:
            self.health_bar.current_health = self.health_bar.max_health



def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
