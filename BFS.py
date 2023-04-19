def bfs(start, tree):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for child_node in tree[node]:
                if child_node not in visited:
                    queue.append(child_node)
    print("bfs traversed is: ", visited)


def bfs_search(start, goal, tree):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node is goal:
                print("node ", goal, " found the path -> ", visited)
                return
            for child_node in tree[node]:
                if child_node not in visited:
                    queue.append(child_node)
    print("not found ", goal)


tree = {
    "A": ["B", "D"],
    "B": ["C"],
    "C": [],
    "D": ["E", "F"],
    "E": ["F", "G"],
    "F": ["H"],
    "G": ["H"],
    "H": []
}

start = input("Enter the source node: ")
goal = input("Enter the goal node: ")

bfs(start, tree)
bfs_search(start, goal, tree)
