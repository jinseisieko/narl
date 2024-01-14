import random

from Inventory.Exception.ExceptionNonRank import ExceptionNonRank
from Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName


class GetItems:
    def __init__(self) -> None:
        self.names: list = []
        self.rank1: list = []
        self.rank2: list = []
        self.rank3: list = []

    def add(self, name: str, rank: int):
        self.names.append(name)

        if rank == 1:
            self.rank1.append(name)
        elif rank == 2:
            self.rank2.append(name)
        elif rank == 3:
            self.rank3.append(name)
        else:
            raise ExceptionNonRank(f"impossible rank {rank}")

    def get_random(self, rank=None):
        if rank is None:
            return random.choice(self.names)
        else:
            if rank == 1:
                return random.choice(self.rank1)
            elif rank == 2:
                return random.choice(self.rank2)
            elif rank == 3:
                return random.choice(self.rank3)
            else:
                raise ExceptionNonRank(f"impossible rank {rank}")

    def get_rank(self, name: str):
        if name in self.rank1:
            return 1
        elif name in self.rank2:
            return 2
        elif name in self.rank3:
            return 3
        else:
            raise ExceptionNotFoundName(f'not found name {name}')

    def get_rank_random(self, r1=1, r2=1, r3=1):
        rank = random.choice([1] * r1 + [2] * r2 + [3] * r3)
        return self.get_random(rank), rank
