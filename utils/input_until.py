from rich import print
import random

def get_valid_int_input(prompt, valid_options): # Функция для получения корректного ввода от пользователя
    while True:
        try:
            print(prompt, end='')
            x = int(input())
            if x not in valid_options:
                print(f"Пожалуйста, введите {', '.join(str(opt) for opt in valid_options)}")
                continue
            return x # Возвращаем корректное значение
        except ValueError:
            print("Пожалуйста, введите число")

def check_dogde(dogde, damage): # Функция для проверки уклонения
    if random.random() < dogde:  # Если случайное число меньше шанса уклонения
        print("[green]Вы уклонились от удара![/green]")
        return 0  # Возвращаем 0 урона
    else:
        return damage  # Возвращаем полученный урон