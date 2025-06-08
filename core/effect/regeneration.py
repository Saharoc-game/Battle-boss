from rich import print
from core.effect.effectmain import Effect
from core.item.ring import Ring

class Regen(Effect):
    def __init__(self, duration: int, heal: int):
        super().__init__(duration, heal)
        self.heal = Ring.effect
    def apply(self, target):
        target.hp += self.heal
