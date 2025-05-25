from core.effect.poison import PosionEffect 

class BleedingEffect(PosionEffect) :

    """Эффект Кровотечение: Каждый ход отнимает damage. Длится duration ходов """

    def __init__(self, duration: int, damage: int):
        """ Создаём новый эффект. Принимаем duration и damage"""
        super().__init__(duration)
        print(f"У вас кровопотеря! Эффект будет действовать {duration} ходов. А так же сила {damage} ")
        self.damage = damage

    def apply(self, target):
        """Обновляем эффект. Отнимаем у target урон эффекта"""
        target.hp -= self.damage
