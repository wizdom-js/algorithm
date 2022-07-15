import sys
sys.stdin = open('input.txt')

n = int(input())    # 전체 용액의 수
solution_values = list(map(int, input().split()))   # 용액의 특성값들

solution_values.sort()      # 정렬하기

s = 0
e = n - 1

gap = 999999999999  # 저장할 용액의 특성 값
solution1 = 0  # 갱신될 용액의 값 1
solution2 = 0  # 갱신될 용액의 값 2

# s <= e 로 할 경우 같은 곳에서 멈추는 경우가 있음
while s < e:
    mix = solution_values[s] + solution_values[e]   # 용액 혼합하기
    if abs(mix) < abs(gap):   # 혼합한 절댓값이 저장되어있는 특성 값보다 절댓값이 작다면 갱신
        solution1 = solution_values[s]
        solution2 = solution_values[e]
        if mix == 0:
            break
        gap = mix

    if mix < 0: # 용액이 0보다 작다면 좀 더 큰값으로 바ㅂ꾸기
        s += 1
    else:   # 그렇지 않다면 용액 작은 값으로 바꾸기
        e -= 1

print(solution1, solution2)

