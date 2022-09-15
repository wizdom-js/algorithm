def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    name_idx = dict()

    for i in range(len(enroll)):
        name_idx[enroll[i]] = i

    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = name_idx[s]
            answer[idx] += m - m // 10
            m //= 10
            s = referral[idx]

    return answer