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

n = int(input())    # 단어의 개수

words = [[] for _ in range(8)]  # 단어를 자리 수별로 저장할 리스트
word_dic = {}   # 단어 값을 넣을 딕셔너리

for i in range(n):
    word = input()  # 단어 입력받기
    len_word = len(word)
    for j in range(len_word):
        words[7-j].append(word[len_word-j-1])   # words에 자리 별로 단어 넣어주기
        word_dic[word[j]] = word_dic.get(word[j], 0) + 10 ** (len_word-j-1) # 해당 자리에 맞는 값 넣기

#
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
for num in word_dic.values():   # 알파벳 빼고 값들만 가져와
    numbers.append(num) # 값들 다 넣기

numbers.sort(reverse=True)  # 내림차순 정렬 (큰 값부터 큰 수(9, 8, ..)를 곱해줄거니까)

answer = 0
num = 9 # 최댓값을 만들어야 하므로 9부터 시작
for i in numbers:
    answer += num * i   # 숫자 배정해서 값 더해나가기
    num -= 1

print(answer)