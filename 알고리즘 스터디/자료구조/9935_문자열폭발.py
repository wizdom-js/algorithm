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


words = input()
explode = list(input())
exp_l = len(explode)

p = 0
new_words = []

for word in words:
    new_words.append(word)
    if new_words[-1] == explode[-1] and new_words[-exp_l:] == explode:
        for _ in range(exp_l):
            new_words.pop()

if new_words:
    print(''.join(new_words))
else:
    print('FRULA')