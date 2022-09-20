import sys
sys.stdin = open('input.txt')

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
        if string[l] != string[r]:
            if answer == 1:
                answer = 2
                break

            if string[l+1] == string[r] and check_palindrome(l+1, r):
                l += 1
                answer = 1
                break

            if string[l] == string[r-1] or check_palindrome(l, r-1):
                r -= 1
                answer = 1

            if answer != 1:
                answer = 2
                break

        l += 1
        r -= 1

    print(answer)


