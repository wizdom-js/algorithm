import sys
sys.stdin = open('input.txt')

def dfs(cnt):   # cnt => 행
    global answer
    if cnt == n:    # 모든 체스를 다 두었다면
        answer += 1
        return

    for i in range(n):
        if visited[i]:  # 해당 열에 체스 이미 있다면 패스
            continue
        idx[cnt] = i    # 없으면 해당 열에 체스 놓기
        for j in range(cnt):
            # 대각선 체크
            # 대각선의 경우 두 좌표에서 행 - 행 = 열 - 열이 같으면 두개는 같은 대각선상에 있다
            if (idx[cnt] - cnt) == (idx[j] - j) or (idx[cnt] + cnt) == (idx[j] + j):
                break
        else:
            visited[i] = True   # 현재 열 방문처리
            dfs(cnt + 1)    # 다음 행 고고
            visited[i] = False  # 다음 사용을 위해 해제


n = int(input())    # n x n 체스판 위에 퀸 n개
visited = [False for _ in range(n)] # 열 방문처리할 리스트
idx = [0 for _ in range(n)] # 대각선 계산을 위한 리스트
answer = 0
dfs(0)

print(answer)
