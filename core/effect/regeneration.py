from core.effect.effectmain import Effect

class RegenerationEffect(Effect):

    """Эффект Регенерации: Каждый ход восстанавливает n-ое колличество hp"""

    def __init__(self, duration: int, power: int):
        super().__init__(duration)
        self.power = power

    def apply(self, target):
        """Обновляем эффект. Добавляем target hp по формуле target.hp * ((power * 5 + 5) / 100)"""
        self.heal = int(target.hp * ((self.power * 5 + 5) / 100))
        target.hp += min(self.heal, target.max_hp)
