def custom_split(expression):
    numbers = []
    operators = []
    num = ''
    for e in expression:
        if e in ('-', '+', '*'):
            numbers.append(int(num))
            operators.append(e)
            num = ''
        else:
            num += e
    numbers.append(int(num))
    return numbers, operators


def calculate(a, b, mark):
    if mark == "*":
        return a * b
    elif mark == "+":
        return a + b
    elif mark == "-":
        return a - b


def solution(expression):
    numbers, operators = custom_split(expression)
    print(numbers)
    print(operators)
    set_operator = list(set(operators))
    answer = 0
    for i in range(1 << len(set_operator)):
        tmp = numbers
        for j in range(len(set_operator)):
            if i & (1 << j):
                for k in range(len(operators)):
                    if operators[k] == set_operator[j]:
                        tmp[k] = calculate(tmp[k], tmp[k + 1], operators[k])
                        tmp.pop(k)
                        answer = max(answer, tmp[k])
    return answer