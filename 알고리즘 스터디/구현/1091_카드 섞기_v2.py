import sys
sys.stdin = open('input.txt')

n = int(input())    # 카드 길이
p = list(map(int, input().split())) # 처음 카드 정보
s = list(map(int, input().split())) # 카드 섞는 방법

first_p = p

answer = 0
while True:
    nxt_p = [0 for _ in range(n)]   # 섞은 카드를 저장할 리스트

    # 원하는 배열대로 되었는지 확인
    for i in range(n):
        if p[i] % 3 != i % 3:
            break
    else:
        break

    # 카드 섞기
    for i in range(n):
        nxt_p[s[i]] = p[i]

    answer += 1

    # 처음 배열이랑 같다면 => 해당 싸이클 반복 => 지민이가 원하는대로 만들 수 없음
    if first_p == nxt_p:
        answer = -1
        break

    p = nxt_p

print(answer)