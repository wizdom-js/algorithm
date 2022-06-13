import heapq as hq

def solution(scoville, K):
    count = 0
    hq.heapify(scoville)

    while True :
        a = hq.heappop(scoville)
        if a >= K :
            return count
        
        if len(scoville) == 0 :
            return -1
        
        b = hq.heappop(scoville)
        hq.heappush(scoville, a + b*2)
        count += 1