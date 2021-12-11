import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())    # 숫자 개수 n, 목표 합 s
numbers = list(map(int, input().split()))   # 숫자들

inf = float('inf')
answer = inf   # 길이 무한대로 설정 (가장 짧은 것을 구하는 것이므로)

tmp_sum = numbers[0]     # 임시 숫자들의 합을 저장할 변수
l = r = 0  # 움직일 포인터
while l <= r and r < n:  # l이 r 포인터보다 넘어서거나, r포인터가 n을 넘어설때까지 반복
    if s <= tmp_sum:    # 숫자들의 합이 목표 합보다 크거나 같은 경우
        # 길이 갱신
        tmp_l = r - l + 1
        answer = tmp_l if tmp_l < answer else answer

        # 길이 줄이기 (제일 왼쪽 숫자 (가장 처음에 더한 숫자) 빼주기)
        tmp_sum -= numbers[l]
        l += 1  # 빼줬으니 l포인터 한칸 옮기기
        continue
    else:
        r += 1  # 목표 합에 도달하지 못했을 경우 r포인터 한칸 옮기기

    if r == n: break    # r포인터가 n이랑 같아졌다면 더이상 더할 숫자 없음! 중단. (인덱스 에러 방지)
    tmp_sum += numbers[r]   # r포인터가 가르키는 숫자 더해주기

print(answer if answer != inf else 0)   # 초기 설정한 숫자(무한대)와 같다면 0 출력 (목표 합 만들지 못한경우) 아니면 구한 길이 출력 !


'''
1. 그냥 숫자 123412512341234 사용 (또는 float('1e9')) < float('inf')
2. try except < if r == n: break
3. if 문으로 정답 갱신 < min  (안확실)
'''