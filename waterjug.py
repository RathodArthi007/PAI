from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path

        next_states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in next_states:
            queue.append((state, path))

solution = water_jug_bfs(4, 3, 2)

print("Solution Steps:")
for step in solution:
    print(step)
