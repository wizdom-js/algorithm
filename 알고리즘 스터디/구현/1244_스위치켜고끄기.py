import sys
sys.stdin = open('input.txt')

# 학생이 남자일 경우
def boy(n):
    for i in range(n, switch_n+1, n): # 받은 수의 배수의 스위치 상태 바꾸기
        # switch_on_off(i-1)  # 숫자가 1번부터 시작이니까 -1번째의 스위치 상태 변경
        switch[i-1] ^= 1

# 학생이 여자일 경우
def girl(n):
    switch_on_off(n)    # 기준이 되는 수의 스위치 상태 바꾸기
    tmp = 1
    while 0 <= n-tmp and n+tmp < switch_n:  # 인덱스 범위 설정
        if switch[n-tmp] == switch[n+tmp]:  # 좌우가 대칭이라면 스위치 상태 바꾸기
            # switch_on_off(n-tmp)
            # switch_on_off(n+tmp)
            switch[n-tmp] ^= 1
            switch[n+tmp] ^= 1
        else:
            break   # 대칭 아니면 중단
        tmp += 1    # 다음 좌우 스위치 보기

# 스위치 상태 바꾸기
def switch_on_off(i):
    if switch[i]:
        switch[i] = 0
    else:
        switch[i] = 1


switch_n = int(input()) # 스위치 개수
switch = list(map(int, input().split()))    # 스위치의 상태

student_n = int(input())    # 학생 수
for _ in range(student_n):
    s, n = map(int, input().split())    # 학생 성별 s, 받은 수 n
    if s == 1:
        boy(n)
    else:
        girl(n-1)   # 숫자가 1번부터 시작이니까 빼고 시작

for i in range(0, switch_n, 20):    # 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력
    print(*switch[i:i+20])
