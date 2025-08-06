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
                (prev_a, prev_b) = parent[(a, b)] if parent[(a, b)] is not None else (None, None)
                if prev_a is None:
                    break
                a, b = prev_a, prev_b
            path.reverse()
            return path

        next_states = [
            (jug1_capacity, b),  # Fill Jug 1
            (a, jug2_capacity),  # Fill Jug 2
            (0, b),              # Empty Jug 1
            (a, 0),              # Empty Jug 2
            # Pour Jug 1 into Jug 2
            (a - min(a, jug2_capacity - b), b + min(a, jug2_capacity - b)),
            # Pour Jug 2 into Jug 1
            (a + min(b, jug1_capacity - a), b - min(b, jug1_capacity - a)),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)
    return None

# --- User Input Section ---

jug1 = int(input("Enter Jug 1 capacity: "))
jug2 = int(input("Enter Jug 2 capacity: "))
target = int(input("Enter target volume: "))

solution = water_jug_bfs(jug1, jug2, target)
if solution:
    print("Steps to reach target:")
    for step in solution:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("No solution possible or invalid logic.")
