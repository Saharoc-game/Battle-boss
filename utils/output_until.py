from rich import print

def get_stats_player_and_boss(player, boss) :
    print(f"Ваше здоровье [blue]{player.hp}[/blue]. Ваша магия  [blue]{player.magic}[/blue]. Ваши деньги  [blue]{player.money}[/blue]")
    print(f"Здоровье босса [red]{boss.hp}[/red]. Магия босса [red]{boss.magic}[/red].")