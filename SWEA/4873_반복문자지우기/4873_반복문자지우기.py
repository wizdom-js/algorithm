import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for idx in range(1, t+1):
    s = input()
    answer = [] # 스택 이용할 리스트

    for word in s:
        # word == 지금 answer에 추가할까 말까 고민하는 문자
        # answer에 문자가 들어있고, 마지막 문자가 지금 붙이려는 문자와 같다면 중복이므로 pop으로 제거
        if answer and answer[-1] == word:
            answer.pop()

        # answer가 비어있거나, 중복되지 않는 문자라면 추가
        else:
            answer.append(word)

    print('#{} {}'.format(idx, len(answer)))
