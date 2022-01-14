import sys
sys.stdin = open('input.txt')

from collections import deque

# words = input()
# explode = input()
#
# p = 0
#
# while p < len(words):
#     if words[p] == explode[0]:
#         tmp_p = p
#         for exp in explode:
#             if words[tmp_p] != exp:
#                 p += 1
#                 break
#             tmp_p += 1
#         else:
#             words = words[:p] + words[tmp_p:]
#             print(words)
#             p -= 1
#             p = 0 if p < 0 else p
#     else:
#         p += 1
#
# if words:
#     print(''.join(words))
# else:
#     print('FRULA')


words = input() # 입력받은 문자열
explode = list(input()) # 폭발 문자열
exp_l = len(explode)

new_words = []

for word in words:
    new_words.append(word)  # 기존 문자열의 단어 하나를 새 리스트에 추가
    # new_words의 마지막 글자가 폭발 문자열의 마지막 글자와 같고,
    # 그래서 끝의 글자들이 폭발 문자열과 같다면
    if new_words[-1] == explode[-1] and new_words[-exp_l:] == explode:
        for _ in range(exp_l):  # 폭발 시키기 (문자 제거)
            new_words.pop()

if new_words:  # 문자 남아있다면 문자열로 변환하여 print
    print(''.join(new_words))
else:
    print('FRULA')  # 남아있는 문자 없는 경우