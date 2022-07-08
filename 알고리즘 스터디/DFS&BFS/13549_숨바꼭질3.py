import sys
sys.stdin = open('input.txt')

from collections import deque

subin, sister = map(int, input().split())
visited = [0 for _ in range(100001)]

queue = deque([[subin, 0]])
while queue:
    now, time = queue.popleft()
    visited[now] = True

    if now == sister:
        print(time)
        break

    if now < 50001 and not visited[now*2]:
        queue.append([now*2, time])
    if now > 0 and not visited[now-1]:
        queue.append([now-1, time+1])
    if now < 100000 and not visited[now+1]:
        queue.append([now+1, time+1])


def another_way():
    subin, sister = map(int, input().split())
    visited = [-1 for _ in range(100001)]
    visited[subin] = 0

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
