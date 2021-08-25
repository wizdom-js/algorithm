import sys
sys.stdin = open('input.txt')

n = int(input())

dasom = int(input())    # 다솜이 현재 득표 수
vote = sorted([int(input()) for _ in range(n-1)])   # 다른 후보 득표 수

cnt = 0     # 매수할 사람의 수
# 다솜이 득표수가 다른 후보 득표 수보다 작거나 같을 경우에만 매수 시도.
# 또한 다솜이 혼자 후보일 경우가 있으므로(n=1), 다른 후보가 있을 경우에만(vote에 값이 있을 경우) 매수 시도한다.
while dasom <= vote[-1] and vote:
    dasom += 1
    vote[-1] -= 1
    vote.sort()     # 정렬
    cnt += 1

print(cnt)


