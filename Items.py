"""classes Items and additional functions"""


def get_item(id_: int):
    if id_ == RuneOfSpeed.id:
        return RuneOfSpeed()
    elif id_ == RuneOfHeart.id:
        return RuneOfHeart()
    elif id_ == RuneOfArrow.id:
        return RuneOfArrow()
    elif id_ == RuneOfRange.id:
        return RuneOfRange()
    elif id_ == RuneOfRapidity.id:
        print(1)
        return RuneOfRapidity()
    else:
        raise Exception()


class Item:
    def __init__(self) -> None:
        self.id: [int, None] = None
        self.image: str = ''
        self.parent: str = "Item"
        self.characteristics: dict = {}

    def apply(self, player) -> None:
        """changes the player's characteristics, each characteristic should have getters and setters"""

        for key, item in self.characteristics.items():
            if hasattr(player, key):
                exec(f"player.{key} {item}")


class ShotTypeItem:
    def __init__(self) -> None:
        self.id: int = 0
        self.image: str = ''
        self.parent: str = "ShotTypeItem"
        self.characteristics: dict = {}

    def get_name(self) -> str:
        """return name for item definition"""
        return self.__class__.__name__


class RuneOfSpeed(Item):
    id = 0

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_speed'
        self.characteristics['max_speed'] = '+= 0.1'


class RuneOfHeart(Item):
    id = 1

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_heart'
        self.characteristics['max_hp'] = '+= 1'


class RuneOfArrow(Item):
    id = 2

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_arrow'
        self.characteristics['period'] = "-=1"

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class RuneOfRange(Item):
    id = 3

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_range'
        self.characteristics['projectile_range'] = '+= 5'


class RuneOfRapidity(Item):
    id = 4

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_rapidity'
        self.characteristics['projectile_speed'] = '+= 0.1'
