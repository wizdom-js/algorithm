def seperate(file):
    header, number, tail = '', '', ''

    for i in range(len(file)):
        if file[i].isdigit() and len(number) < 5:   # 해당 글자 숫자이고, number 최대길이 안넘은 경우
            number += file[i]
        elif not number:    # number에 값 안들어왔다면 header임
            header += file[i]
        else:   # 그 이외 (number 최대로 채워졌거나, number다음 숫자 아닌 글자 왔을 경우)는 다 tail
            tail = file[i:]
            break
    return header, number, tail


def solution(files):
    files_sep = []
    for file in files:
        header, number, tail = seperate(file)   # 세 파트로 분리
        files_sep.append((header, number, tail))    # 분리한거 튜플로 담아주기

    files_sep.sort(key=lambda x: (x[0].upper(), int(x[1]))) # header를 대문자로 통일해서 먼저 정렬한 후, number를 int로 변환해서 정렬

    return [''.join(f) for f in files_sep]  # 분리한 파일명들 합쳐서 return

print(solution(["aa 123456", "aa 12345"]))

############################################################



def num_idx(file, head_e):
    # number 인덱스 파악
    number_e = 0
    for i in range(head_e + 1, head_e + 6):
        if not file[i].isdigit():
            number_e = i - 1
            return number_e
    return head_e + 5


def solution(files):
    head_e = 0
    for i in range(len(files[0])):
        if files[0][i].isdigit():
            head_e = i - 1
            break

    dic = {}
    for file in files:
        number_e = num_idx(file, head_e)
        temp = (file[:head_e + 1].upper(), int(file[head_e + 1:number_e + 1]))
        dic[temp] = dic.get(temp, []) + [file]

    sort_dic = sorted(dic.keys())
    result = []
    for key in sort_dic:
        result.extend(dic[key])

    return result


