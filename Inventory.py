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

    def get_to_draw(self) -> list[str]:
        array_draw: list[str] = []
        for i in range(len(self.items) // 5):
            array_draw += [self.items[i * 5:i * 5 + 5]]
        if len(self.items) % 5 != 0:
            array_draw += [self.items[-(len(self.items) % 5):]]
        return array_draw
