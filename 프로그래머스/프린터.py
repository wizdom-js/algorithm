from collections import deque

def solution(priorities, location):
    queue = deque(list(map(tuple, enumerate(priorities))))
    answer = 0
    while True:
        tmp = queue.popleft()
        for q in queue:
            if tmp[1] < q[1]:
                queue.append(tmp)
                break
        else:
            answer += 1
            if tmp[0] == location:
                return answer