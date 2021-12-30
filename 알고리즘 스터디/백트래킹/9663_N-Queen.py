import sys
sys.stdin = open('input.txt')

def dfs(cnt):
    global answer
    if cnt == n:    # 모든 체스를 다 두었다면
        answer += 1
        return

    for i in range(n):
        if visited[i]:  # 해당 열에 체스 이미 있다면
            continue
        idx[cnt] = i    # 없으면 해당 열에 체스 놓기
        for j in range(cnt):
            # 대각선의 경우 현재 인덱스의 합이 대각선 방향 각각의 인덱스의 합들과 같다는 규칙이 있다.
            if (idx[cnt] - cnt) == (idx[j] - j) or (idx[cnt] + cnt) == (idx[j] + j):
                break
        else:
            visited[i] = True
            dfs(cnt + 1)
            visited[i] = False


n = int(input())
visited = [False for _ in range(n)]
idx = [0 for _ in range(n)]
answer = 0
dfs(0)

print(answer)
