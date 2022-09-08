def solution(alp, cop, problems):
    # 문제를 푸는데 필요한 최대 알고력과 코딩력 저장
    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    # 초기 알고력과 초기 코딩력이 최대 알고력, 코딩력보다 클 수 있으므로 세팅
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)

    # 최대 깊이 => 최대 알고력(코딩력) + 풀었을 때 증가하는 최대 알고력(코딩력) => 150 + 30
    dp = [[99999999999 for _ in range(181)] for _ in range(181)]
    # 초기 알고력, 코딩력 시간 0으로 세팅
    dp[alp][cop] = 0

    # for문 범위 => 초기 알고력(코딩력) ~ 최대 알고력(코딩력)
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고력, 코딩력 1 높이기
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            # 문제를 풀어서 알고력, 코딩력 높이기
            for [alp_req, cop_req, alp_rwd, cop_rwd, cost] in problems:
                # 해당 문제 풀 수 있는 능력이라면
                if i >= alp_req and j >= cop_req:
                    # 풀어서 얻은 알고력과 코딩력이 최대 알고력과 코딩력보다 크다면 max_alp, max_cop에 저장
                    # 문제를 풀어서 알고력과 코딩력이 최대보다 커지더라도 우리는 최대 알고력과 코딩력까지가 궁금한 것이기 때문
                    nxt_alp, nxt_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]