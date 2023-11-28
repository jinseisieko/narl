"""classes Items and additional functions"""


class Item:
    def __init__(self) -> None:
        self.id: int = None
        self.parent: str = "Item"
        self.characteristics: dict = {}

    def apply(self, player) -> None:
        """changes the player's characteristics, each characteristic should have getters and setters"""

        for key, item in self.characteristics.items():
            if hasattr(player, key):
                exec(f"player.{key} *= {item}")


class ShotTypeItem:
    def __init__(self) -> None:
        self.id: int = 0
        self.parent: str = "ShotTypeItem"
        self.characteristics: dict = {}

    def get_name(self) -> str:
        """return name for item definition"""
        return self.__class__.__name__
