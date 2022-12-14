import math

def solution(n, k):
    answer = []
    number_list = [i for i in range(1, n + 1)]

    while n:
        temp = math.factorial(n) // n
        idx = k // temp
        k = k % temp

        if k == 0:
            answer.append(number_list.pop(idx - 1))
        else:
            answer.append(number_list.pop(idx))

        n -= 1

    return answer