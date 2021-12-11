import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())    # 숫자 개수 n, 목표 합 s
numbers = list(map(int, input().split()))   # 숫자들

tmp_sum = 0     # 임시 숫자들의 합을 저장할 변수
answer = 128349127598217598718296792   # 길이 크게크게 설정 (가장 짧은 것을 구하는 것이므로)
p = 0   # 움직일 포인터 (왼쪽)
for i in range(n):    # i == 오른쪽 포인터
    tmp_sum += numbers[i]   # i번째 숫자 더하기

    if s <= tmp_sum:    # 숫자들의 합이 목표 합보다 크거나 같다면
        for j in range(p, i+1):     # 합한 숫자들에서 맨 왼쪽 숫자 빼보면서 길이 줄이기
            tmp_sum -= numbers[j]   # 가장 왼쪽 숫자 (가장 먼저 더한 숫자 빼기)
            if tmp_sum < s:         # 목표 합(s)보다 작아졌다면 (목표 합보다 작아질 때까지 빼는거임)
                answer = min(i - j + 1, answer) # 길이 짧은걸로 갱신
                p = j + 1   # (왼쪽) 포인터는 방금 뺀 숫자의 다음부터 시작
                # (방금 뺀 숫자를 포함하면 목표 합이 된다. 방금 뺀 숫자를 포함하지 않으면 목표 합보다 작아지므로 거기서부터 다시 오른쪽 포인터 옮기면서 더해간다)
                break   # 이미 목표 합보다 숫자가 작아졌으므로 중단

if answer == 128349127598217598718296792:   # 목표 합을 구할 수 없는 경우
    answer = 0

print(answer)

