import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(num, cnt):
    queue = deque([(num, cnt)]) # 처음 시작 숫자 넣어주기
    while queue:
        num, cnt = queue.popleft()  # queue에 담겨있는거 꺼내기
        if num == m:    # 그 숫자가 목표 숫자라면
            return cnt  # 연산 횟수 return

        num_temp = num  # 연산 네번 해야 하니까 임시 변수에 현재 숫자로 초기화
        for i in range(4):
            if i == 0:
                num_temp += 1
            elif i == 1:
                num_temp -= 1
            elif i == 2:
                num_temp *= 2
            else:
                num_temp -= 10

            if 0 < num_temp < 1000001 and not visited[num_temp]:    # 범위 안에 있고, 방문 안한 곳이라면
                queue.append((num_temp, cnt+1)) # queue에 담기
                visited[num_temp] = 1   # 방문처리

            num_temp = num  # 초기화


def bfs1(num, cnt):
    queue = deque([(num, cnt)]) # 처음 시작 숫자 넣어주기
    while queue:
        num, cnt = queue.popleft()  # queue에 담겨있는거 꺼내기
        if num == m:    # 그 숫자가 목표 숫자라면
            return cnt  # 연산 횟수 return

        operators = [num+1, num-1, num*2, num-10]
        for nxt_num in operators:
            if 0 < nxt_num < 1000001 and not visited[nxt_num]:    # 범위 안에 있고, 방문 안한 곳이라면
                queue.append((nxt_num, cnt+1)) # queue에 담기
                visited[nxt_num] = 1   # 방문처리


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())    # 시작 숫자 n, 목표 숫자 m
    visited = [0 for _ in range(1000001)]   # 방문 처리 (연산했던 숫자 또 연산 하는거 방지)
    visited[n] = 1  # 시작 숫자 자리 방문
    print('#{} {}'.format(idx, bfs1(n, 0)))
