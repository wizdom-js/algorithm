# strip, split 사용
def solution(s):
    answer = []

    processed_s = s.lstrip('{').rstrip('}').split('},{')

    set_list = []
    for num_set in processed_s:
        set_list.append(list(map(int, num_set.split(','))))

    set_list.sort(key = len)

    for num_set in set_list:
        for num in num_set:
            if num not in answer:
                answer.append(num)

    return answer


# 구현
def solution(s):
    set_list = []   # 집합을 담을 리스트

    # 집합이 담긴 문자열 s를 숫자가 담긴 집합으로 바꾸기
    idx = 1
    while idx < len(s):
        tmp = []
        number = ""
        while True:
            idx += 1
            if s[idx] == ",":   # 숫자 완성된 경우
                tmp.append(int(number))
                number = ""
            elif s[idx] == "}":  # 집합 완성된 경우
                tmp.append(int(number))
                idx += 1    # 쉼표(,) 뛰어넘기 위해 +1
                break
            else:   # 숫자 이어진 경우
                number += s[idx]

        set_list.append(tmp)    # 완성된 집합 리스트에 담기
        idx += 1

    # 길이가 짧은 것부터 먼저 나오도록 정렬
    set_list.sort(key=lambda x: len(x))

    num_dict = dict()
    answer = []
    for num_set in set_list:
        for num in num_set:
            # 나오지 않은 숫자라면 정답 배열에 담기
            if not num in num_dict:
                num_dict[num] = True
                answer.append(num)

    return answer


# 집합 안의 숫자 count 형식
def solution(s):
    num_dict = dict()
    str_num = ""
    idx = 2
    while idx < len(s):
        if s[idx] == ",":
            pass
        elif s[idx] == "}":
            idx += 2  # 쉼표(,), 열린 괄호({) 뛰어넘기 위해 +2
        else:
            str_num += s[idx]
            idx += 1
            continue

        # 숫자 카운트
        if num_dict.get(str_num):
            num_dict[str_num] += 1
        else:
            num_dict[str_num] = 1
        str_num = ""

        idx += 1

    # 카운트 많이 된 숫자가 먼저 answer에 들어가야하므로 정렬
    tmp = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for num in tmp:
        answer.append(int(num[0]))

    return answer


# strip + split + count => 젤 빠름 
def solution(s):
    num_dict = dict()

    processed_s = s.lstrip('{').rstrip('}').split('},{')

    for num_set in processed_s:
        set_list = list(map(int, num_set.split(',')))
        for num in set_list:
            if num_dict.get(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1

    # 카운트 많이 된 숫자가 먼저 answer에 들어가야하므로 정렬
    tmp = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for num in tmp:
        answer.append(int(num[0]))

    return answer