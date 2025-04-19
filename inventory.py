import random
def drop_item_sword(bosses_killed): # Выдача случайного меча
    x = random.randint(5, 23) + bosses_killed
    print("Вы нашли меч и его урон ", x)
    return x

def drop_item_armor(bosses_killed) : # Выдача случайной брони
    x = random.randint(1, 50)
    print("Вы нашли броню и её защита ", x, "%")
    return x
