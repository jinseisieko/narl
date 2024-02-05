import json

tasks = [
    {
        'id': "kill_100_enemies",
        'name': "kill 100 enemies",
        'description': "kill 100 enemies in a normal game",
        'data': json.dumps({
            "count": 0
        }),
        'fulfillment': False
    },

]
