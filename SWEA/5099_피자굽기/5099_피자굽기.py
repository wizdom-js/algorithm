import sys
sys.stdin = open('sample_input.txt')

# tc = int(input())
#
# for idx in range(1, tc+1):
#     n, m = map(int, input().split())        # 화덕의 크기 n, 피자의 개수 m
#     pizza = list(map(int, input().split())) # 만들 피자 가져오기
#
#     # 인덱스 머리아파서 걍 같이 넣어줌 ex) [[7, 1], [2, 2], [6, 3], [5, 4] [3, 5]]
#     pizza_info = [[pizza[i], i+1] for i in range(m)]
#
#     fire = pizza_info[:n]   # 화덕에 먼저 들어간 피자
#     pizza = pizza_info[n:]  # 화덕에 아직 못들어간 피자
#
#     # 화덕에서 피자가 없어질때까지 반복
#     while fire:
#         p, p_i = fire.pop(0)            # 확인할 피자 pop
#
#         # 줄어든 치즈 양 계산하여 치즈 다 안녹았으면 화덕에 다시 넣기
#         if p//2:
#             fire.append([p//2, p_i])
#         # 다 녹았으면 새로운 피자 가져와서 화덕에 넣기
#         elif p//2 == 0 and pizza:
#             fire.append(pizza.pop(0))
#
#     # 마지막으로 확인한 피자의 번호 출력
#     print('#{} {}'.format(idx, p_i))
#





tc = int(input())

for idx in range(1, tc + 1):
    n, m = map(int, input().split())  # 화덕의 크기 n, 피자의 개수 m
    pizza = list(map(int, input().split()))  # 만들 피자 가져오기

    fire = pizza[:n]  # 화덕에 먼저 들어간 피자
    pizza_n = [i for i in range(1, n+1)]

    pizza = pizza[n:]  # 화덕에 아직 못들어간 피자

    i = -1
    next_pn = n
    while True:
        i += 1
        if fire[i]:
            check = fire[i] // 2

            if check:
                fire[i] = check
            elif not check and pizza:
                fire[i] = pizza.pop(0)
                next_pn += 1
                pizza_n[i] = next_pn

            else:
                pizza_n[i] = 0
                fire[i] = 0
                n -= 1

        if i == n-1:
            i = -1



    # 마지막으로 확인한 피자의 번호 출력
    print('#{} {}'.format(idx, pizza_n[i]))
