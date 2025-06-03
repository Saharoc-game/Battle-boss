from rich import print

from core.effect.effectmain import Effect

class StunEffect(Effect) :

    """Эффект Оглушение (Стан): Игрок пропускает ход. Длится 1 ход """

    def __init__(self):
        print("[red]Вас оглушили![/red]")
        self.duration = 1