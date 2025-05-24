from core.effect.effectmain import Effect

class StunEffect(Effect) :

    """Эффект Оглушение (Стан): Игрок пропускает ход. Длится 1 ход """

    def __init__(self, ):
        self.duration = 1