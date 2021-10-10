import sys
sys.stdin = open('input.txt')

# min max index 함수 쓴 버전
# 10개의 테스트 케이스
for idx in range(1, 11):
    # 덤프 횟수
    n = int(input())
    # 각 상자의 높이 값
    boxes_height = list(map(int, input().split()))

    # 평탄화 작업
    for i in range(n):
        # 가장 높은 상자, 가장 낮은 상자 찾기
        h_idx = boxes_height.index(max(boxes_height))
        l_idx = boxes_height.index(min(boxes_height))

        # 박스 옮기기
        boxes_height[h_idx] -= 1
        boxes_height[l_idx] += 1

    # final 가장 높은 상자, 가장 낮은 상자 찾기
    highest = max(boxes_height)
    lowest = min(boxes_height)


    print('#{} {}'.format(idx, highest-lowest))





