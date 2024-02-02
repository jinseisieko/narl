class Level:
    def __init__(self) -> None:
        self.background = []
        self.obstacles = []
        self.number = -1
        self.difficulty = 0
        self.enemies_types = (0, 1)
        self.count_waves = 1
        self.next = None


class Level1(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ["grass1",
                           "grass2",
                           "grass3",
                           "grass4", ]
        self.obstacles = ...  # ...
        self.number = 1
        self.difficulty = 1
        self.enemies_types = (0, 2)
        self.count_waves = 1
        self.next = Level2


class Level2(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ['forest2'] * 20 + ['forest1',
                                              'forest2',
                                              'forest3',
                                              'forest4',
                                              'forest5',
                                              'forest6',
                                              'forest7',
                                              'forest8',
                                              'forest9',
                                              'forest10',
                                              'forest11',
                                              'forest12',
                                              'forest13',
                                              'forest14',
                                              'forest15',
                                              ]
        self.obstacles = ...  # ...
        self.number = 2
        self.difficulty = 1
        self.enemies_types = (3, 5)
        self.count_waves = 10
