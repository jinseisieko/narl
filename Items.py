"""classes Items and additional functions"""


class Item:
    def __init__(self) -> None:
        self.id: int = 0
        self.parent: str = "Item"
        self.characteristics: dict = {}

    def apply(self, player) -> None:
        """changes the player's characteristics, each characteristic should have getters and setters"""

        for key, item in self.characteristics.items():
            if hasattr(player, key):
                eval(f"player.set_{key}(player.get_{key}() * item)")
