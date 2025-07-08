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

def check_dogde_and_parry(dodge, parry, damage): # Функция для проверки уклонения и парирования
    if random.randint(1, 100) <= dodge:  
        print("[green]Вы уклонились от удара![/green]")
        return None  
    elif random.randint(1, 100) <= parry:
        print("[green]Вы смогли парировать удар босса![/green]")
        print("Вы отразили [blue]50%[/blue] урона")
        return {"player_damage": damage//2, "boss_damage": damage//2} # Возвращаем урон по боссу и урон по игроку
    else:
        return {"player_damage": damage}  # Возвращаем полученный урон