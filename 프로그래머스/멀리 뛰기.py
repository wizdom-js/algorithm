def solution(n):
    # n + 2로 한 이유 => n이 1인 경우 4번째 줄에서 에러 나기 떄문
    # if n < 3 : return n 해도 되지만 코드 간결화를 위함
    dp = [0 for _ in range(n + 2)]
    dp[1] = 1
    dp[2] = 2

    # 점화식 => 현재 x칸을 뛰기 위한 방법의 수 = 이전 경우(x-1)의 수 + 전전 경우(x-2)의 수
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[n]