class ExceptionNonRank(Exception):
    """impossible rank"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)