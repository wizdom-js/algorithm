import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for idx in range(1, t+1):
    print('#{}'.format(idx), end=' ')

    # 다섯개의 단어들 받아오기
    words = []
    for _ in range(5):
        words.append(list(input()))

    # 세로로 읽기
    for i in range(15):
        for j in range(5):
            # try except을 이용해서 인덱스 에러 안나도록 해줌.
            try:
                print(words[j][i], end='')
            except:
                continue

    # 다음 테스트 케이스를 위한 print
    print()

    # words_r = list(map(lambda x: ''.join(list(x)), zip(*words)))