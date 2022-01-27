def solution(n, times): 
    s = 0
    e = max(times) * n
    answer = 0
    while s <= e:
        m = (s + e) // 2
        tmp = 0
        for time in times:
            tmp += m // time
            if n <= tmp:
                e = m - 1
                answer = m
                break
        else:
            s = m + 1

    return answer