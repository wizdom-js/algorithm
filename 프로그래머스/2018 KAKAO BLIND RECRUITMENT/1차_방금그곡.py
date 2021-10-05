# '#' 처리 (소문자로 바꿔준다.)
def change_sharp(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    return melody


# 받아온 시간을 분 단위로 반환해주는 함수
def play_time(start, end):
    sh, sm = map(int, start.split(':'))  # 시작 시, 분
    eh, em = map(int, end.split(':'))  # 종료 시, 분
    return (eh - sh) * 60 + (em - sm)


def solution(m, musicinfos):
    m = change_sharp(m)  # 네오가 기억한 멜로디

    melody_candi = []  # 방송된 곡들 중, 일치하는 곡들의 정보 담을 리스트
    for info in musicinfos:
        info = info.split(',')
        pt = play_time(info[0], info[1])  # 재생시간 분 단위로 계산

        melody = change_sharp(info[3])  # 악보 정보
        q, r = divmod(pt, len(melody))

        if m in melody * q + melody[:r]:  # 재생된 악보 중에 기억한 멜로디 있다면
            melody_candi.append((pt, info[2]))  # 후보에 추가

    if melody_candi:
        melody_candi.sort(key=lambda x: x[0], reverse=True)     # 재생시간이 긴 순으로 정렬 (재생시간만 정렬)
        return melody_candi[0][1]    # 맨 앞의 제목 return
    return "(None)"   # 일치하는 음악 없을 경우


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # WORLD
print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) # FOO
print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))   # HELLO