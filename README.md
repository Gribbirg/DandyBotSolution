# Dandy Bot Solution

[![ru](https://img.shields.io/badge/game-readme-green.svg)](game-info.md)
[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![ru](https://img.shields.io/badge/lang-ru-red.svg)](README.ru.md)

My simple universal solution for this task placed here: [user_bot.py](user_bot.py).

## Main idea

BFS is used to find nearest gold at each step.
If gold was nearest at previous step after moving in it direction it will remain the closest until we collect it.
Also set is used with visited points to avoid entering positions that have already been visited.

Main BFS function:

```python
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
```
