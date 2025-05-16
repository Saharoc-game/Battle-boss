from effectmain import Effect

class PosionEffect(Effect) :

    """Эффект Яд: Каждый ход отнимает damage. Длится duration ходов """

    def __init__(self, duration: int, damage: int):
        """ Создаём новый эффект. Принимаем duration и damage"""
        super().__init__(duration)
        self.damage = damage

    def apply(self, target):
        """Обновляем эффект. Отнимаем у target урон эффекта"""
        target.health -= self.damage

    