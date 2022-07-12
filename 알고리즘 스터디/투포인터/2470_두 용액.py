import sys
sys.stdin = open('input.txt')

n = int(input())    # 전체 용액의 수
solution_values = list(map(int, input().split()))   # 용액의 특성값들

solution_values.sort()

s = 0
e = n - 1
gap = 999999999999
solution1 = -1
solution2 = -1
while s < e:
    mix = solution_values[s] + solution_values[e]
    if mix == 0:
        solution1 = solution_values[s]
        solution2 = solution_values[e]
        break
    elif abs(mix) < abs(gap):
        solution1 = solution_values[s]
        solution2 = solution_values[e]
        gap = mix

    if mix < 0:
        s += 1
    else:
        e -= 1

print(solution1, solution2)
