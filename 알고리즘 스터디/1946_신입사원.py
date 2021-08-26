import sys
sys.stdin = open('input.txt')

####### 파이파이로 해결 ###########

tc = int(input())

for idx in range(1, tc+1):
    n = int(input())    # 지원자의 수
    grades = [tuple(map(int, input().split())) for _ in range(n)]   # 성적 받아오기

    grades.sort()   # 하나의 기준(서류)으로 내림차순 정렬

    answer = 0  # 선발할 수 있는 신입사원의 최대 인원수

    # 서류 기준으로 정렬했으니 면접 등수만 보면된다.
    temp_g = n+1    # 임시 변수 (최저등급 +1)
    for grade in grades:
        # 현재 면접 등수가 임시 변수에 저장된 등수보다 높다면
        # 서류 또는 면접에서 높은 것이므로 뽑는다. 예) [(1, 5), (2, 3)]
        if grade[1] < temp_g:
            answer += 1
            temp_g = grade[1]  # 갱신
        if grade[1] == 1:  # 최고등급이면 for문 중단
            break
    print(answer)



########### 첨에 풀었던거 ###############3

# tc = int(input())
#
# for idx in range(1, tc+1):
#     n = int(input())    # 지원자의 수
#     grades = [tuple(map(int, input().split())) for _ in range(n)]   # 성적 받아오기
#
#     grades.sort(key=lambda x: x[0])   # 하나의 기준(서류)으로 내림차순 정렬
#
#     answer = 0  # 선발할 수 있는 신입사원의 최대 인원수
#     for i in range(n):
#         # 현재 성적의 다음부터 비교
#         for j in range(i+1, n):
#             # 만약 서류나, 면접 성적이 모두 떨어진다면
#             # 이미 위에서 서류 기준으로 정렬했으니 면접 성적만 비교하면 된다.
#             if grades[j][1] < grades[i][1]:
#                 break
#
#         # 서류 혹은 면접 혹은 둘다 성적이 다른 지원자들에 비해 떨어지지 않는다면
#         else:
#             answer += 1
#
#     print(answer)
