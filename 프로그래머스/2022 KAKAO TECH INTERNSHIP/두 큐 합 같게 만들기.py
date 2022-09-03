from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q1)
    for i in range(len(queue1) * 3):
        if sum_q1 == sum_q2:
            return i
        elif sum_q1 > sum_q2:
            num = q1.popleft()
            q2.append(num)
            sum_q1 -= num
            sum_q2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum_q1 += num
            sum_q2 -= num

    return -1