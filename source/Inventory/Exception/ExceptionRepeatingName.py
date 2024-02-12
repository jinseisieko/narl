from source.Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionRepeatingName(ExceptionPrototype):
    """Repeated id_ error"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
