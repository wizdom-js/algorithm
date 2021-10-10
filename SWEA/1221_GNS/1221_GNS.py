import sys
sys.stdin = open('GNS_test_input.txt')

tc = int(input())

for idx in range(1, tc+1):
    tc_num, n = input().split()
    num_list = list(input().split())

    # 각 단어가 몇 번 나올지 count 해주는 딕셔너리
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    # num_list의 단어들 +1
    for num in num_list:
        num_dict[num] += 1

    # 정답 받을 리스트
    sorted_num_list = []
    # 단어와 개수 받아와서 리스트에 개수만큼 넣은 뒤, sorted_num_list에 추가.
    for num, total in num_dict.items():
        l = [num for _ in range(total)]
        sorted_num_list.extend(l)

    print('{} {}'.format(tc_num, ' '.join(sorted_num_list)))

