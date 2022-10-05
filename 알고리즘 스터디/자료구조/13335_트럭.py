import sys
sys.stdin = open('input.txt')

from collections import deque

n, bridge_l, bridge_w = map(int, input().split())
trucks = list(map(int, input().split()))

now_weight = 0
now_length = 0
bridge = deque()
time = 0
for truck in trucks:
    while True:
        if now_length + 1 <= bridge_l:   # 다리에 트럭 올라갈 자리 있다면
            if now_weight + truck <= bridge_w:  # 무게도 충분하다면
                now_weight += truck
                now_length += 1
                bridge.append(truck)
                time += 1
                break
            else:   # 무게 초과되는 경우 => 다른 트럭 빼내야함
                bridge.append(0)
                now_length += 1
                time += 1
        else:   # 다리 full이라면 => 맨 앞 트럭 꺼내도 됨
            t = bridge.popleft()
            now_weight -= t
            now_length -= 1

# 마지막으로 올라간 트럭이 다리를 지나야 하므로 "현재까지 시간 + 다리 길이"를 프린트해준다.
print(time + bridge_l)

