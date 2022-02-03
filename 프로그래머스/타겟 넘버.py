def solution(numbers, target):
    answer = 0
    numbers_l = len(numbers)

    def dfs(cnt, total):
        nonlocal answer
        if cnt == numbers_l:
            if total == target:
                answer += 1
            return

        dfs(cnt+1, total-numbers[cnt])
        dfs(cnt+1, total+numbers[cnt])

    dfs(0, 0)
    return answer