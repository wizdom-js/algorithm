import sys
sys.stdin = open('input.txt')

n = int(input())        # 사람 수
seats = list(input())   # 좌석 배치도

holder = 1      # 홀더 개수 (맨 왼쪽에 하나 놓고 시작 좌석마다 오른쪽에 컵 홀더 놓는다고 가정)
while seats:
    seat = seats.pop()  # 좌석 하나 받아오기

    # 좌석이 S 인 경우
    if seat == 'S':
        holder += 1

    # 좌석이 L 인 경우
    else:
        holder += 1
        seats.pop() # 커플석이므로 다음 L 제거

# 홀더 이용하고 싶어하는 사람이 더 적으면 사람 수 반환
# 홀더 이용하고 싶어하는 사람이 더 많으면 배치 가능한 홀더 개수 반환
print(n if n < holder else holder)
