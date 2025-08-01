#bfs

from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # Each element is (node, path_so_far)
    visited = set()

    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)

            if vertex == goal:
                return path

            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No path found

# --- Input Section ---

# Enter the graph
print("Enter the graph as adjacency list (example: A:B,C B:D,E C:F ...):")
raw_input = input("Graph: ").strip()

# Parse the input and build the graph
graph = {}
all_nodes = set()

for item in raw_input.split():
    if ':' in item:
        node, neighbors = item.split(":")
        node = node.strip().upper()
        neighbor_list = [n.strip().upper() for n in neighbors.split(",") if n.strip()]
        graph[node] = neighbor_list
        all_nodes.add(node)
        all_nodes.update(neighbor_list)

# Ensure all nodes are in the graph (even if they have no children)
for node in all_nodes:
    if node not in graph:
        graph[node] = []

# Input start and goal
start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

# Validate and run BFS
if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node.")
else:
    path = bfs(graph, start_node, goal_node)

    if path:
        print("BFS Solution Path:", " -> ".join(path))
    else:
        print(f"No path found from {start_node} to {goal_node}.")