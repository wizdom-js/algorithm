import sys
sys.stdin = open('input.txt')


######### 함수 사용 안한 버전 ###########

# 선택정렬 이용해서 numbers 정렬
def selectionSort(n, numbers):
    # 처음 인덱스부터 마지막 -1까지 반복
    # (i보다 오른쪽에 위치한 값과 비교하므로 마지막까지 갈 필요 없다.)
    for i in range(n-1):
        # 가장 작은 수를 가진 인덱스 초기화 (맨 앞이 제일 작다고 일단 가정)
        min_idx = i

        # i의 오른쪽에 위치한 인덱스(i+1)부터 끝 인덱스의 전(n)까지 반복
        # ( 원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 가지니까 )
        for j in range(i+1, n):
            # j번째 위치한 값이 min_idx위치의 값보다 작으면
            if numbers[j] < numbers[min_idx]:
                # 가장 작은 값을 가진 인덱스(min_idx)를 j로 업뎃
                min_idx = j

        # 최종적으로 가장 작은 값을 비교하는 범위의 맨 처음(i)으로 위치를 바꿔준다.
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    # 정렬된 numbers 반환
    return numbers


tc = int(input())

for idx in range(1, tc+1):
    # 정수의 개수 n
    n = int(input())
    # n개의 정수 받아오기
    numbers = list(map(int, input().split()))
    # selectionSort 함수를 사용하여 numbers 정렬
    sorted_numbers = selectionSort(n, numbers)

    # 특별한 정렬을 담을 리스트
    answer = []
    # 가장 큰 수와 가장 작은 수를 동시에 넣을 것이므로 반복문 5번만 돌아도 된다.
    for i in range(5):
        # numbers에 남아있는 수 중,
        # 가장 큰 수, 가장 작은 수 를 answer에 넣어준다.
        answer.extend([sorted_numbers.pop(), sorted_numbers.pop(0)])

    print('#{}'.format(idx), end=' ')
    # print(*objects, sep=' ', end='\n') 이 특징을 이용해 리스트 안의 숫자를 한칸씩 띄워서 출력할 수 있다.
    print(*answer)





# ######### sorted 사용 버전 ###################
#
# tc = int(input())
#
# for idx in range(1, tc+1):
#     n = int(input())
#     numbers = sorted(list(map(int, input().split())))
#     answer = []
#     for i in range(5):
#         answer.extend([numbers.pop(), numbers.pop(0)])
#
#     print('#{}'.format(idx), end=' ')
#     print(*answer)