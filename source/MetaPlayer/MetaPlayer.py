class MetaPlayer:
    def __init__(self) -> None:
        super().__init__()
        self.name = "guest"

    def set(self, name, password):
        self.name = name
