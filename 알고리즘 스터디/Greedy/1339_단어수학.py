import sys
sys.stdin = open('input.txt')

# n = int(input())
#
# words = [[0 for _ in range(8)] for _ in range(n)]
# word_dic = {}
#
# for i in range(n):
#     word = input()
#     len_word = len(word)
#     for j in range(len_word):
#         words[i][7-j] = word[len_word-j-1]
#         word_dic[word[j]] = word_dic.get(word[j], 0) + 1
#
# print(words)
# print(word_dic)

n = int(input())

words = [[] for _ in range(8)]
word_dic = {}

for i in range(n):
    word = input()
    len_word = len(word)
    for j in range(len_word):
        words[7-j].append(word[len_word-j-1])
        word_dic[word[j]] = word_dic.get(word[j], 0) + 10 ** (len_word-j-1)
print(words)
# num = 9
# word_num = {}
# answer = 0
# for i in range(8):
#     if words[i]:
#         order = [(word_dic[w], w) for w in words[i]]
#         order.sort(key=lambda x: x[0], reverse=True)
#         for o, w in order:
#             if w not in word_num:
#                 word_num[w] = num
#                 answer += num * (10 ** (7-i))
#                 num -= 1
#             else:
#                 answer += word_num[w] * (10 ** (7 - i))
# print(answer)

numbers = []
for num in word_dic.values():
    numbers.append(num)

numbers.sort(reverse=True)

answer = 0
num = 9
for i in numbers:
    answer += num * i
    num -= 1
print(answer)
print(word_dic)