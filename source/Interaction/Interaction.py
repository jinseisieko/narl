from source.Game import GAME


class Interaction:
    def __init__(self) -> None:
        super().__init__()
        self.game = GAME

    def aboba(self):
        self.game.fps = 120
