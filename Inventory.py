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

    def apply_item(self, item):
        if item.parent == "Item":
            item.apply(self.player)
