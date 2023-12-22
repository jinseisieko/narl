from InventoryClasses.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionRepeatingName(ExceptionPrototype):
    """Repeated name error"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
