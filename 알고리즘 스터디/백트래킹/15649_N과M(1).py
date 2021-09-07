import sys
sys.stdin = open('input.txt')


def recur(cur):
    # m개 골랐다면 print
    if cur == m:
        print(*arr)
        return

    for i in range(n):
        if not visited[i]:  # 중복 아니라면
            visited[i] = True   # 방문 처리
            arr[cur] = i+1      # 리스트에 숫자 담기
            recur(cur + 1)      # 그 다음 숫자 들어가서 가져와
            visited[i] = False  # 다음에 쓰기 위해 방문 처리 해제

    # for i in range(1, n+1):
    #     if i not in arr:    # 해당 숫자가 고른 숫자가 아니라면
    #         arr[cur] = i    # 리스트에 숫자 넣기
    #         recur(cur + 1)  # 들어가서 다음 숫자 넣어
    #         arr[cur] = 0    # 리스트 쓸거니까 0으로 초기화


# 1부터 자연수 n까지, 중복없이 m개 고른 수열 구하기
n, m = map(int, input().split())
arr = [0 for _ in range(m)]     # m개 고른 수열 담을 리스트
visited = [False for _ in range(n)] # 중복 없어야하니, 방문처리할 리스트 만들어준다.

recur(0)

