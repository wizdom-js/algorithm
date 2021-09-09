import sys
sys.stdin = open('input.txt')

# def recur(idx, cnt, total):
#     global diff, answer
#
#     # 세개 골랐니
#     if cnt == 3:
#         # 합이 m보다 작거나 같고 원래 diff 변수에 있던 m과의 차이보다 작나요?
#         if total <= m and m-total < diff:
#             diff = m-total   # 그럼 차이를 갱신해주세요
#             answer = total      # 정답도요
#         return  # 잘가
#
#     # 이미 m보다  크거나, idx 초과면 돌아가
#     if m < total or idx == n:
#         return
#
#     recur(idx+1, cnt+1, total+cards[idx])   # 지금 인덱스 카드 숫자 고를고야
#     recur(idx+1, cnt, total)    # 지금 인덱스 카드 숫자 안고를고야

#######################
# 영남 T 코드 참고

def recur(idx, cnt, total):
    global answer

    # 세개 골랐니
    if cnt == 3:
        # 어차피 m못넘으니 m보다 작거나 같은 수 중에 젤 큰거 가져오면 된다.
        if total <= m and answer < total:
            answer = total  # 정답 갱신
        return

    # 이미 m보다  크거나, idx 초과면 돌아가
    if m < total or idx == n:
        return

    recur(idx+1, cnt+1, total+cards[idx])   # 지금 인덱스 카드 숫자 고를고야
    recur(idx+1, cnt, total)    # 지금 인덱스 카드 숫자 안고를고야


# 카드의 개수 n, 플레이어가 고른 카드의 합 m
n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

recur(0, 0, 0)

print(answer)