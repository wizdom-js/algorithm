import sys
sys.stdin = open('input.txt')

n = int(input())    # 카드 길이
p = list(map(int, input().split())) # 처음 카드 정보
s = list(map(int, input().split())) # 카드 섞는 방법

correct_p = [0, 1, 2] * (n // 3)    # 지민이가 원하는 카드 배열
card_set = set()    # 카드 배열 담을 set
set_cnt = 0

answer = 0
while True:
    nxt_p = [0 for _ in range(n)]   # 섞은 카드를 저장할 리스트

    if p == correct_p:  # 원하는 배열대로 되었다면
        break

    # 카드 섞기
    for i in range(n):
        nxt_p[s[i]] = p[i]

    answer += 1

    card_set.add(tuple(nxt_p))  # 현재 카드 배열 추가하기
    if len(card_set) == set_cnt:    # 카드 배열이 중복이었다면 => 무한 루프 => 원하는 배열 만들 수 없음
        answer = -1
        break
    set_cnt += 1    # 배열 수 추가

    p = nxt_p

print(answer)

