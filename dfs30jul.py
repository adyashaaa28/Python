def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            # Add neighbors to stack in reversed order to match DFS
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# === USER INPUT ===
raw_input_data = input("Enter the graph as adjacency list (e.g. A:B,C B:D,E C:F): ").strip()
graph = {}
all_nodes = set()
for item in raw_input_data.split():
    if ':' in item:
        node, neighbors = item.split(":")
        node = node.strip().upper()
        neighbor_list = [n.strip().upper() for n in neighbors.split(",") if n.strip()]
        graph[node] = neighbor_list
        all_nodes.add(node)
        all_nodes.update(neighbor_list)
for node in all_nodes:
    if node not in graph:
        graph[node] = []

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node.")
else:
    path = dfs(graph, start_node, goal_node)
    if path:
        print("DFS Solution Path:", " -> ".join(path)) 
    else:
        print(f"No path found from {start_node} to {goal_node}.")
