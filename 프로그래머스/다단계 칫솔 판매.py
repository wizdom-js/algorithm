def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    name_idx = dict()
    for i, e in enumerate(enroll):
        name_idx[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = name_idx[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money