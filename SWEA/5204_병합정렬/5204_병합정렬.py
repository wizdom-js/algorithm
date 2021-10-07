import sys
sys.stdin = open('sample_input.txt')

# 분할 단계
def merge_sort(arr):
    if len(arr) <= 1:   # 길이가 1이 될때까지 분할하는거야
        return arr

    middle = len(arr) // 2  # 중심을 기준으로 두개의 구간으로 나누기
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)   # 병합 고고


# 병합 단계 v2 - append
def merge(left, right):
    global answer

    if right[-1] < left[-1]:    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 count
        answer += 1

    # pop(0) 대신 인덱스로 접근, append 사용
    result = []
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:       # left, right에 추가할 원소 남아있을 때까지 반복
        if l < len_l and r < len_r:     # left, right에 둘다 원소가 남아 있다면
            if left[l] <= right[r]:     # 왼쪽이 작은 경우
                result.append(left[l])  # 왼쪽 값 추가
                l += 1  # left의 다음 원소 지목
            else:
                result.append(right[r]) # 오른쪽이 작은 경우, 오른쪽 값 추가
                r += 1  # right의 다음 원소 지목

        elif l < len_l: # left에만 원소 남아있는 경우
            result.append(left[l])
            l += 1
        elif r < len_r: # right에만 원소 남아있는 경우
            result.append(right[r])
            r += 1

    return result


# 병합 단계 v2 - 인덱스로만
def merge2(left, right):
    global answer

    if right[-1] < left[-1]:    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 count
        answer += 1

    # 인덱스로만 접근
    len_l = len(left)
    len_r = len(right)
    result = [0 for _ in range(len_l+len_r)]
    l = r = i = 0
    while l < len_l or r < len_r:       # left, right에 추가할 원소 남아있을 때까지 반복
        if l < len_l and r < len_r:     # left, right에 둘다 원소가 남아 있다면
            if left[l] <= right[r]:     # 왼쪽이 작은 경우
                result[i] = left[l]     # 왼쪽 값 추가
                i += 1      # result 다음 자리로 이동
                l += 1      # left의 다음 원소 지목
            else:
                result[i] = right[r]    # 오른쪽이 작은 경우, 오른쪽 값 추가
                i += 1      # result 다음 자리로 이동
                r += 1      # right의 다음 원소 지목

        elif l < len_l:     # left에만 원소 남아있는 경우
            result[i] = left[l]
            i += 1
            l += 1

        elif r < len_r:     # right에만 원소 남아있는 경우
            result[i] = right[r]
            i += 1
            r += 1

    return result


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    result = merge_sort(arr)

    print('#{} {} {}'.format(idx, result[n//2], answer))


