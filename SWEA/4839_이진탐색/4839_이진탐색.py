import sys
sys.stdin = open('input.txt')

# 페이지 몇 번만에 찾았는지 반환하는 함수
def pageSearch(total_p, goal_p):
    start = 1           # 시작페이지
    end = total_p       # 마지막 페이지
    count = 0           # 몇트만에 찾았는지

    # 시작 쪽수가 마지막 쪽수보다 크지 않는 동안 반복
    while start <= end:
        count += 1                      # 시도 +1
        middle = (start + end) // 2     # 중간 페이지 계산
        # print('goal_p', goal_p, 'start', start, 'middle', middle, 'end', end, 'count', count)

        # 중간 페이지가 목표한 페이지와 같다면 count 반환
        if middle == goal_p:
            return count
        # 중간 페이지보다 목표 페이지가 작다면 마지막 페이지를 중간 페이지로 대체
        elif goal_p < middle:
            end = middle
        # 중간페이지가 목표 페이지보다 크다면 처음 페이지를 중간 페이지로 대체
        else:
            start = middle

    return False # 못찼았을 경우 False 반환 (현재 케이스에서는 없음)



tc = int(input())

for idx in range(1, tc+1):
    # 총 페이지 수, a가 찾는 쪽 번호, b가 찾는 쪽 번호
    total_p, a_p, b_p = map(int, input().split())

    # a, b가 위의 pageSearch 함수를 이용해서 각자 찾는 쪽 번호를 몇 번만에 찾았는지 각 변수에 저장
    search_a = pageSearch(total_p, a_p)
    search_b = pageSearch(total_p, b_p)

    winner = None
    # 비겼을 경우
    if search_a == search_b:
        winner = 0
    # a가 이겼을 경우
    elif search_a < search_b:
        winner = 'A'
    # b가 이겼을 경우
    else:
        winner = 'B'


    print('#{} {}'.format(idx, winner))