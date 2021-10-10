import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

# 딕셔너리
for idx in range(1, tc+1):
    str1 = input()
    str_cnt = {s:0 for s in str1}

    str2 = input()
    for s in str2:
        if s in str_cnt:
            str_cnt[s] += 1

    print('#{} {}'.format(idx, max(str_cnt.values())))
    print(str_cnt)


