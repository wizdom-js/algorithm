def solution(s):
    answer = []

    processed_s = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in processed_s:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


def solution(s):
    set_list = []
    idx = 1
    while idx < len(s):
        tmp = []
        number = ""
        while True:
            idx += 1
            if s[idx] == ",":
                tmp.append(int(number))
                number = ""
            elif s[idx] == "}":
                tmp.append(int(number))
                idx += 1
                break
            else:
                number += s[idx]

        set_list.append(tmp)
        idx += 1

    set_list.sort(key=lambda x: len(x))

    num_dict = dict()
    answer = set()
    for num_set in set_list:
        for num in num_set:
            if not num in num_dict:
                num_dict[num] = True
                answer.append(num)

    return answer