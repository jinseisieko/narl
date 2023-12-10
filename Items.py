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
    elif id_ == LastPlaceMedal.id:
        return LastPlaceMedal()
    elif id_ == Lollipop.id:
        return Lollipop()
    elif id_ == MiniVolcano.id:
        return MiniVolcano()
    elif id_ == Hat.id:
        return Hat()
    elif id_ == MiniShark.id:
        return MiniShark()
    elif id_ == Helmet.id:
        return Helmet()
    elif id_ == GreenRocket.id:
        return GreenRocket()
    elif id_ == RedRocket.id:
        return RedRocket()
    elif id_ == IronClaw.id:
        return IronClaw()
    elif id_ == Gun.id:
        return Gun()
    elif id_ == Hammer.id:
        return Hammer()
    elif id_ == PlusOne.id:
        return PlusOne()
    elif id_ == Buckshot.id:
        return Buckshot()
    elif id_ == Wristwatch.id:
        return Wristwatch()
    elif id_ == Pill.id:
        return Pill()
    elif id_ == GreenGecko.id:
        return GreenGecko()
    elif id_ == Butterfly.id:
        return Butterfly()
    elif id_ == GraveShovel.id:
        return GraveShovel()
    elif id_ == Casino.id:
        return Casino()
    elif id_ == RedGecko.id:
        return RedGecko()
    elif id_ == Flower.id:
        return Flower()
    elif id_ == Syringe.id:
        return Syringe()
    elif id_ == ChristmasTree.id:
        return ChristmasTree()
    elif id_ == DecoratedChristmasTree.id:
        return DecoratedChristmasTree()
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

        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")

        if hasattr(player, 'projectile_size'):
            exec(f"import math; player.projectile_size = math.ceil(player.projectile_size)")

        if hasattr(player, 'projectile_damage'):
            exec("import math; player.projectile_damage = math.ceil(player.projectile_damage)")

        if hasattr(player, 'max_hp'):
            exec("import math; player.max_hp = math.ceil(player.max_hp)")


class ShotTypeItem:
    def __init__(self) -> None:
        self.id: int = 0
        self.image: str = ''
        self.parent: str = "ShotTypeItem"
        self.characteristics: dict = {}

    def apply(self, player) -> None:
        """changes the player's characteristics, each characteristic should have getters and setters"""

        for key, item in self.characteristics.items():
            if hasattr(player, key):
                exec(f"player.{key} {item}")

        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")

        if hasattr(player, 'projectile_size'):
            exec(f"import math; player.projectile_size = math.ceil(player.projectile_size)")

        if hasattr(player, 'projectile_damage'):
            exec("import math; player.projectile_damage = math.ceil(player.projectile_damage)")

        if hasattr(player, 'max_hp'):
            exec("import math; player.max_hp = math.ceil(player.max_hp)")

    def get_name(self) -> str:
        """return name for item definition"""
        return self.__class__.__name__


class Lightning(Item):
    id = 0

    def __init__(self) -> None:
        super().__init__()
        self.image = 'lightning'
        self.characteristics['max_speed'] = '+= 0.2'


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
        self.characteristics['period'] = "-=40"


class HuntingArrow(Item):
    id = 3

    def __init__(self) -> None:
        super().__init__()
        self.image = 'hunting_arrow'
        self.characteristics['projectile_range'] = '+= 10'


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


class Meteorite(Item):
    id = 6

    def __init__(self) -> None:
        super().__init__()
        self.image = "meteorite"
        self.characteristics['projectile_speed'] = '*= 0.80'
        self.characteristics['projectile_size'] = '+= 4'


class ElderberryStick(Item):
    id = 7

    def __init__(self) -> None:
        super().__init__()
        self.image = "elderberry_stick"
        self.characteristics['period'] = "*= 0.5"
        self.characteristics['projectile_speed'] = '+= 0.75'
        self.characteristics['projectile_range'] = '+= 10'
        self.characteristics['projectile_damage'] = '+= 2'


class Paddle(Item):
    id = 8

    def __init__(self) -> None:
        super().__init__()
        self.image = "paddle"
        self.characteristics['period'] = "*= 1.1"
        self.characteristics['max_speed'] = '+= 0.3'


class PaeShot(Item):
    id = 9

    def __init__(self) -> None:
        super().__init__()
        self.image = 'pae_shot'
        self.characteristics['period'] = "*= 0.95"
        self.characteristics['projectile_range'] = '+= 100'


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


