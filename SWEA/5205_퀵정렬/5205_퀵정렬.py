import sys
sys.stdin = open('sample_input.txt')


def partition(l, r):
    p = arr[l]      # 피봇 설정
    i, j = l, r
    while i <= j:   # 왼쪽과 오른쪽이 만나기 전까지
        while i <= j and arr[i] <= p:   # p보다 큰 값을 만날때까지 오른쪽으로 이동
            i += 1
        while i <= j and arr[j] >= p:   # p보다 작은 값을 만날 때까지 왼쪽으로 이동
            j -= 1
        if i < j:   # i, j 정해졌다면
            arr[i], arr[j] = arr[j], arr[i] # 교환
    arr[l], arr[j] = arr[j], arr[l] # 작은 값 피봇과 교환
    return j    # 파티션이 끝난 후 피봇 위치


def quick_sort(l, r):
    if l < r:
        s = partition(l, r) # 분할
        quick_sort(l, s-1)
        quick_sort(s+1, r)


for idx in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, len(arr)-1)
    print('#{} {}'.format(idx, arr[n//2]))