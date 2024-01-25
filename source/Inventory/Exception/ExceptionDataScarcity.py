from source.Inventory.Exception.ExceptionPrototype import ExceptionPrototype


class ExceptionDataScarcity(ExceptionPrototype):
    """Error describing a deficiency in the submitted data set"""

    def __init__(self, name: str, *args: object) -> None:
        super().__init__(*args)
        self.name: str = name
