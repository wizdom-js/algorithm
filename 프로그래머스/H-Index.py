# H-지수 구하는 법
# 연구자의 전체 논문을 피인용 순으로 정렬한 후, 논문의 순번과 피인용 횟수를 비교하여 피인용 횟수가 논문의 순번보다 작아지기 시작하는 직전의 순번이 연구자의 h-index가 된다.
def solution(citations):
    citations.sort(reverse=True)  # 피인용 순으로 정렬

    quotation_idx = 0
    for i in range(len(citations)):
        if citations[i] <= quotation_idx:  # 피인용 횟수가 논문 순번보다 작거나 같다면 h-index
            return quotation_idx
        quotation_idx += 1

    return quotation_idx    # 피인용 횟수가 다 같은 경우