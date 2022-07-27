# 기본 시간, 기본 요금, 단위 시간, 단위 요금 전역 변수로 빼기
base_time, base_fee, unit_time, unit_fee = 0, 0, 0, 0


# 시간 계산하는 함수 => 시 단위를 분으로 통합
def cal_time(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(':'))   # 들어온 시간 시, 분으로 나누기
    out_hour, out_minute = map(int, out_time.split(':'))    # 나간 시간

    result_time = 0 # 분으로 통합한 시간
    if out_minute < in_minute:  # 나간 분이 더 작을 경우
        out_hour -= 1
        result_time += 60 + out_minute - in_minute
    else:   # 그렇지 않을 경우
        result_time += out_minute - in_minute

    result_time += (out_hour - in_hour) * 60    # 남은 시 -> 분으로 계산하기

    return result_time


# 요금 계산하기
def cal_fee(parking_time):
    if parking_time <= base_time:   # 기본 시간내로 주차했다면
        return base_fee # 기본 요금만 내기

    parking_time -= base_time   # 기본 시간 빼주기 (기본 시간 이상 주차)

    if parking_time % unit_time:    # 단위 시간으로 시간이 딱 떨어지지 않는 경우
        return base_fee + (parking_time // unit_time + 1) * unit_fee    # 올림해서 계산
    return base_fee + parking_time // unit_time * unit_fee


def solution(fees, records):
    global base_time, base_fee, unit_time, unit_fee

    base_time, base_fee, unit_time, unit_fee = fees
    parking_lot = {}    # 들어온 자동차 기록하는 딕셔너리
    parking_sum = {}    # 나간 자동차의 총 주차시간 기록하는 딕셔너리
    for record in records:
        time, license_number, history = record.split()  # 시간, 차번호, 나간건지 들어온건지의 기록
        if history == "IN": # 입차인 경우
            parking_lot[license_number] = time  # 번호로 입차시간 기록
        else:   # 출차의 경우
            parking_time = cal_time(parking_lot[license_number], time)  # 번호로 주차 시간 계산해서 기록하기

            del parking_lot[license_number] # 입차 딕셔너리에서 지우기

            if license_number in parking_sum:   # 2번째 주차인 경우
                parking_sum[license_number] += parking_time # 원래 있는 곳에다가 더해주기
            else:
                parking_sum[license_number] = parking_time

    for license_number, time in parking_lot.items():    # 출차내역 없는 차량 처리
        parking_time = cal_time(time, "23:59")  # 출차 시간 23:59분으로 시간 계산

        if license_number in parking_sum:   # 주차 시간 기록
            parking_sum[license_number] += parking_time
        else:
            parking_sum[license_number] = parking_time

    license_sort = sorted(list(parking_sum.keys())) # 차 번호순대로 정렬
    answer = []
    for license_number in license_sort: # 차 번호순대로 뽑아서 요금 계산 후 정답 리스트에 넣기 
        answer.append(cal_fee(parking_sum[license_number]))

    return answer

