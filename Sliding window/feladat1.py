import heapq

def min_total_cost(n, k, arr):
    costs = []
    left_heap, right_heap = [], []
    left_sum, right_sum = 0, 0
    
    def balance():
        while len(left_heap) > len(right_heap) + 1:
            val = -heapq.heappop(left_heap)
            left_sum -= val
            heapq.heappush(right_heap, val)
            right_sum += val
        while len(right_heap) > len(left_heap):
            val = heapq.heappop(right_heap)
            right_sum -= val
            heapq.heappush(left_heap, -val)
            left_sum += val

    def insert(value):
        nonlocal left_sum, right_sum
        if not left_heap or value <= -left_heap[0]:
            heapq.heappush(left_heap, -value)
            left_sum += value
        else:
            heapq.heappush(right_heap, value)
            right_sum += value
        balance()

    def remove(value):
        nonlocal left_sum, right_sum
        if value <= -left_heap[0]:
            left_heap.remove(-value)
            heapq.heapify(left_heap)
            left_sum -= value
        else:
            right_heap.remove(value)
            heapq.heapify(right_heap)
            right_sum -= value
        balance()
    
    for i in range(n):
        insert(arr[i])
        if i >= k - 1:
            median = -left_heap[0]
            cost = median * len(left_heap) - left_sum + right_sum - median * len(right_heap)
            costs.append(cost)
            remove(arr[i - k + 1])
    return costs

# Bemenet kezelése
n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = min_total_cost(n, k, arr)
print(" ".join(map(str, result)))