import sys
sys.stdin = open('input.txt')

unit_n, total_time = map(int, input().split())  # 시험 단원 개수, 공부 할 수 있는 총 시간

# 2차원으로 풀기 top-down 방식 
# dp = [[0 for _ in range(total_time+1)] for _ in range(unit_n+1)]
# arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(unit_n)]   # [공부 시간, 문제 배점]

# for i in range(1, unit_n+1):
#     t = arr[i][0]   # 현재 단원 예상 공부 시간
#     s = arr[i][1]   # 현재 단원 문제의 배점 
#     for j in range(1, total_time+1):
#         if j < t:   # 시간 j보다 현재 시간이 더 든다면 
#             dp[i][j] = dp[i-1][j]   # 이전 배점으로 채우기 
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-t]+s)  # 이전 시간에서의 배점 vs 현재 단원 예상 공부 시간을 빼고 현재 배점 더하기 

# print(dp[-1][-1])


## 1차원으로 풀기 bottom-up 방식
# 각 물건을 1번씩 밖에 사용하지 못하므로 1차원 리스트로 풀이할 경우 거꾸로 탐색하면서 풀어야한다. 
# 가방 용량을 최대부터 1까지 큰쪽에서 작은 쪽의 순서로 살펴보기
''''''
arr = []
for _ in range(unit_n):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [0 for _ in range(total_time + 1)] 
for w, v in arr:
    for i in range(total_time, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)   # 기존의 dp[i]와 물건을 넣는 dp[i-w]+v를 비교하여 더 큰값으로 갱신 

print(dp[-1])