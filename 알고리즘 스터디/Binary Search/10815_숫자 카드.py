import sys
sys.stdin = open('input.txt')

n = int(input())    # 숫자 카드의 개수
n_numbers = list(map(int, input().split()))   # 숫자 카드에 적혀있는 정수

m = int(input())    # 숫자 카드인지 아닌지 구해야 할 개수
m_numbers = list(map(int, input().split()))   # 위 숫자 카드에 적혀있는 정수

n_numbers.sort()    # 이분탐색 하기 위한 정렬

# 상근이가 해당 카드 가지고 있는지 아닌지 판단하기 위한 함수
# => 이분 탐색 함수
def sang_have(x):
    s = 0
    e = n - 1
    while s <= e:
        m = (s + e) // 2    # 중간 값 잡기
        if n_numbers[m] == x:   # 해당 카드가 있다면 True 반환
            return True
        elif n_numbers[m] > x:  # 해당 카드보다 값이 크다면
            e = m - 1
        else:   # 해당 카드보다 값이 작은 경우
            s = m + 1
    return False    # 해당 카드 없는 경우

# 판별애야 할 카드를 반복물 돌면서 판별
for number in m_numbers:
    if sang_have(number):
        print(1, end=" ")
    else:
        print(0, end=" ")


