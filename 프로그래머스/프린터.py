from collections import deque

def solution(priorities, location):
    queue = deque(list(map(tuple, enumerate(priorities))))  # 중요도와 순서 튜플로 묶기
    answer = 0
    while True:
        tmp = queue.popleft()   # 문서 꺼내기
        for q in queue:
            if tmp[1] < q[1]:   # 다음 문서가 더 중요도가 높다면 뒤로 보내기
                queue.append(tmp)
                break
        else:   # 꺼낸 문서가 중요도 가장 높다면
            answer += 1 # 순서 +1
            if tmp[0] == location:  # 원하는 문서라면
                return answer