from improvements import get_improvement


def reproduce_command(command, player):
    print(command)
    try:
        split_command = command.split()
        name_obj, name_command, values = split_command[0], split_command[1], split_command[2:]

    except Exception as e:
        name_obj, name_command, values = None, None, None
        print(e)

    if name_obj == "player":
        if name_command == "additem":
            player.add_improvement(get_improvement(int(values[0])))

        if name_command == "set":
            if values[0] == "speed":
                player.default_speed = int(values[1])

            if values[0] == "prange":
                player.default_range_projectile = int(values[1])

            if values[0] == "pspeed":
                player.default_speed_projectile = int(values[1])

            if values[0] == "psize":
                player.default_size_projectile = int(values[1])

            if values[0] == "period":
                player.default_period = int(values[1])
