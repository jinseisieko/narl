import random

from source.Inventory.Exception.ExceptionNonRank import ExceptionNonRank
from source.Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName


class GetItems:
    def __init__(self) -> None:
        self.names: list = []
        self.rank1: list = []
        self.rank2: list = []
        self.rank3: list = []
        self.blocked: list = []
        self.unlocked: list = []

    def add(self, id_: str, rank: int, blocked: bool = True):
        self.names.append(id_)

        if rank == 1:
            self.rank1.append(id_)
        elif rank == 2:
            self.rank2.append(id_)
        elif rank == 3:
            self.rank3.append(id_)
        elif rank == -1:
            if blocked:
                self.blocked.append(id_)
            else:
                self.unlocked.append(id_)
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
            elif rank == -1:
                return random.choice(self.unlocked)
            else:
                raise ExceptionNonRank(f"impossible rank {rank}")

    def get_rank(self, name: str):
        if name in self.rank1:
            return 1
        elif name in self.rank2:
            return 2
        elif name in self.rank3:
            return 3
        elif name in self.unlocked:
            return -1
        else:
            raise ExceptionNotFoundName(f'not found name {name}')

    def get_rank_random(self, r1=1, r2=1, r3=1, r_1=1):
        rank = random.choice([1] * r1 + [2] * r2 + [3] * r3 + [-1] * r_1)
        print(self.unlocked)
        if rank == -1 and len(self.unlocked) == 0:
            rank = random.choice([1] * r1 + [2] * r2 + [3] * r3)
        return self.get_random(rank), rank
