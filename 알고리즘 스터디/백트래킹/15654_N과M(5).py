import sys
sys.stdin = open('input.txt')

def recur(cnt):
    if cnt == m:
        print(*answer)
        return

    for i in range(n):
        # 고른 숫자 아니라면
        if not visited[i]:
            visited[i] = True   # 방문처리해
            answer[cnt] = arr[i]    # 숫자 넣어
            recur(cnt+1)            # 다음 숫자 넣으러 가
            visited[i] = False      # 해당 숫자 다음번에 또 써야하니 방문처리 풀어


# 1부터 자연수 n까지, m개 고른 수열 구하기
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))   # 오름차순이니 정렬해준다.
visited = [False for _ in range(n)] # 중복 없어야하니, 방문처리 리스트 만들기
answer = [0 for _ in range(m)]

recur(0)