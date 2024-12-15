import sys
sys.setrecursionlimit(300000)

def count_paths(n, k, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent, steps_left):
        if steps_left == 0:
            return 1
        
        count = 0
        for neighbor in graph[node]:
            if neighbor != parent: 
                count += dfs(neighbor, node, steps_left - 1)
        return count

    total_paths = 0
    for start_node in range(1, n + 1):
        total_paths += dfs(start_node, -1, k)

    return total_paths // 2

if __name__ == "__main__":
    n, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    result = count_paths(n, k, edges)
    print(result) 