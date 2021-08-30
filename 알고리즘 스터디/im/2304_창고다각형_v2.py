import sys
sys.stdin = open('input.txt')

###### 가장 높은 기둥의 위치를 다 append 하지않고 시작과 끝 위치만 찾는다. ######
##### 더 느림 ###### 왜지.. 더 빠를 줄 알았는데

n = int(input())
pillars = sorted([tuple(map(int, input().split())) for _ in range(n)])

# 가장 높은 기둥 찾기,
highest_h = max(pillars, key=lambda x:x[1])[1]

# 가장 높은 기둥들의 시작, 끝 위치
h_s_l = 0
h_e_l = 0

# 면적 저장할 변수
area = 0

# 맨 앞 기둥 ~ 높은 기둥 구역까지의 면적
temp_h = 0
temp_l = 0
for l, h in pillars:
    # 저장되어있는 높이보다 현재 기둥의 높이가 더 크다면
    if temp_h < h:
        area += temp_h * (l - temp_l)  # 이전에 저장한 기둥 ~ 현재 기둥 전 까지 면적 다 더해
        temp_h = h  # 갱신
        temp_l = l

    # 가장 높은 기둥 만나면 멈추고, 가장 높은 기둥의 첫번째 위치를 저장.
    if h == highest_h:
        h_s_l = l
        break

# 높은 기둥 구역 ~ 맨 뒤 기둥까지의 면적
temp_h = 0
temp_l = 0
for l, h in pillars[::-1]:
    # 저장되어있는 높이보다 현재 기둥의 높이가 더 크다면
    if temp_h < h:
        area += temp_h * (temp_l - l)  # 이전에 저장한 기둥 ~ 현재 기둥 전 까지 면적 다 더해
        temp_h = h  # 갱신
        temp_l = l

    # 가장 높은 기둥의 만나면 멈추고, 가장 높은 기둥의 마지막 위치를 저장 (뒤에서부터 도니까)
    if h == highest_h:
        h_e_l = l
        break

# 현재까지 저장한 면적 + (가장 높은 기둥 위치 ~ 가장 높은 기둥 마지막 위치)까지의 면적
print(area + (h_e_l + 1 - h_s_l)*highest_h)