import json

from source.Calculations.Data import get_data, update_data
from source.Save.ModelSave import *


def save():
    data, sets = [[] for _ in range(6)], [[] for _ in range(3)]
    get_data(data, sets)

    with DB.atomic():
        Save.create(data=data, sets=sets)


def load():
    with DB.atomic():
        save_ = Save.select()[-1]
        data, sets = json.loads(save_.data), json.loads(save_.sets)

        update_data(data, sets)
