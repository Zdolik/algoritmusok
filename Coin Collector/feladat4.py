import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, graph, coins, visited, dp):
    if visited[node]:
        return dp[node]
    visited[node] = True
    
    # Maximum coins starting from this room
    max_coins = coins[node]
    for neighbor in graph[node]:
        max_coins = max(max_coins, coins[node] + dfs(neighbor, graph, coins, visited, dp))
    
    dp[node] = max_coins
    return dp[node]

def max_coins(n, m, coins, edges):
    # Graph initialization
    graph = defaultdict(list)
    for a, b in edges:
        graph[a - 1].append(b - 1)
    
    # Dynamic programming and visited arrays
    dp = [-1] * n
    visited = [False] * n
    
    # Perform DFS on all nodes
    result = 0
    for i in range(n):
        result = max(result, dfs(i, graph, coins, visited, dp))
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(max_coins(n, m, coins, edges))