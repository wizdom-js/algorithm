# 딕셔너리 만들기
def dictionary():
    dic = {}
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    return dic

def solution(msg):
    dic = dictionary()
    msg = msg.upper()
    answer = []
    idx = 27
    k = 0
    for i in range(len(msg)-1):
        if i < k:
            continue
        for j in range(i+1, len(msg)+1):
            temp = dic.get(msg[i:j+1], 0)
            if not temp:
                dic[msg[i:j+1]] = idx
                idx += 1
                answer.append(dic[msg[i:j]])
                k = j
                break
            if j == len(msg):
                answer.append(temp)
                break

    return answer

#######################################################

# 딕셔너리 만들기
def dictionary():
    dic = {}
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    return dic


def solution1(msg):
    dic = dictionary()
    msg = list(msg.upper())[::-1]
    answer = []     # 색인 번호 배열
    idx = 26

    w = msg.pop()   # 글자 하나 뽑기
    last = True

    while msg:
        c = msg.pop()   # 글자 하나 뽑기
        if w + c in dic:    # 더한 글자가 사전에 있다면
            while True:
                w = w + c   # 합쳐줘
                if msg:                # 뽑을거 있다면 새 글자 하나 더 뽑기
                    c = msg.pop()
                else:           # 마지막 글자까지 더한게 모든 글자 다 처리한 경우
                    last = False       # 스위치 꺼
                    break

                if w + c not in dic:    # 하나 더 뽑은게 사전에 없다면 멈춰
                    break

        idx += 1        # 사전 인덱스 하나 추가
        dic[w + c] = idx        # 새 글자 딕셔너리에 추가
        answer.append(dic[w])   # 있는 글자는 색인 번호 배열에 추가
        w = c   # c부터 시작

    if last:    # 한글자 남은 경우 (c에 글자 남아있었던 경우)
        answer.append(dic[w])   # 한글자 처리

    print(dic)
    return answer


print(solution1('ABABABABABABABAB'))
# print(solution1('KAKAO'))