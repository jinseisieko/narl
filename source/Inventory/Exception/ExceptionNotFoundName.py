from source.Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionNotFoundName(ExceptionPrototype):
    """Error describing id_ not found"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)