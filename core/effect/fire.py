from core.effect.poison import PosionEffect

class FireEffect(PosionEffect) :
     
    """Эффект Огонь: Каждый ход отнимает damage. Длится duration ходов. Каждый ход снижает урон на 30% """

    def __init__(self, duration: int, damage: int):
        """ Создаём новый эффект. Принимаем duration и damage"""
        super().__init__(duration, damage)
        print(f"Вас подожгли! Вы будете гореть {duration} ходов. А так же сила {damage} ")
        self.damage = damage

    def apply(self, target):
        """Обновляем эффект. Отнимаем у target урон эффекта. Также снижаем damage на 30%"""
        target.hp -= self.damage
        self.damage = int(self.damage - (self.damage * 0.3))

