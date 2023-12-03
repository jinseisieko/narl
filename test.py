def get_to_draw(items) -> list[str]:
    array_draw: list[str] = []
    for i in range(len(items) // 5):
        array_draw += [items[i * 5:i * 5 + 5]]
    if len(items) % 5 != 0:
        array_draw += [items[-(len(items) % 5):]]

    return array_draw

if __name__ == '__main__':
    print(get_to_draw([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))