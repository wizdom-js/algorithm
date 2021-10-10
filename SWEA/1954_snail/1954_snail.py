import sys
sys.stdin = open('input.txt')

# tc의 수
tc = int(input())

# tc 수만큼 반복
for idx in range(1, tc+1):
    # 달팽이의 크기만큼 2차원 배열 만들어주기
    snail = [[0] * idx for _ in range(idx)]

    # 델타 (우하좌상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1 # 달팽이 배열에 넣는 수 초기화
    x, y = 0, -1 # 달팽이 인덱스 초기화
    k = 0 # 방향 설정

    # cnt가 달팽이 크기(idx*idx)보다 작거나 같을 동안만 반복.
    while cnt <= idx*idx:
        # 한칸 이동
        nx, ny = x+dx[k], y+dy[k]

        # 달팽이 크기에서 벗어나지 않고, 해당 위치의 값이 0인 경우
        if 0 <= nx < idx and 0 <= ny < idx and snail[nx][ny] == 0:
            # 해당 자리에 숫자 넣어주기
            snail[nx][ny] = cnt
            # 숫자 + 1
            cnt += 1
            # 현재 인덱스 저장
            x, y = nx, ny

        # 달팽이 크기에서 벗어났거나, 해당 위치에 이미 숫자가 부여되어 있는 경우
        # k값 조정을 통해 방향을 바꾼다.
        else:
            k = (k+1) % 4

    print('#{}'.format(idx))
    # 2차원 배열인 snail 출력
    for i in range(idx):
        print(*snail[i])