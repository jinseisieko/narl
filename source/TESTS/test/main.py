import datetime

from model import *

DB.connect()

with DB.atomic():
    u = User.create(username="james",
                    password="qwe123",
                    email="james@mail.org",
                    join_date=datetime.datetime.now(), )
    u2 = User.create(username="caren",
                     password="qwe123",
                     email="caren@mail.org",
                     join_date=datetime.datetime.now(), )
    r = Relationship.create(from_user=u, to_user=u2)

with DB.atomic():
    for r in Relationship.select():
        r: Relationship
        print(r, r.from_user.username, r.to_user.username)


DB.close()
