import sys
sys.stdin = open('input.txt')


# 회문인지 체크하는 함수
def check_palindrome(l, r):
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


t = int(input())
for _ in range(t):
    string = input()
    answer = 0
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:  # 그 자체로 회문인지
            # 이미 한 글자 제거한 경우
            if answer == 1:
                answer = 2
                break

            # 왼쪽 문자열 삭제 후 회문이 된다면
            if check_palindrome(l+1, r):
                l += 1
                answer = 1
                break

            # 오른쪽 문자열 삭제 후 회문이 된다면
            if check_palindrome(l, r-1):
                r -= 1
                answer = 1

            # 그 자체로 회문도 안되는데 유사회문도 되지 않는 경우 => 일반 문자열
            if answer != 1:
                answer = 2
                break
        
        l += 1
        r -= 1

    print(answer)


