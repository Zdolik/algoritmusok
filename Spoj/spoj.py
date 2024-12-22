import heapq
import sys

def safest_path(n, m, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for a, b, p in edges:
        probability = p / 100
        graph[a].append((b, probability))
        graph[b].append((a, probability))
    
    pq = [(-1, 1)] 
    max_prob = [0] * (n + 1)
    max_prob[1] = 1
    
    while pq:
        prob, node = heapq.heappop(pq)
        prob = -prob 
        
        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))
    
    return max_prob[n] * 100

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    results = []
    i = 0
    while i < len(data):
        line = data[i].strip()
        i += 1
        
        if line == "0":
            break
        
        n, m = map(int, line.split())
        edges = []
        for _ in range(m):
            a, b, p = map(int, data[i].strip().split())
            i += 1
            edges.append((a, b, p))
        
        result = safest_path(n, m, edges)
        results.append(f"{result:.6f} percent")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()