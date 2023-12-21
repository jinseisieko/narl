from Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionDataScarcity(ExceptionPrototype):
    def __init__(self, name: str, *args: object) -> None:
        self.name: str = name
        super().__init__(*args)
