from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    # 최대 이동 횟수 => q1 * 3 - 2
    # 큰 수가 몰려 있는 경우를 생각하면 된다. 
    # [1,1,1,8,10,9] [1,1,1,1,1,1] => 15회
    for i in range(len(q1) * 3 - 2):
        if sum_q1 == sum_q2:    # 원소 합이 같은 경우
            return i
        elif sum_q1 > sum_q2:   # q1이 큰 경우
            number = q1.popleft()
            q2.append(number)
            sum_q1 -= number
            sum_q2 += number
        else:                   # q2합이 큰 경우
            number = q2.popleft()
            q1.append(number)
            sum_q1 += number
            sum_q2 -= number

    return -1