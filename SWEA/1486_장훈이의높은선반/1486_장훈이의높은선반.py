import sys
sys.stdin = open('input.txt')


def bfs(i, top_h):
    global answer

    if b <= top_h:  # 점원들이 쌓은 탑의 합이 선반보다 높아졌다면
        answer = min(answer, top_h) # 최소 높이로 갱신
        return

    if i == n:  # 기저까지 들어왔다면 들어가
        return

    bfs(i+1, top_h+heights[i])  # 현재 키 선택하고 들어가
    bfs(i+1, top_h) # 현재 키 선택 X 들어가


tc = int(input())
for idx in range(1, tc+1):
    n, b = map(int, input().split())    # 점원의 수 n, 선반의 높이 b
    heights = list(map(int, input().split()))   # 점원들의 키

    answer = 99999999
    bfs(0, 0)
    print('#{} {}'.format(idx, abs(b-answer)))
