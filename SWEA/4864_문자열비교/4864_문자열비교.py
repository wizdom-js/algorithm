import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

for idx in range(1, tc+1):
    str1 = input()
    str2 = input()

    str1_l = len(str1)

    answer = 0

    ######## 간편 버전 ###########
    # if str1 in str2:
    #     answer = 1


    ######## 보이어무어 ##########

    # 건너뛸 리스트 만들기
    str_skip = {str1[i]:str1_l - i -1 for i in range(str1_l)}

    # 검색
    i = str1_l -1
    while i < len(str2):
        j = str1_l - 1

        while str2[i] == str1[j]:
            if not j:
                answer = 1
                break

            i -= 1
            j -= 1

        if str_skip[str1[j]] > str1_l - j:
            i += str_skip[str1[j]]
        else:
            i += str1_l-j



    print('#{} {}'.format(idx, answer))