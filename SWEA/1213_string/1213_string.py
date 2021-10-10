import sys
sys.stdin = open('test_input.txt')

for idx in range(1, 11):
    n = int(input())    # 케이스 번호 받을 n
    target = input()    # 찾을 문자열
    string = input()    # 문장
    count = 0           # 문자열이 문장 안에 몇 번 등장했는가

    # Brute Force
    target_i = 0    # 찾을 문자열의 인덱스
    string_i = 0    # 문장의 인덱스
    # 찾을 문자열의 인덱스와, 문장의 인덱스가 각 길이를 넘지 않는 동안 반복
    while target_i < len(target) and string_i < len(string):
        # 찾는 문자열의 원소와 문장의 원소가 다르다면
        if target[target_i] != string[string_i]:
            string_i -= target_i    # 시작했던 문장 인덱스로 이동 (0번째였으면 0, 1부터 시작했으면 1) 브루트포스니까
            target_i = -1           # 찾을 문자열의 인덱스 맨 앞으로

        target_i += 1       # 찾는 문자열의 원소가 같아도, 달라도 둘다 한칸 이동한다.
        string_i += 1       # 이 코드 때문에 위에서 문장인덱스는 시작했던 곳으로(원래 그 다음으로 갔어야 하니까),  target은 -1로 가게 한 것.

        # target 인덱스가 target의 길이와 같아졌다는 말은,
        # 인덱스가 넘어갔다는 소리이므로 목표하는 단어를 찾았다는 의미가 된다.
        # 따라서 count해주고 인덱스를 맨 앞으로 돌려 놓는다.
        if target_i == len(target):
            count += 1
            target_i = 0

    print('#{} {}'.format(idx, count))
