import json

from source.Calculations.Data import get_data, update_data
from source.Save.ModelSave import *


def save(game):
    data, sets = [[] for _ in range(6)], [[] for _ in range(3)]
    get_data(data, sets)

    with DB.atomic():
        Save.create(data=str(data), sets=str(sets),
                    items=str(game.player.characteristics.item_names).replace("'", '"'))


def load(game):
    with DB.atomic():
        saves_ = Save.select()
        if len(saves_) == 0:
            return 0
        save_ = saves_[-1]
        data, sets, items = json.loads(save_.data), json.loads(save_.sets), json.loads(save_.items)
        update_data(data, sets)
        game.player.characteristics.item_names = items
        return 1


def delete_all_save():
    with DB.atomic():
        for obj in Save.select():
            obj.delete_instance()
