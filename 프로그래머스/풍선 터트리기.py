def solution(a):
    answer = 2

    if 0 <= len(a) <= 2:
        return len(a)

    l, r = a[0], a[-1]

    for i in range(1, len(a) - 1):
        if l > a[i]:
            answer += 1
            l = a[i]
        if r > a[-1 - i]:
            answer += 1
            r = a[-1 - i]

    answer = answer if l != r else answer - 1
    return answer