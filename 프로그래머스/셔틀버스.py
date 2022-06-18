def solution(n, t, m, timetable):
    timetable.sort()
    print(timetable)
    crew_n = len(timetable)
    timetable_c = [0] * crew_n
    for i in range(crew_n):
        hour, minutes = map(int, timetable[i].split(':'))
        timetable_c[i] = hour*60 + minutes
    
    bus_time = 9*60 - t
    p = 0
    for bus in range(1, n+1):
        bus_time += t
        passenger = 0
        for crew in range(p, crew_n):
            if timetable_c[crew] <= bus_time:
                passenger += 1
                if m == passenger:
                    if bus == n:
                        answer = timetable_c[crew]-1
                        hour, minutes = divmod(answer, 60)
                        return f'{hour:0>2}:{minutes:0>2}'
                    else:
                        p = crew + 1
                        break
            else:
                p = crew
                break
        
    hour, minutes = divmod(bus_time, 60)
    return f'{hour:0>2}:{minutes:0>2}'