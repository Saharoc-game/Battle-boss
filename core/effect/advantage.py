from core.effect.effectmain import Effect


class AdvantageEffect(Effect) :

    def __init__(self):
        """Создаём эффект. Длится duration ходов """
        self.duration = 1

    def apply(self, target):
        target.advantage = 30
