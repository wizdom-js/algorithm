import sys
sys.stdin = open('input.txt')

n = int(input())    # 레벨의 수
levels = [int(input()) for _ in range(n)] # 레벨들 받아오기

answer = 0              # 점수 몇번 내려야 하는지 받는 변수
level = levels[-1]      # 찐 끝판왕 레벨의 점수 가져오기

# 레벨들 중, 위의 끝판왕 레벨 앞부터 비교 (반대로 돌기)
for i in range(n-2, -1, -1):

    # 하위 레벨의 점수가 더 높은 경우
    if level <= levels[i]:
        minus = levels[i] - level + 1   # 점수 얼마나 내려야 하는지
        answer += minus                 # 차이 정답에 더해주기
        level = levels[i] - minus       # 다음 하위 레벨과 비교하기 위해 갱신

    # 이미 상위 레벨의 점수가 높은 경우 현재 레벨만 갱신
    else:
        level = levels[i]

print(answer)


# stage1 = levels.pop()   # 찐 끝판왕 레벨 가져오기
# while levels:
#     stage2 = levels.pop()       # 현재 남아있는 레벨 중 끝판왕 가져오기
#
#     if stage1 <= stage2:
#         minus = stage2 - stage1 + 1 # 점수 얼마나 내려야 하는지
#         answer += minus  # 정답에 더해주기
#         stage1 = stage2 - minus   # 다음 레벨과 비교하기위해 내린 점수로 갱신
#
#     else:
#         stage1 = stage2
#
# print(answer)




'''
4
6
5
4
8
'''