from Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionRepeatingName(ExceptionPrototype):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
