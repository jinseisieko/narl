"""classes Items and additional functions"""


def get_item(id_: int):
    if id_ == Lightning.id:
        return Lightning()
    elif id_ == RuneOfHeart.id:
        return RuneOfHeart()
    elif id_ == WoodenBow.id:
        return WoodenBow()
    elif id_ == HuntingArrow.id:
        return HuntingArrow()
    elif id_ == IronBullet.id:
        return IronBullet()
    elif id_ == Cigarette.id:
        return Cigarette()
    elif id_ == Meteorite.id:
        return Meteorite()
    elif id_ == ElderberryStick.id:
        return ElderberryStick()
    elif id_ == Paddle.id:
        return Paddle()
    elif id_ == PaeShot.id:
        return PaeShot()
    elif id_ == RedBall.id:
        return RedBall()
    elif id_ == Sunflower.id:
        return Sunflower()
    elif id_ == OrangeSlice.id:
        return OrangeSlice()
    elif id_ == Dagger.id:
        return Dagger()
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


class Lightning(Item):
    id = 0

    def __init__(self) -> None:
        super().__init__()
        self.image = 'lightning'
        self.characteristics['max_speed'] = '+= 0.1'


class RuneOfHeart(Item):
    id = 1

    def __init__(self) -> None:
        super().__init__()
        self.image = 'rune_of_heart'
        self.characteristics['max_hp'] = '+= 1'


class WoodenBow(Item):
    id = 2

    def __init__(self) -> None:
        super().__init__()
        self.image = 'wooden_bow'
        self.characteristics['period'] = "-=1"

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class HuntingArrow(Item):
    id = 3

    def __init__(self) -> None:
        super().__init__()
        self.image = 'hunting_arrow'
        self.characteristics['projectile_range'] = '+= 5'


class IronBullet(Item):
    id = 4

    def __init__(self) -> None:
        super().__init__()
        self.image = 'iron_bullet'
        self.characteristics['projectile_speed'] = '+= 0.1'


class Cigarette(Item):
    id = 5

    def __init__(self) -> None:
        super().__init__()
        self.image = "cigarette"
        self.characteristics['period'] = "*= 0.90"
        self.characteristics['max_speed'] = "+= 0.2"
        self.characteristics['max_hp'] = "-= 2"

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class Meteorite(Item):
    id = 6

    def __init__(self) -> None:
        super().__init__()
        self.image = "meteorite"
        self.characteristics['projectile_speed'] = '*= 0.80'
        self.characteristics['projectile_size'] = '*= 1.20'


class ElderberryStick(Item):
    id = 7

    def __init__(self) -> None:
        super().__init__()
        self.image = "elderberry_stick"
        self.characteristics['period'] = "*= 0.5"
        self.characteristics['projectile_speed'] = '+= 0.5'
        self.characteristics['projectile_range'] = '+= 10'
        self.characteristics['projectile_damage'] = '+= 2'

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class Paddle(Item):
    id = 8

    def __init__(self) -> None:
        super().__init__()
        self.image = "paddle"
        self.characteristics['period'] = "*= 1.1"
        self.characteristics['max_speed'] = '+= 0.3'

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class PaeShot(Item):
    id = 9

    def __init__(self) -> None:
        super().__init__()
        self.image = 'pae_shot'
        self.characteristics['period'] = "*= 0.95"
        self.characteristics['projectile_range'] = '+= 100'

    def apply(self, player) -> None:
        super().apply(player)
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")


class RedBall(Item):
    id = 10

    def __init__(self) -> None:
        super().__init__()
        self.image = 'red_ball'
        self.characteristics['projectile_speed'] = '+= 0.2'


class Sunflower(Item):
    id = 11

    def __init__(self) -> None:
        super().__init__()
        self.image = 'sunflower'
        self.characteristics['projectile_damage'] = '+= 2'


class OrangeSlice(Item):
    id = 12

    def __init__(self) -> None:
        super().__init__()
        self.image = "orange_slice"
        self.characteristics['projectile_speed'] = '+= 0.1'
        self.characteristics['max_hp'] = "+= 1"


class Dagger(Item):
    id = 13

    def __init__(self) -> None:
        super().__init__()
        self.image = "dagger"
        self.characteristics['projectile_speed'] = '+= 0.1'
        self.characteristics['projectile_damage'] = '+= 3'



