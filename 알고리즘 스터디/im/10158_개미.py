import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())    # 격자 공간
sx, sy = map(int, input().split())  # 개미의 시작 좌표값
t = int(input())    # 개미가 움직일 시간

# 개미의 움직임
# 개미는 올라갔다 -> 내려갔다를 반복한다.
# 그리고 좌표의 맨 아래지점, 맨 위 지점은 왜 1번만 있는지는 조금만 생각해보면 간단하다 해당 지점에서 한번 더 머무르는 것이 아니기 때문.
# 또한 올라가는게 먼저이니, 상승 움직임? 부터 넣어준다.
move_x = [i for i in range(w)] + [i for i in range(w, 0, -1)]
move_y = [i for i in range(h)] + [i for i in range(h, 0, -1)]

# 개미의 움직임은 반복이므로 시작지점 + 개미가 움직일 시간을 move_x의 길이(2*w)로 나눈 나머지의 길이만 이동하면 된다.
f_x = move_x[(sx + t) % (2 * w)]
f_y = move_y[(sy + t) % (2 * h)]

print('{} {}'.format(f_x, f_y))



