from peewee import *
DB
with DB.atomic():
    caren: User = next(iter(User.select().where(User.username == "caren")))
    print("original:", caren.username)

    for u in User.select().where(User.username == "james"):
        for r in u.relationships:
            r: Relationship
            print("relation:", r, r.from_user.username, r.to_user.username)

            to_user: User = r.to_user
            to_user.username = "ilona"
            to_user.save()
            print("renamed as ilona...")

    caren = User.get(int(str(caren)))  # refresh user fields
    print("refreshed:", caren.username)
    caren.username = "caren"
    caren.save()  # undone changes
    print("renamed back as caren")