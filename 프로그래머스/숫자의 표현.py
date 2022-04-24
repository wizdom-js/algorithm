def solution(n):
    answer = 0
    for i in range(1, n+1, 2):
        if not n % i:
            answer += 1
    return answer


def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        cnt = 0
        for j in range(i, n+1):
            cnt += j
            if cnt == n:
                answer += 1
                break
            elif cnt > n: 
                break
            else:
                continue
    return answer