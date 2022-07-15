import sys
sys.stdin = open('input.txt')

n = int(input())    # 전체 용액의 수
solution_values = list(map(int, input().split()))   # 용액의 특성값들

solution_values.sort()      # 정렬하기

gap = 999999999999999
solution1 = 0
solution2 = 0

def binary_search(start_index, standard_sol):
    global gap, solution1, solution2
    s = start_index
    e = n-1

    while s <= e:
        m = (s + e) // 2
        mix = standard_sol + solution_values[m]
        if abs(mix) < gap:
            gap = abs(mix)
            solution1 = standard_sol
            solution2 = solution_values[m]
            if gap == 0:
                break
        if mix < 0:
            s += 2
        else:
            e -= 2

    return

for i in range(n-1):
    binary_search(i, solution_values[i])
    if gap == 0:
        break

print(solution1, solution2)
