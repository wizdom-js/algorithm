def play_time(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    if sm < em:
        return (em - sm) + (eh - sh)
    else:
        return (sm - em) + (eh - sh - 1)


def is_melody(m, melody, ml):
    s = 0
    for i in range(len(melody)):
        if melody[i] == m[s]:
            s += 1
        else:
            s = 0
        if s == ml:
            if melody[s] != '#':
                return True
    return False


def solution(m, musicinfos):
    ml = len(m)
    melody_can = []
    for info in musicinfos:
        info = info.split(',')
        pt = play_time(info[0], info[1])

        if is_melody(m, info[3] * pt, ml-1):
            melody_can.append((pt, info[2]))

    melody_can.sort(reverse=True)
    return melody_can[0][1]


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))