def solution(n, t, m, timetable):
    timetable.sort()    # 타임테이블 정렬

    crew_n = len(timetable) # 타임테이블 개수
    for i in range(crew_n): # 시간표를 분으로 전환
        hour, minutes = map(int, timetable[i].split(':'))
        timetable[i] = hour * 60 + minutes

    bus_time = 9 * 60 - t   # 버스 처음 시간
    p = 0                   # 크루 포인터
    for bus in range(1, n + 1):
        bus_time += t   # 버스 시간
        passenger = 0   # 탑승 크루 수
        for crew in range(p, crew_n):   # 안탄 크루들 태우기
            if timetable[crew] <= bus_time: # 현재 버스 시간에 오거나, 먼저 와있는 크루라면
                passenger += 1          # 태우기
                if m == passenger:      # 만석이라면
                    if bus == n:        # 근데 마지막 버스라면
                        answer = timetable[crew] - 1    # 맨 마지막 탑승 크루보다 1분 일찍와
                        hour, minutes = divmod(answer, 60)
                        return f'{hour:0>2}:{minutes:0>2}'  # 문자열로 바꾸고 return
                    else:
                        p = crew + 1    # 만석인데 마지막 버스 아니면
                        break           # 다음 크루부터 태우도록 포인터 옮기기
            else:           # 크루가 버스 시간보다 더 늦게왔다면
                p = crew    # 지금 크루부터 다음 버스에 태우도록 포인터 옮기기
                break       # 다음 버스 오도록 break

    hour, minutes = divmod(bus_time, 60)
    return f'{hour:0>2}:{minutes:0>2}'  # break 안걸렸으면 마지막 버스 타 그냥 