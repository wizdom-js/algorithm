import sys
sys.stdin = open('input.txt')

n = int(input())
pillars = sorted([tuple(map(int, input().split())) for _ in range(n)])

# 가장 높은 기둥 찾기,
highest_h = max(pillars, key=lambda x:x[1])[1]
# 가장 높은 기둥들의 위치 저장
highest_l = []
for l, h in pillars:
    if highest_h == h:
        highest_l.append(l)


# 높은 기둥 구역 면적 처리 먼저 해줌
# 가장 높은 기둥의 첫번째 위치 ~ 가장 높은 기둥의 마지막 위치 까지의 면적을 먼저 계산하여 넣어준다.
area = highest_h * (highest_l[-1]+1 - highest_l[0])

# 맨 앞 기둥 ~ 높은 기둥 구역까지의 면적
temp_h = 0
temp_l = 0
for l, h in pillars:
    # 저장되어있는 높이보다 현재 기둥의 높이가 더 크다면
    if temp_h < h :
        area += temp_h * (l-temp_l)     # 이전에 저장한 기둥 ~ 현재 기둥 전 까지 면적 다 더해
        temp_h = h      # 갱신
        temp_l = l

    # 가장 높은 기둥의 첫번째 위치 만나면 멈추기
    if l == highest_l[0]:
        break


# 높은 기둥 구역 ~ 맨 뒤 기둥까지의 면적
temp_h = 0
temp_l = 0
for l, h in pillars[::-1]:
    # 저장되어있는 높이보다 현재 기둥의 높이가 더 크다면
    if temp_h < h:
        area += temp_h * (temp_l - l)   # 이전에 저장한 기둥 ~ 현재 기둥 전 까지 면적 다 더해
        temp_h = h      # 갱신
        temp_l = l

    # 가장 높은 기둥의 마지막 위치 만나면 멈추기
    if l == highest_l[-1]:
        break

print(area)

'''
5
1 11
2 11
3 11
4 11
5 11
# 55
'''


