import sys
sys.stdin = open('sample_input.txt')


for idx in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split()))) # 리스트 a 정렬
    b = list(map(int, input().split())) # 체크할 숫자들이 들어가있는 리스트 b

    answer = 0
    for t_n in b:   # t_n : target number
        s = 0       # 시작 인덱스
        e = n - 1   # 마지막 인덱스
        switch = None   # 이전에 탐방한 구간이 어딘지
        while s <= e:
            mid = (s + e) // 2  # 중간지점
            if a[mid] == t_n:   # t_n을 리스트 a에서 찾은 경우
                answer += 1
                break
            elif a[mid] > t_n and switch != 'l':    # t_n이 중간 지점 숫자보다 작고, 이전 방향 왼쪽 아니었다면
                e = mid - 1     # 다음은 왼쪽 구간 탐방 하도록
                switch = 'l'    # 스위치 왼쪽으로 설정
            elif a[mid] < t_n and switch != 'r':    # t_n이 중간 지점 숫자보다 크고, 이전 방향 오른쪽 아니었다면
                s = mid + 1     # 다음은 오른쪽 구간 탐방하도록
                switch = 'r'    # 스위치 오른쪽으로 설정
            else:       # 방향 겹치는 경우
                break
    print('#{} {}'.format(idx, answer))
