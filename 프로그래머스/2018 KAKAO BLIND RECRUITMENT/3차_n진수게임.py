# n 진수로 바꾸기
def change(n, number):
    result = ''
    while number > 0:
        number, r = divmod(number, n)
        if 9 < r:   # 10이상은 알파벳으로 나타내기
            result += chr(55+r)
        else:
            result += str(r)
    return result[::-1] # 뒤집기

def solution(n, t, m, p):
    number = 1  # 2부터 시작하도록
    temp = '01'  # 0부터 시작이므로 0과 1은 담고 시작
    while len(temp) <= m*t: # 사람 수 * 갯수만큼 다 구하고 슬라이스
        number += 1 # 숫자 +1
        temp += change(n, number)   # n진수로 바꾼 number 더해주기

    return ''.join(temp[p-1:m*t:m]) # p부터 시작해서 m(사람 수)만큼 뛰어넘기


print(solution(16, 16, 2, 1))   # "02468ACE11111111"