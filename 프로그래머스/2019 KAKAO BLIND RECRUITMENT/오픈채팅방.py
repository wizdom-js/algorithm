def solution(record):
    id_nick = {}    # id에 따른 닉네임 저장
    log = []        # 들어왔다 나갔다 기록

    for rec in record:
        rec = rec.split()       # 띄워쓰기 기준으로 분리
        if rec[0] == 'Enter':   # 채팅방에 들어온 경우
            id_nick[rec[1]] = rec[2]    # id를 키로, nickname을 value로 저장
            log.append((rec[1], '님이 들어왔습니다.'))  # 채팅방 출입 기록에 저장
        elif rec[0] == 'Leave': # 채팅방 나간 경우
            log.append((rec[1], '님이 나갔습니다.'))   # 채팅방 출입 기록에 저장
        else:                   # 닉네임 수정한 경우
            id_nick[rec[1]] = rec[2]    # 딕셔너리에서 수정해주기

    return [id_nick[l[0]]+l[1] for l in log]    # id별 저장한 닉네임 불러와서 출입기록과 합쳐주기
