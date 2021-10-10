import sys
sys.stdin = open("sample_input.txt")

# 가위바위보 (1: 가위, 2: 바위, 3: 보)
def game(c1, c2):

    # 가위바위보 버전 1
    # c1이 이겼을 경우 혹은 비겼을 경우(c1이 인덱스가 작으므로 c1 반환)
    if cards[c1] == cards[c2] or cards[c1] % 3 == (cards[c2] + 1) % 3:
        return c1

    # c2가 이겼을 경우
    return c2

    # 가위바위보 버전 2
    if (cards[c1] - cards[c2]) % 3 == 2:
        return c2
    return c1

    # 가위바위보 버전 3
    # if cards[c1] == 1:
    #     return c2 if cards[c2] == 2 else c1
    # elif cards[c1] == 2:
    #     return c2 if cards[c2] == 3 else c1
    # else:
    #     return c2 if cards[c2] == 1 else c1


# 토너먼트(시작 지점, 끝 지점)
# (자기 자신 밖에 없어서) 대결할 사람이 없을 때까지 토너먼트한다.
def tournament(s, e):
    # 대결할 사람 없으면(한 명일 때) 현재 인덱스(s) 반환
    if s == e:
        return s

    m = (s + e) // 2            # 중간 지점 구하기 예) [1, 2, 3] s = 0 e = 2
    g1 = tournament(s, m)       # 중간기준 앞 그룹 토너먼트 하기 [1, 2] s = 0, e = 1 -> [1] s = 0, e = 0 -> 0 / [2] s = 1, e = 1 -> 1
    g2 = tournament(m+1, e)     # 중간기준 뒤 그룹 토너먼트 하기 [3] -> s = e = 2 -> 2 (cards[2] = 3)

    return game(g1, g2) # 가위바위보하기


tc = int(input())

for idx in range(1, tc+1):
    n = int(input())
    cards = list(map(int, input().split()))

    print('#{} {}'.format(idx, tournament(0, n-1)+1))   # 카드는 1부터 시작이므로 +1 해주기
