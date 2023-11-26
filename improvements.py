# Улучшения


# айди предметов
def get_improvement(id_):
    if id_ == RedShellImprovement.id:
        return RedShellImprovement()
    elif id_ == BlueShellImprovement.id:
        return BlueShellImprovement()
    elif id_ == YellowShellImprovement.id:
        return YellowShellImprovement()
    elif id_ == PurpleShellImprovement.id:
        return PurpleShellImprovement()
    elif id_ == GreenShellImprovement.id:
        return GreenShellImprovement()
    elif id_ == ScopeImprovement.id:
        return ScopeImprovement()
    elif id_ == BigScopeImprovement.id:
        return BigScopeImprovement()
    elif id_ == OpticalScopeImprovement.id:
        return OpticalScopeImprovement()
    elif id_ == MilitaryScopeImprovement.id:
        return MilitaryScopeImprovement()
    elif id_ == TechnicalScopeImprovement.id:
        return TechnicalScopeImprovement
    elif id_ == AtomShotImprovement.id:
        return AtomShotImprovement()
    elif id_ == MilkImprovement.id:
        return MilkImprovement()
    elif id_ == BoomerangShotImprovement.id:
        return BoomerangShotImprovement()
    elif id_ == WeightImprovement.id:
        return WeightImprovement()
    elif id_ == HeavyWeightImprovement.id:
        return HeavyWeightImprovement()
    elif id_ == VeryHeavyWeightImprovement.id:
        return VeryHeavyWeightImprovement()
    elif id_ == SuperVeryHeavyWeightImprovement.id:
        return SuperVeryHeavyWeightImprovement()


class Improvement:
    def __init__(self):
        super().__init__()
        self.parent = "Improvement"

    def start(self, player):
        pass


class ShotImprovement:
    def __init__(self):
        super().__init__()
        self.parent = "ShotImprovement"


# Красная Ракушка
class RedShellImprovement(Improvement):
    id = 0

    def __init__(self):
        super().__init__()
        self.add_period = 3
        self.color = [255, 0, 0]

    def start(self, player):
        super().start(player)
        player.period -= self.add_period
        player.color_projectile = [(player.color_projectile[0] + self.color[0]) // 2,
                                   (player.color_projectile[1] + self.color[1]) // 2,
                                   (player.color_projectile[2] + self.color[2]) // 2]


# Синяя Ракушка
class BlueShellImprovement(Improvement):
    id = 1

    def __init__(self):
        super().__init__()
        self.add_period = 3
        self.color = [0, 0, 255]

    def start(self, player):
        super().start(player)
        player.period -= self.add_period
        player.color_projectile = [(player.color_projectile[0] + self.color[0]) // 2,
                                   (player.color_projectile[1] + self.color[1]) // 2,
                                   (player.color_projectile[2] + self.color[2]) // 2]


# Зеленая Ракушка
class GreenShellImprovement(Improvement):
    id = 2

    def __init__(self):
        super().__init__()
        self.add_period = 3
        self.color = [0, 255, 0]

    def start(self, player):
        super().start(player)
        player.period -= self.add_period
        player.color_projectile = [(player.color_projectile[0] + self.color[0]) // 2,
                                   (player.color_projectile[1] + self.color[1]) // 2,
                                   (player.color_projectile[2] + self.color[2]) // 2]


# Фиолетовая Ракушка
class PurpleShellImprovement(Improvement):
    id = 3

    def __init__(self):
        super().__init__()
        self.add_period = 3
        self.color = [255, 0, 255]

    def start(self, player):
        super().start(player)
        player.period -= self.add_period
        player.color_projectile = [(player.color_projectile[0] + self.color[0]) // 2,
                                   (player.color_projectile[1] + self.color[1]) // 2,
                                   (player.color_projectile[2] + self.color[2]) // 2]


# Желтая Ракушка
class YellowShellImprovement(Improvement):
    id = 4

    def __init__(self):
        super().__init__()
        self.add_period = 3
        self.color = [255, 255, 0]

    def start(self, player):
        super().start(player)
        player.period -= self.add_period
        player.color_projectile = [(player.color_projectile[0] + self.color[0]) // 2,
                                   (player.color_projectile[1] + self.color[1]) // 2,
                                   (player.color_projectile[2] + self.color[2]) // 2]


# Прицел
class ScopeImprovement(Improvement):
    id = 6

    def __init__(self):
        super().__init__()
        self.add_range = 20

    def start(self, player):
        super().start(player)
        player.range_projectile += self.add_range


# Оптический Прицел
class OpticalScopeImprovement(Improvement):
    id = 7

    def __init__(self):
        super().__init__()
        self.add_range = 30

    def start(self, player):
        super().start(player)
        player.range_projectile += self.add_range


# Военный Прицел
class MilitaryScopeImprovement(Improvement):
    id = 8

    def __init__(self):
        super().__init__()
        self.add_range = 30
        self.add_damage = 0.1

    def start(self, player):
        super().start(player)
        player.range_projectile += self.add_range
        player.damage += self.add_damage


# Технический Прицел
class TechnicalScopeImprovement(Improvement):
    id = 9

    def __init__(self):
        super().__init__()
        self.add_range = 15
        self.add_period = 2

    def start(self, player):
        super().start(player)
        player.range_projectile += self.add_range
        player.period -= self.add_period


# Большой Прицел
class BigScopeImprovement(Improvement):
    id = 10

    def __init__(self):
        super().__init__()
        self.add_range = 20

    def start(self, player):
        super().start(player)
        player.range_projectile += self.add_range


# Молоко
class MilkImprovement(Improvement):
    id = 17

    def __init__(self):
        super().__init__()
        self.mult_period = 3
        self.speed_projectile = 4

    def start(self, player):
        super().start(player)
        player.period /= self.mult_period
        player.speed_projectile = self.speed_projectile


# Бумеранг
class BoomerangShotImprovement(ShotImprovement):
    id = 5

    def __init__(self):
        super().__init__()
        self.ageing_factor = 1 / 3
        self.name = "Boomerang"

    def get_ageing_factor(self):
        return self.ageing_factor


# Атом
class AtomShotImprovement(ShotImprovement):
    id = 11

    def __init__(self):
        super().__init__()
        self.name = "Atom"


# Гиря
class WeightImprovement(Improvement):
    id = 12

    def __init__(self):
        super().__init__()
        self.add_size = 1

    def start(self, player):
        super().start(player)
        player.size_projectile = [player.size_projectile[0] + self.add_size, player.size_projectile[1] + self.add_size]


# Тяжелая Гиря
class HeavyWeightImprovement(Improvement):
    id = 13

    def __init__(self):
        super().__init__()
        self.add_size = 2

    def start(self, player):
        super().start(player)
        player.size_projectile = [player.size_projectile[0] + self.add_size, player.size_projectile[1] + self.add_size]


# Очень Тяжелая Гиря
class VeryHeavyWeightImprovement(Improvement):
    id = 14

    def __init__(self):
        super().__init__()
        self.add_size = 3

    def start(self, player):
        super().start(player)
        player.size_projectile = [player.size_projectile[0] + self.add_size, player.size_projectile[1] + self.add_size]


# СУПЕР Очень Тяжелая Гиря
class SuperVeryHeavyWeightImprovement(Improvement):
    id = 15

    def __init__(self):
        super().__init__()
        self.add_size = 4

    def start(self, player):
        super().start(player)
        player.size_projectile = [player.size_projectile[0] + self.add_size, player.size_projectile[1] + self.add_size]
