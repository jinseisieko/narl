structure_command = input().split()

match structure_command:
    case (object_, name):
        print(1)
    case (object_, name, value):
        print(2)
    case (object_, name, value1, value2):
        print(3)
    case (object_, name, value1, value2, value3):
        print(4)
