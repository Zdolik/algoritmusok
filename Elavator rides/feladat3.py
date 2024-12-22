def min_elevator_rides(n, x, weights):

    dp = [(n + 1, 0)] * (1 << n)
    dp[0] = (1, 0) 

    for mask in range(1 << n): 
        for i in range(n):  #
            if not (mask & (1 << i)):  
                prev_mask = mask | (1 << i)
                current_rides, current_weight = dp[mask]
                person_weight = weights[i]
                
                if current_weight + person_weight <= x:
                   
                    dp[prev_mask] = min(dp[prev_mask], (current_rides, current_weight + person_weight))
                else:
                 
                    dp[prev_mask] = min(dp[prev_mask], (current_rides + 1, person_weight))

  
    return dp[(1 << n) - 1][0]

if __name__ == "__main__":
    n, x = map(int, input().split())
    weights = list(map(int, input().split()))
    print(min_elevator_rides(n, x, weights))