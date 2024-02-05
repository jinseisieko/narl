import json

achievements = [
    {
        'id': "kill_1000_enemies",
        'name': "kill 1000 enemies",
        'description': "kill 1000 enemies in a normal game",
        'data': json.dumps({
            "count": 0
        }),
        'fulfillment': False
    },

]
