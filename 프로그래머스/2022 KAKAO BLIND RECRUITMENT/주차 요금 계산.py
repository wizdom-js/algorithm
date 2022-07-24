base_time, base_fee, unit_time, unit_fee = 0, 0, 0, 0


def cal_time(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(':'))
    out_hour, out_minute = map(int, out_time.split(':'))

    result_time = 0
    if out_minute < in_minute:
        out_hour -= 1
        result_time += 60 + out_minute - in_minute
    else:
        result_time += out_minute - in_minute

    result_time += (out_hour - in_hour) * 60

    return result_time


def cal_fee(parking_time):
    if parking_time <= base_time:
        return base_fee

    parking_time -= base_time

    if parking_time % unit_time:
        return base_fee + (parking_time // unit_time + 1) * unit_fee
    return base_fee + parking_time // unit_time * unit_fee


def solution(fees, records):
    global base_time, base_fee, unit_time, unit_fee

    base_time, base_fee, unit_time, unit_fee = fees
    parking_lot = {}
    parking_sum = {}
    for record in records:
        time, license_number, history = record.split()
        if history == "IN":
            parking_lot[license_number] = time
        else:
            parking_time = cal_time(parking_lot[license_number], time)

            del parking_lot[license_number]

            if license_number in parking_sum:
                parking_sum[license_number] += parking_time
            else:
                parking_sum[license_number] = parking_time

    for license_number, time in parking_lot.items():
        parking_time = cal_time(time, "23:59")

        if license_number in parking_sum:
            parking_sum[license_number] += parking_time
        else:
            parking_sum[license_number] = parking_time

    license_sort = sorted(list(parking_sum.keys()))
    answer = []
    for license_number in license_sort:
        answer.append(cal_fee(parking_sum[license_number]))

    return answer

