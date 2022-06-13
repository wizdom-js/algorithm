def solution(n):
    answer = ''
    number = "412"
    while n>0 :

        answer = number[n%3] + answer
        n = n // 3
        
    return answer