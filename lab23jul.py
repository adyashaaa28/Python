from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    parent = dict()

    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))
    parent[(0, 0)] = None

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            while (a, b) is not None:
                path.append((a, b))
                prev = parent[(a, b)]
                if prev is None:
                    break
                a, b = prev
            path.reverse()
            return path

        next_states = [
            (jug1_capacity, b),
            (a, jug2_capacity),
            (0, b),
            (a, 0),
            (0, a + b) if a + b <= jug2_capacity else (a - (jug2_capacity - b), jug2_capacity),
            (a + b, 0) if a + b <= jug1_capacity else (jug1_capacity, b - (jug1_capacity - a)),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)

    return None


jug1 = 4
jug2 = 3
target = 2

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print("Steps to reach target:")
    for step in solution:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("No solution possible or logic error occurred.")
