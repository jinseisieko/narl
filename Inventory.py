from Constants import H
from Items import Item, ShotTypeItem


class Inventory:
    def __init__(self, player) -> None:
        # values
        self.weapon_type: str = "None"
        self.items: list[Item, ShotTypeItem] = []
        self.player = player

    def add_item(self, item: [Item, ShotTypeItem]) -> None:
        self.items.append(item)
        self.apply_item(item)

    def apply_item(self, item) -> None:
        if item.parent == "Item":
            item.apply(self.player)
        elif item.parent == "ShotTypeItem":
            item.apply(self.player)
            if item.get_name() == "Buckshot":
                self.player.buckshot_scatter_count += 1
            elif item.get_name() == "GreenGecko":
                self.player.green_gecko_count += 1
            elif item.get_name() == "RedGecko":
                self.player.red_gecko_count += 1
            elif item.get_name() == "Scope":
                self.player.scope_count += 1
            elif item.get_name() == "Cactus":
                self.player.cactus_count += 1
            elif item.get_name() == "Pokeball":
                self.player.pokeball_count += 1

    def get_to_draw(self) -> list[str]:
        array_draw: list[str] = []
        for i in range(len(self.items) // H):
            array_draw += [self.items[i * H:i * H + H]]
        if len(self.items) % H != 0:
            array_draw += [self.items[-(len(self.items) % H):]]
        return array_draw
