from collections import deque


def script(check, x, y):
    if check("gold", x, y) != 0:
        return "take"
    return get_direction(check, x, y)


def get_direction(check, x, y):
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
    queue = deque()

    directions = get_base_directions()
    neighbours = get_neighbours(x, y)
    for i in range(4):
        queue.append((directions[i], neighbours[i]))

    return queue


def add_to_queue(queue, x, y, direction):
    for neighbour in get_neighbours(x, y):
        queue.append((direction, neighbour))


def get_neighbours(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def get_base_directions():
    return ["left", "right", "up", "down"]
