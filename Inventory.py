from Items import Item, ShotTypeItem


class Inventory:
    def __init__(self, player) -> None:
        # values
        self.weapon_type: str = "None"
        self.items: list[Item, ShotTypeItem] = []
        self.player = player

    def add_item(self, item: (Item, ShotTypeItem)) -> None:
        self.items.append(item)

    def apply_item(self, item):
        item.apply(self.player)
