import random

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.item.armor import Armor
from core.item.sword import Sword

from utils.input_until import get_valid_int_input

class ShopEvent:
    def __init__(self):
        self.inventory = []

    def add_random_item(self) :
        if random.randint(0, 1) == 0 :
            sword = Sword(kolboss=0)
            self.inventory.append(sword.create())
        else :
            armor = Armor()
            self.inventory.append(armor.create())

    def trigger(self, player):
        print("\n[bold cyan]Вы попали в магазин![/bold cyan]")

        for i in range(5) :
            self.add_random_item()

        while True :
            print(f"У вас денег [yellow]{player.money}[/yellow]")

            console = Console()
            console.print(Panel("[bold cyan]Выберите предмет, который вы купите[/bold cyan]", border_style="bright_blue"))

            valid_indexes = [0]

            # Создаём таблицу
            table = Table(show_header=True, header_style="bold magenta") 

            # Добавляем колонки
            table.add_column("№", style="bold cyan", width=3, justify="center")
            table.add_column("Название", style="bold yellow")
            table.add_column("Тип", style="green")
            table.add_column("Параметр", style="bold blue")
            table.add_column("Цена", style="bold yellow")

            for index, item in enumerate(self.inventory, start=1): # Добавляем предметы по очереди
                if item['type'] == 'sword': # Мечи
                    table.add_row(
                        str(index),
                        f"[white]{item['name']}[/white]",
                        "[yellow]Меч[/yellow]",
                        f"[red]Урон {item['damage']}[/red]",
                        f"[bold gold1]{item['cost']} монет[/bold gold1]"
                    ) # Добавляем строчу
                    valid_indexes.append(index)
                elif item['type'] == 'armor': # Броня
                    table.add_row(
                    str(index),
                    f"[white]{item['name']}[/white]",
                    "[blue]Броня[/blue]",
                    f"[green]Защита {item['defence']}[/green]",
                    f"[bold gold1]{item['cost']} монет[/bold gold1]"
                ) # Добавляем строчу
                valid_indexes.append(index)
            console.print(table)

            ans = get_valid_int_input(
                "[bold green]Введите номер предмета:[/bold green]\nЧтобы выйти из магазина, введите [blue]0[/blue]\n ",
                valid_indexes
            ) - 1 # Игрок выбирает предмет

            if ans == -1 :
                print("Вы вышли из магазина")
                return None
            
            selected_item = self.inventory[ans]
            coins = selected_item['cost']

            if coins <= player.money :
                player.inventory.mass += selected_item['weight']
                player.money -= coins
                if selected_item['type'] == 'armor' :
                    defence = selected_item['defence']
                    cost = (selected_item['cost'] + 1) // 2
                    name = selected_item['name']
                    description = selected_item['description']
                    weight = selected_item['weight']
                    item = Armor(
                        defence=defence,
                        cost=cost,
                        name=name,
                        description=description,
                        weight=weight)
                else :
                    damage = selected_item['damage']
                    cost = selected_item['cost']
                    name = selected_item['name']
                    description = selected_item['description']
                    weight = selected_item['weight']
                    item = Sword(
                        kolboss=player.bosses_killed,
                        damage=damage,
                        cost=cost,
                        name=name,
                        description=description,
                        weight=weight)
                player.inventory.inventory.append(item.create())
                self.inventory.pop(ans)
                console.print(Panel(f"Вы купили предмет за [bold gold1]{coins}[/bold gold1]", border_style="bright_blue"))

