def solution(stones, k):
    s = 0
    e = max(stones)
    answer = 0
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        for stone in stones:
            if stone <= m:
                cnt += 1
            else:
                cnt = 0
            if k <= cnt:
                break

        if cnt < k:
            s = m + 1
        else:
            answer = m
            e = m - 1

    return answer