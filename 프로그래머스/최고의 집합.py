def solution(n, s):
    answer = []

    if s // n < 1:
        answer = [-1]
    else:
        s_n = s // n

        for i in range(n):
            answer.append(s_n)
        s_p_n = s % n

        idx = len(answer) - 1

        for i in range(s_p_n):
            answer[idx - i] = answer[idx - i] + 1

    return answer