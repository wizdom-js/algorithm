import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())    # 나무의 수 n, 나무의 길이 m
tree_h = list(map(int, input().split())  # 나무의 높이

s, e = 1, max(tree_h)   # 시작 높이, 끝 높이
while s <= e:
    mid = (s + e) // 2  # 자를 높이

    temp = 0    # 잘린 나무
    for tree in tree_h:
        if tree >= mid: # mid보다 큰 나무라면 자르기
            temp += tree - mid

    # temp == m: break 하면 안됨. 절단기의 높이를 더 높일 수 있기 때문
    if temp >= m:   # 목표 나무 길이보다 크다면 절단기 높이기
        s = mid + 1
    else:           # 목표 나무 길이보다 작다면 절단기 낮추기
        e = mid - 1

print(e)
