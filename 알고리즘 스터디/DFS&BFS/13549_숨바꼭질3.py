import sys
sys.stdin = open('input.txt')

from collections import deque

# 목적지까지 최단거리(시간)을 구하는 것이기 때문에 bfs => 도착하자마자 탐색 종료하면 더 깊은 depth까지 가지 않아도 되므로

subin, sister = map(int, input().split())   # 수빈이와 동생의 위치
visited = [0 for _ in range(100001)]    # 방문처리 할 리스트

queue = deque([[subin, 0]]) # 수빈이가 이동 할 곳
while queue:
    now, time = queue.popleft()
    visited[now] = True # 수빈 지금 위치 방문 처리

    if now == sister:   # 동생을 만난 경우
        print(time)
        break

    # 위치 조건 0 <= x <= 100,000
    # 방문하지 않은 곳 가기
    if now < 50001 and not visited[now*2]:  # 순간이동
        queue.append([now*2, time])
    if now > 0 and not visited[now-1]:  # -1로 이동
        queue.append([now-1, time+1])
    if now < 100000 and not visited[now+1]: # +1로 이동
        queue.append([now+1, time+1])



def another_way():
    subin, sister = map(int, input().split())
    visited = [-1 for _ in range(100001)]   # 방문 리스트를 -1로 처리
    visited[subin] = 0  # 처음 수빈이의 위치 0으로 처리하고 계속해서 더해나가는 방식

    queue = deque([subin])
    while queue:
        now = queue.popleft()

        if now == sister:
            print(visited[now])
            break

        if now < 50001 and visited[now * 2] == -1:
            queue.append(now * 2)
            visited[now * 2] = visited[now]
        if now > 0 and visited[now - 1] == -1:
            queue.append(now - 1)
            visited[now - 1] = visited[now] + 1
        if now < 100000 and visited[now + 1] == -1:
            queue.append(now + 1)
            visited[now + 1] = visited[now] + 1
