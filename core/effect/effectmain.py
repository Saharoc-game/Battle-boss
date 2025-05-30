class Effect() :

    def __init__(self, duration):
        """Создаём эффект. Длится duration ходов """
        self.duration = duration

    def apply(self, target):
        """Обновление эффекта"""
        pass

    def update(self):
        """Уменьшение длительности эффекта"""
        if self.duration > 0:
            self.duration -= 1
        return self.duration > 0