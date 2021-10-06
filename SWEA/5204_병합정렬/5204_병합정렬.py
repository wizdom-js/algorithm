import sys
sys.stdin = open('sample_input.txt')


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    global answer

    if right[-1] < left[-1]:
        answer += 1

    result = []
    l = r = 0
    while len(left) > l or len(right) > r:
        if len(left) > l and len(right) > r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        elif len(left) > l:
            result.append(left[l])
            l += 1
        elif len(right) > r:
            result.append(right[r])
            r += 1

    return result

    # result = [0 for _ in range(100001)]
    # l = r = i = 0
    # len_l = len(left)
    # len_r = len(right)
    # while l < len_l or r < len_r:
    #     if l < len_l and r < len_r:
    #         if left[l] <= right[r]:
    #             result[i] = left[l]
    #             i += 1
    #             l += 1
    #         else:
    #             result[i] = right[r]
    #             i += 1
    #             r += 1
    #     elif l < len_l:
    #         result[i] = left[l]
    #         i += 1
    #         l += 1
    #     elif r < len_r:
    #         result[i] = right[r]
    #         i += 1
    #         r += 1
    # return result


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    result = merge_sort(arr)

    print('#{} {} {}'.format(idx, result[n//2], answer))


