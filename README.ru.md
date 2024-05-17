# Решение Dandy Bot

[![ru](https://img.shields.io/badge/game-readme-green.svg)](game-info.md)
[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![ru](https://img.shields.io/badge/lang-ru-red.svg)](README.ru.md)

Моё простое универсальное решение здесь: [user_bot.py](user_bot.py).

## Основная идея

Используется BFS, чтобы найти ближайшее золото на каждом этапе.
Если золото было ближайшим на предыдущем шаге, после движения в его направлении оно останется ближайшим, пока мы не его соберем.
Также используется ```set``` с посещенными точками, чтобы не обрабатывать уже посещенные позиции.

Основная BFS функция:
```python
def get_direction(check, x, y):
    """
    Найти направление к ближайшему золоту
    :param check: ф-ция для проверки ячейки
    :param x: координата x
    :param y: координата y
    :return: направление
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