class LastPlaceMedal(Item):
    id = 14

    def __init__(self) -> None:
        super().__init__()
        self.image = "last_place_medal"
        self.c: float = 2

    def apply(self, player) -> None:
        exec(
            f"""from Constants import *
import math
c1 = abs(DEFAULT_PLAYER_SPEED - player.max_speed) / DEFAULT_PLAYER_SPEED * 3
c2 = abs(DEFAULT_PROJECTILE_RANGE - player.projectile_range) / DEFAULT_PROJECTILE_RANGE
c3 = abs(DEFAULT_PROJECTILE_SPEED - player.projectile_speed) / DEFAULT_PROJECTILE_SPEED * 4
c4 = abs(DEFAULT_PROJECTILE_SIZE - player.projectile_size) / DEFAULT_PROJECTILE_SIZE * 6
c5 = abs(DEFAULT_PROJECTILE_DAMAGE - player.projectile_damage) / DEFAULT_PROJECTILE_DAMAGE
c = [c1, c2, c3, c4, c5].index(min([c1, c2, c3, c4, c5]))
if c == 0:
    player.max_speed *= {self.c}
elif c == 1:
    player.projectile_range *= {self.c}
elif c == 2:
    player.projectile_speed *= {self.c}
elif c == 3:
    player.projectile_size *= {self.c}
elif c == 4:
    player.projectile_damage *= {self.c}
""")
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")

        if hasattr(player, 'projectile_size'):
            exec(f"import math; player.projectile_size = math.ceil(player.projectile_size)")

        if hasattr(player, 'projectile_damage'):
            exec("import math; player.projectile_damage = math.ceil(player.projectile_damage)")


class Lollipop(Item):
    id = 15

    def __init__(self) -> None:
        super().__init__()
        self.image = "lollipop"
        self.characteristics['projectile_range'] = "+= 8"


class MiniVolcano(Item):
    id = 16

    def __init__(self) -> None:
        super().__init__()
        self.image = "mini_volcano"
        self.characteristics['projectile_damage'] = "+= 1"
        self.characteristics['period'] = "*= 1.1"


class Hat(Item):
    id = 17

    def __init__(self) -> None:
        super().__init__()
        self.image = 'hat'
        self.characteristics['max_speed'] = '-= 0.3'
        self.characteristics['projectile_range'] = "+= 10"


class MiniShark(Item):
    id = 18

    def __init__(self) -> None:
        super().__init__()
        self.image = 'mini_shark'
        self.characteristics['period'] = "-= 100"
        self.characteristics['projectile_size'] = "*= 0.8"


class Helmet(Item):
    id = 19

    def __init__(self) -> None:
        super().__init__()
        self.image = 'helmet'
        self.characteristics['max_hp'] = "+= 1"
        self.characteristics['max_speed'] = '-= 0.1'
        self.characteristics['projectile_speed'] = '*= 0.94'


class GreenRocket(Item):
    id = 20

    def __init__(self) -> None:
        super().__init__()
        self.image = 'green_rocket'
        self.characteristics['projectile_damage'] = "+= 5"
        self.characteristics['period'] = "+= 200"


class RedRocket(Item):
    id = 21

    def __init__(self) -> None:
        super().__init__()
        self.image = 'red_rocket'
        self.characteristics['projectile_damage'] = "+= 10"
        self.characteristics['period'] = "+= 500"


class IronClaw(Item):
    id = 22

    def __init__(self) -> None:
        super().__init__()
        self.image = 'iron_claw'
        self.characteristics['projectile_damage'] = "+= 5"
        self.characteristics['max_speed'] = '-= 0.2'
        self.characteristics['projectile_speed'] = '-= 0.1'


class Gun(Item):
    id = 23

    def __init__(self) -> None:
        super().__init__()
        self.image = 'gun'
        self.characteristics['max_speed'] = '-= 0.5'
        self.characteristics['period'] = "*= 0.60"


class Hammer(Item):
    id = 24

    def __init__(self) -> None:
        super().__init__()
        self.image = 'hammer'
        self.characteristics['period'] = "*= 0.9"
        self.characteristics['projectile_damage'] = "*= 1.1"
        self.characteristics['projectile_speed'] = '*= 1.1'
        self.characteristics['projectile_size'] = "*= 1.1"
        self.characteristics['projectile_range'] = "*= 0.70"


