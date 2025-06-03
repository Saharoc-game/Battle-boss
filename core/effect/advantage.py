from rich import print

from core.effect.effectmain import Effect


class AdvantageEffect(Effect) :

    def __init__(self):
        """Создаём эффект. Длится duration ходов """
        self.duration = 2
        print(f"У вас перевес! Ваш урон снижен на [red]30%[/red]")

    def apply(self, target):
        target.advantage = 30
