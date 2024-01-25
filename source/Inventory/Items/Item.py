from source.Inventory.Exception.ExceptionDataScarcity import ExceptionDataScarcity
from source.Inventory.Exception.ExceptionNotUnannounced import ExceptionNotUnannounced


class Item:
    """improves the performance of objects"""

    def __init__(self, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
                 code: str = '') -> None:
        """renewal_plus: dictionary where the key is the name of the variable
         and the value is an additive number
        renewal_multiply: dictionary where the key is the name of the variable
         and the value is the number to multiply by
        renewal_super: significances that are indicative and affect the process or mechanics of the game"""

        super().__init__()
        self.name: str = name
        self.renewal_plus: dict = renewal_plus
        self.renewal_multiply: dict = renewal_multiply
        self.renewal_super: dict = renewal_super
        self.code: str = code

        if self.name is None:
            raise ExceptionNotUnannounced('self.name cannot be an empty string')

    def apply(self, **kwargs) -> dict:
        """a method of using an object to increase its performance"""

        for name_field, value in self.renewal_plus.items():
            if not (name_field in kwargs):
                raise ExceptionDataScarcity(name_field, f"'{name_field}' needs, name item: {self.name}")
            kwargs[name_field] += value

        for name_field, value in self.renewal_multiply.items():
            if not (name_field in kwargs):
                raise ExceptionDataScarcity(name_field, f"'{name_field}' needs, name item: {self.name}")
            if type(kwargs[name_field]) is int:
                kwargs[name_field] *= value
                kwargs[name_field] = int(kwargs[name_field])
                continue
            kwargs[name_field] *= value

        for name_field, value in self.renewal_super.items():
            if not (name_field in kwargs):
                raise ExceptionDataScarcity(name_field, f"'{name_field}' needs, name item: {self.name}")
            kwargs[name_field] = value

        player = kwargs
        exec(self.code)

        return kwargs

    def __repr__(self) -> str:
        return f"${self.name}, {self.renewal_plus}, {self.renewal_multiply}, {self.renewal_super}, '{self.code}'$"