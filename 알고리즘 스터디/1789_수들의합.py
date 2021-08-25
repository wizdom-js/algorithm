import sys
sys.stdin = open('input.txt')

s = int(input())    # 서로 다른 n개의 자연수의 합

cnt = 0         # n개의 자연수 개수를 담을 변수
n = 1           # s에서 빼줄 숫자 (+1 하면서 빼준다)
# 처음 주어진 s가 0이하가 될때까지 반복
while s > 0:
    s -= n
    cnt += 1
    n += 1

# 만약 s가 음수이면 숫자 하나 제거해줘야 하므로 cnt -1 해준다.
if s < 0:
    cnt -= 1

print(cnt)