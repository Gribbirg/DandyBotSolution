from collections import deque


def script(check, x, y):
    """
    Main fun of action
    If is gold on position take it else moving
    :param check: fun for check position
    :param x: coords x
    :param y: coords y
    :return: action
    """
    if check("gold", x, y) != 0:
        return "take"
    return get_direction(check, x, y)


def get_direction(check, x, y):
    """
    Find direction to nearest gold
    :param check: fun for check position
    :param x: coords x
    :param y: coords y
    :return: direction
    """
    visited = set()
    queue = get_base_queue(x, y)

    while True:
        direction, (x, y) = queue.popleft()

        if check("gold", x, y):
            return direction
        if (x, y) in visited or check("wall", x, y):
            continue

        add_to_queue(queue, x, y, direction)
        visited.add((x, y))


def get_base_queue(x, y):
    """
    Get queue with base coordinates
    :param x: coords x
    :param y: coords y
    :return: start queue
    """
    queue = deque()

    directions = get_base_directions()
    neighbours = get_neighbours(x, y)
    for i in range(4):
        queue.append((directions[i], neighbours[i]))

    return queue


def add_to_queue(queue, x, y, direction):
    """
    Add all neighbours to queue
    :param queue: current queue
    :param x: coords x
    :param y: coords y
    :param direction: first step direction
    """
    for neighbour in get_neighbours(x, y):
        queue.append((direction, neighbour))


def get_neighbours(x, y):
    """
    Get all neighbours
    :param x: coords x
    :param y: coords y
    :return: neighbours coordinates
    """
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def get_base_directions():
    """
    :return: base directions names
    """
    return ["left", "right", "up", "down"]
