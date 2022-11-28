def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)

    return ''.join(str_numbers)