import sys
sys.stdin = open('input.txt')


# min max 함수 안쓴 버전
# 가장 높은 상자, 가장 낮은 상자 찾아주는 함수
def find_min_max(boxes_height):
    # 가장 높거나 가장 낮은 [박스 길이, 해당 인덱스] 초기화
    highest = [boxes_height[0], 0]
    lowest = [boxes_height[0], 0]
    # 박스 전체를 돌면서 비교
    for h in range(len(boxes_height)):
        # 가장 높은 상자 찾기
        if boxes_height[h] > highest[0]:
            highest[0] = boxes_height[h]
            highest[1] = h
        # 가장 낮은 상자 찾기
        if boxes_height[h] < lowest[0]:
            lowest[0] = boxes_height[h]
            lowest[1] = h

    # 가장 높은 상자, 낮은 상자 인덱스 반환
    return highest, lowest


# 10개의 테스트 케이스
for idx in range(1, 11):
    # 덤프 횟수
    n = int(input())
    # 각 상자의 높이 값
    boxes_height = list(map(int, input().split()))

    # 평탄화 작업
    for i in range(n):
        # 가장 높은 상자, 가장 낮은 상자 찾기
        h_box, l_box = find_min_max(boxes_height)

        # 박스 옮기기
        boxes_height[h_box[1]] -= 1
        boxes_height[l_box[1]] += 1

    # final 가장 높은 상자, 가장 낮은 상자 찾기
    f_h_box, f_l_box = find_min_max(boxes_height)


    print('#{} {}'.format(idx, f_h_box[0] - f_l_box[0]))





