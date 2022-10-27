def solution(topping):
    answer = 0
    chulsoo = [0 for _ in range(10001)]
    brother = [0 for _ in range(10001)]
    chulsoo_n = 1
    brother_n = 0

    chulsoo[topping[0]] = 1
    for t in topping[1:]:
        if not brother[t]:
            brother_n += 1
        brother[t] += 1

    if chulsoo_n == brother_n: answer += 1
    for i in range(1, len(topping)):
        t = topping[i]
        if not chulsoo[t]:
            chulsoo_n += 1
        chulsoo[t] += 1

        brother[t] -= 1
        if not brother[t]:
            brother_n -= 1

        if chulsoo_n == brother_n:
            answer += 1
    return answer