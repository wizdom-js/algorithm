def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1    # 시작 지점 
    
    for i in range(1, n+1): # 행 
        for j in range(1, m+1): # 열
            if i == 1 and j == 1: continue;  # 시작점이면 스킵 
            if [j, i] in puddles:   # 물에 잠긴 지역이라면 거기 경로 수 0
                dp[i][j] = 0
            else:
                # 해당 지역 = (위의 경로 수 + 왼쪽의 경로 수) % 1000000007
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[-1][-1]