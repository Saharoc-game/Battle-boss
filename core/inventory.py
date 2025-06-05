import random
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


from core.item.sword import Sword
from core.item.armor import Armor
from utils.input_until import get_valid_int_input

class Inventory:
    def __init__(self):

        self.mass = 0

        self.INVENTORY_STATS = {
            "swords": {"type": "sword",
                    "cost":3, 
                    "damage":5, 
                    "name": "Обычный меч", 
                    "description": "Простой, надежный меч с хорошим балансом и удобной рукоятью.",
                    "weight": 2
                    },

            "armor": {  "cost":3, 
                        "defenсe": 3, 
                        "name": "Кожаная броня", 
                        "description": "Легкая, удобная, немного снижает урон.",
                        "weight": 4.5
                       }
        }

        self.inventory = []

    def choose_item(self):
        console = Console()
        console.print(Panel("[bold green]Выберите предмет, который вы экипируете[/bold green]"))

        valid_indexes = []
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("№", style="bold cyan", width=3, justify="center")
        table.add_column("Название", style="bold yellow")
        table.add_column("Тип", style="green")
        table.add_column("Параметр", style="bold blue")

        for index, item in enumerate(self.inventory, start=1):
            if item['type'] == 'sword':
                table.add_row(
                    str(index),
                    f"[white]{item['name']}[/white]",
                    "[yellow]Меч[/yellow]",
                    f"[red]Урон {item['damage']}[/red]"
                )
                valid_indexes.append(index)
            elif item['type'] == 'armor':
                table.add_row(
                    str(index),
                    f"[white]{item['name']}[/white]",
                    "[blue]Броня[/blue]",
                    f"[green]Защита {item['defence']}[/green]"
                )
                valid_indexes.append(index)

        console.print(table)

        ans = get_valid_int_input(
            "[bold green]Введите номер предмета:[/bold green] ",
            valid_indexes
        ) - 1

        if 0 <= ans < len(self.inventory):
            selected_item = self.inventory[ans]
            if selected_item['type'] == 'sword':
                console.print(
                    Panel(
                        f"[bold green]Вы экипировали меч[/bold green] [yellow]{selected_item['name']}[/yellow] [bold green]с уроном[/bold green] [red]{selected_item['damage']}[/red]",
                        border_style="bright_blue"
                    )
                )
                return {'sword_damage': selected_item['damage']}
            elif selected_item['type'] == 'armor':
                console.print(
                    Panel(
                        f"[bold green]Вы экипировали броню[/bold green] [yellow]{selected_item['name']}[/yellow] [bold green]с защитой[/bold green] [green]{selected_item['defence']}[/green]",
                        border_style="bright_blue"
                    )
                )
                return {'armor_defence': selected_item['defence']}
        else:
            console.print(Panel("[red]Некорректный выбор[/red]", border_style="red"))

    def sell_item(self):
        console = Console()
        console.print(Panel("[bold cyan]Выберите предмет, который вы продадите[/bold cyan]", border_style="bright_blue"))

        valid_indexes = []
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("№", style="bold cyan", width=3, justify="center")
        table.add_column("Название", style="bold yellow")
        table.add_column("Тип", style="green")
        table.add_column("Параметр", style="bold blue")
        table.add_column("Цена", style="bold yellow")

        for index, item in enumerate(self.inventory, start=1):
            if item['type'] == 'sword':
                table.add_row(
                    str(index),
                    f"[white]{item['name']}[/white]",
                    "[yellow]Меч[/yellow]",
                    f"[red]Урон {item['damage']}[/red]",
                    f"[bold gold1]{item['cost']} монет[/bold gold1]"
                )
                valid_indexes.append(index)
            elif item['type'] == 'armor':
                table.add_row(
                    str(index),
                    f"[white]{item['name']}[/white]",
                    "[blue]Броня[/blue]",
                    f"[green]Защита {item['defence']}[/green]",
                    f"[bold gold1]{item['cost']} монет[/bold gold1]"
                )
                valid_indexes.append(index)
        console.print(table)

        ans = get_valid_int_input(
            "[bold green]Введите номер предмета:[/bold green] ",
            valid_indexes
        ) - 1

        if 0 <= ans < len(self.inventory):
            selected_item = self.inventory[ans]
            coins = selected_item['cost']
            self.mass -= selected_item['weight']
            self.inventory.pop(ans)
            if selected_item['type'] == 'sword':
                console.print(
                    Panel(
                        f"[bold green]Вы продали меч[/bold green] [yellow]{selected_item['name']}[/yellow] "
                        f"[bold green]за[/bold green] [bold gold1]{coins} монет[/bold gold1]",
                        border_style="bright_blue"
                    )
                )
            elif selected_item['type'] == 'armor':
                console.print(
                    Panel(
                        f"[bold green]Вы продали броню[/bold green] [yellow]{selected_item['name']}[/yellow] "
                        f"[bold green]за[/bold green] [bold gold1]{coins} монет[/bold gold1]",
                        border_style="bright_blue"
                    )
                )
            return coins
        else:
            console.print(Panel("[red]Некорректный выбор[/red]", border_style="red"))


    def drop_item_sword(self, bosses_killed):
        sword = Sword(bosses_killed)
        self.mass += sword.weight
        print(Panel(f"Вы получили предмет - {sword.name}\n{sword.description}\nВес - {sword.weight}\nУрон - {sword.damage}\nЦена - {sword.cost}", title="Вы получили предмет!"))
        self.inventory.append(sword.create())
 

    def drop_item_armor(self):
        armor = Armor()
        self.mass += armor.weight
        print(Panel(f"Вы получили предмет - {armor.name}\n{armor.description}\nВес - {armor.weight}\nБроня - {armor.defence}%\nЦена - {armor.cost}", title="Вы получили предмет!"))
        self.inventory.append(armor.create())