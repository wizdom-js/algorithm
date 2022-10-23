import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    queue = deque([[gangho, 0]])
    visited[gangho] = True

    while queue:
        floor, cnt = queue.popleft()

        if floor == startlink:
            return cnt

        move_up = floor + up_button
        move_down = floor - down_button
        if move_up <= height and not visited[move_up]:
            visited[move_up] = True
            queue.append([move_up, cnt + 1])
        if move_down > 0 and not visited[move_down]:
            visited[move_down] = True
            queue.append([move_down, cnt + 1])

    return "use the stairs"

height, gangho, startlink, up_button, down_button = map(int, input().split())
visited = [0 for _ in range(height + 1)]

print(bfs())