import sys
sys.stdin = open('input.txt')

n = int(input())    # 사람과 일의 수 n
d = [list(map(int, input().split())) for _ in range(n)] # 각 사람(행)마다의 일(열)

dp = [[1e9 for _ in range(1 << n)] for _ in range(20)]

def recur(cnt, visit):
    # if cnt == n:
    if visit == (1 << n) - 1: # 사람들에게 모든 일 배분 다 했다면
        return 0

    if dp[cnt][visit] != 1e9:    # 메모이제이션 해놓은 값이 있다면 꺼내 쓰기
        return dp[cnt][visit]


    for i in range(n):  # 처음 저장하는 경우라면 모든 노드를 순회
        bit = 1 << i    # i번째 원소 표현

        # if visited:
        if visit & bit:  # 이미 일 배정 되어 있다면 skip (방문 했다면 skip 역할)
            continue

        # 비용 최솟값으로 갱신
        # 현재 비용 + 다음 사람 일 배분 비용(남은 노드 방문) vs 저장된 값
        dp[cnt][visit] = min(recur(cnt + 1, visit | bit) + d[cnt][i], dp[cnt][visit])
        # tmp = recur(cnt + 1, visit | bit) + d[cnt][i]   # 현재 비용 + 다음 사람 일 배분 비용(남은 노드 방문)
        # if tmp < dp[cnt][visit]:
        #     dp[cnt][visit] = tmp

    return dp[cnt][visit]   # cnt에서 앞으로 다른 노드들(visit)을 방문할 때의 최소비용 반환

print(recur(0, 0))