class PlusOne(Item):
    id = 25

    def __init__(self) -> None:
        super().__init__()
        self.image = 'plus_one'
        self.characteristics['period'] = "-= 1"
        self.characteristics['max_speed'] = '+= 1'
        self.characteristics['projectile_damage'] = "+= 1"
        self.characteristics['projectile_speed'] = '+= 1'
        self.characteristics['projectile_size'] = "+= 1"
        self.characteristics['projectile_range'] = "+= 1"
        self.characteristics['max_hp'] = "+= 1"


class Buckshot(ShotTypeItem):
    id = 26

    def __init__(self) -> None:
        super().__init__()
        self.image = 'buckshot'
        self.characteristics['period'] = "*= 0.40"
        self.characteristics['projectile_size'] = "*= 0.75"
        # adds the scattering effect of sears


class Wristwatch(Item):
    id = 27

    def __init__(self) -> None:
        super().__init__()
        self.image = 'wristwatch'
        self.characteristics['period'] = "*= 0.95"


class Pill(Item):
    id = 28

    def __init__(self) -> None:
        super().__init__()
        self.image = 'pill'
        self.characteristics['max_hp'] = "+= 1"
        self.characteristics['max_speed'] = "+= 0.3"


class GreenGecko(ShotTypeItem):
    id = 29

    def __init__(self) -> None:
        super().__init__()
        self.image = 'green_gecko'
        self.characteristics['projectile_range'] = "*= 1.5"
        # add arc trajectory


class Butterfly(Item):
    id = 30

    def __init__(self) -> None:
        super().__init__()
        self.image = 'butterfly'
        self.characteristics['projectile_size'] = "*= 1.05"


class GraveShovel(Item):
    id = 31

    def __init__(self) -> None:
        super().__init__()
        self.image = 'grave_shovel'
        self.characteristics['projectile_damage'] = "+= 1"
        self.characteristics['projectile_speed'] = '-= 0.1'


class Casino(Item):
    id = 32

    def __init__(self) -> None:
        super().__init__()
        self.image = 'casino'

    def apply(self, player) -> None:
        super().apply(player)
        exec("""import random
c = random.randint(0, 6)
if c == 0:
    player.max_speed += random.uniform(-player.max_speed / 2, player.max_speed / 2)
elif c == 1:
    player.projectile_range += random.uniform(-player.projectile_range / 2, player.projectile_range / 2)
elif c == 2:
    player.projectile_speed += random.uniform(-player.projectile_speed / 2, player.projectile_speed / 2)
elif c == 3:
    player.projectile_size += random.uniform(-player.projectile_size / 2, player.projectile_size / 2)
elif c == 4:
    player.projectile_damage += random.uniform(-player.projectile_damage / 2, player.projectile_damage / 2)
elif c == 5:
    player.period += random.uniform(-player.period / 2, player.period / 2)
elif c == 6:
    player.max_hp += random.uniform(-player.max_hp / 2, player.max_hp / 2)""")
        if hasattr(player, 'period'):
            exec(f"import math; player.period = math.ceil(player.period)")

        if hasattr(player, 'projectile_size'):
            exec(f"import math; player.projectile_size = math.ceil(player.projectile_size)")

        if hasattr(player, 'projectile_damage'):
            exec("import math; player.projectile_damage = math.ceil(player.projectile_damage)")

        if hasattr(player, 'max_hp'):
            exec("import math; player.max_hp = math.ceil(player.max_hp)")


class RedGecko(ShotTypeItem):
    id = 33

    def __init__(self) -> None:
        super().__init__()
        self.image = 'red_gecko'
        self.characteristics['projectile_range'] = "*= 1.5"
        # add arc trajectory


class Flower(Item):
    id = 34

    def __init__(self) -> None:
        super().__init__()
        self.image = 'flower'
        self.characteristics['projectile_range'] = "-= 20"
        self.characteristics['projectile_damage'] = "+= 1"


class Syringe(Item):
    id = 35

    def __init__(self) -> None:
        super().__init__()
        self.image = 'syringe'
        self.characteristics['max_speed'] = "= 10"


class ChristmasTree(Item):
    id = 36

    def __init__(self) -> None:
        super().__init__()
        self.image = 'christmas_tree'
        self.characteristics['projectile_range'] = "+= 20"


class DecoratedChristmasTree(Item):
    id = 37

    def __init__(self) -> None:
        super().__init__()
        self.image = 'decorated_christmas_tree'
        self.characteristics['projectile_range'] = "+= 20"
        self.characteristics['projectile_damage'] = "+= 1"


class Scope(ShotTypeItem):
    id = 38

    def __init__(self) -> None:
        super().__init__()
        self.image = 'scope'
        self.characteristics['projectile_range'] = "+= 20"
        # reduces bullet spread


