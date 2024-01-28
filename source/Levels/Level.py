class Level:
    def __init__(self) -> None:
        self.background = []
        self.obstacles = []
        self.difficulty = 0


class Level1(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ["grass1",
                           "grass2",
                           "grass3",
                           "grass4", ]
        self.obstacles = ...  # ...
        self.difficulty = 1


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
        self.difficulty = 1
