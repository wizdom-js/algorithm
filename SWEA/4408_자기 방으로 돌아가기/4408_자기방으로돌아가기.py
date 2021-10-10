import sys
sys.stdin = open('sample_input.txt')

# 방으로 들어가
def goback(s_room, e_room):

    # 출발 방에서 도착 방까지 해당 루트에 +1 해주기
    for i in range(s_room, e_room+1):
        room[i] += 1


t = int(input())

for idx in range(1, t+1):
    n = int(input())

    # 복도 만들어주기
    # 방이 두 줄로 되어있으므로 복도의 길이는 200
    room = [0 for _ in range(201)]

    for _ in range(n):
        # 출발 방, 끝 방 받아오기
        # 인덱스 편하게 사용하기 위해 방 +1 해주었다. (예. 1번방은 //2 해주면 0이 되므로 )
        # 방이 두 줄이므로 //2 해준다.
        s_room, e_room = map(lambda x: (int(x)+1)//2, input().split())

        # 출발 방보다 도착방이 더 뒤에 있는 경우
        if s_room > e_room:
            goback(e_room, s_room)
        # 출발 방이 도착 방보다 앞에 있는 경우
        else:
            goback(s_room, e_room)


        # # 조건문 안쓰고 하려면 !! 이 경우는 함수 안 만들어두댐
        # s_room, e_room = sorted(map(lambda x: (int(x) + 1) // 2, input().split()))
        # goback(s_room, e_room)

    # 겹치는 부분의 최대인 곳을 구하면 최소 시간이 된다.
    print('#{} {}'.format(idx, max(room)))



# 입력받은 순서대로 들어가는건줄 알고
# 범위를 사용했었는데 (앞에 사람 경로에 다음사람 출발이나 도착 방이 들어간다면 time+1 하는걸로)
# 그게 아니고 다 받아와서 내가 최소 시간을 구하는 것