import sys
sys.stdin = open('input.txt')

n = int(input())    # 숫자 카드의 개수
n_numbers = list(map(int, input().split()))   # 숫자 카드에 적혀있는 정수

m = int(input())    # 숫자 카드인지 아닌지 구해야 할 개수
m_numbers = list(map(int, input().split()))   # 위 숫자 카드에 적혀있는 정수

n_numbers.sort()

def sang_have(x):
    s = 0
    e = n - 1
    while s <= e:
        m = (s + e) // 2
        if n_numbers[m] == x:
            return True
        elif n_numbers[m] > x:
            e = m - 1
        else:
            s = m + 1
    return False

for number in m_numbers:
    if sang_have(number):
        print(1, end=" ")
    else:
        print(0, end=" ")


