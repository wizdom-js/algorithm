import sys
sys.stdin = open('input.txt')

# 숫자들마다 필요한 알파벳 개수 세어 딕셔너리에 넣어주기
number_in_english = ['ZERO', 'SIX', 'EIGHT', 'SEVEN', 'FIVE', 'FOUR', 'NINE', 'TWO', 'THREE', 'ONE']
numbers_order = [0, 6, 8, 7, 5, 4, 9, 2, 3, 1]
need_alphabet_list = [dict() for _ in range(10)]
for i in range(10):
    for alphabet in number_in_english[i]:
        if need_alphabet_list[i].get(alphabet):
            need_alphabet_list[i][alphabet] += 1
        else:
            need_alphabet_list[i][alphabet] = 1


testcase = int(input())
for tc in range(1, testcase+1):
    string = input()

    alphabet_dict = dict()
    for s in string:
        if alphabet_dict.get(s):
            alphabet_dict[s] += 1
        else:
            alphabet_dict[s] = 1

    answer = ''
    for i in range(10):
        need_alphabet = need_alphabet_list[i]
        flag = True
        while flag:
            for alphabet in need_alphabet:
                if alphabet not in alphabet_dict or need_alphabet[alphabet] > alphabet_dict[alphabet]:
                    flag = False
                    break
            else:
                answer += str(numbers_order[i])
                for alphabet in need_alphabet:
                    alphabet_dict[alphabet] -= need_alphabet[alphabet]

    answer = ''.join(sorted(answer))
    print(f'Case #{tc}: {answer}')







