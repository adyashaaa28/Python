#dfs

def dfs(graph, start, goal):
    stack = [(start, [start])]  # Stack stores tuples: (current_node, path_so_far)
    visited = set()

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            if vertex == goal:
                return path  

            for neighbor in reversed(graph.get(vertex, [])): 
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None 


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

# Check if start and goal exist in the graph
if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node. Please enter valid nodes from the graph.")
else:
    path = dfs(graph, start_node, goal_node)

    if path:
        print("DFS Solution Path:", " -> ".join(path))
    else:
        print(f"No path found from {start_node} to {goal_node}.")

