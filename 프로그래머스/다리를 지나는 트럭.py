from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    passing = deque([0] * bridge_length)
    bridge_w = 0
    
    while passing:
        time += 1
        move = passing.popleft()
        if move != 0 :
            bridge_w -= move
        
        if truck_weights:
            if bridge_w + truck_weights.front() <= weight:
                truck = truck_weights.popleft()
                passing.append(truck)
                bridge_w += truck
            else:
                passing.append(0)
    
    return time