from Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionNotFoundName(ExceptionPrototype):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)