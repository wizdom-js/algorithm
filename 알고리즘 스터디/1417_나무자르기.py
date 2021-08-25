import sys
sys.stdin = open('input.txt')

n = int(input())    # 나무의 개수
trees_f = list(map(int, input().split()))   # 첫날의 나무 길이
trees_g = list(map(int, input().split()))   # 나무들이 자라는 길이

# 짝 만들기 (자라는 길이, 첫날의 길이) 순서
# 뒤집어준 이유는 정렬에서 람다 쓰기 싫어서
trees_info = []
for f, g in zip(trees_f, trees_g):
    trees_info.append((g, f))

# 자라는 길이가 짧은 순으로 정렬
trees_info.sort()

answer = 0
# 나무 베기
for day in range(n):
    answer += trees_info[day][0] * day + trees_info[day][1]

print(answer)