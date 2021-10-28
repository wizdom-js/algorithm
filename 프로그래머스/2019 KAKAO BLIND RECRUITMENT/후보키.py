from itertools import combinations


def solution(relation):
    relation_r = list(zip(*relation))   # 돌린거
    col = len(relation_r)   # 컬럼 개수
    row = len(relation)     # 행 개수
    result = 0  # 유일성 만족하는 컬럼 1개 개수

    not_candi = []  # 유일성 만족하지 못하는 컬럼
    for i in range(col):
        if row == len(set(relation_r[i])):  # 유일성을 만족하면
            result += 1     # +1
        else:
            not_candi.append(i) # 유일성을 만족하지 못하는 컬럼 리스트에 추가

    make_candi = []
    for i in range(2, len(not_candi) + 1):  # 유일성 만족못하는 컬럼들로 조합 만들기 2개부터 ~ 컬럼 개수만큼
        for combi in combinations(not_candi, i):    # i개의 개수로 조합 만들기
            tmp = [tuple(rel[j] for j in combi) for rel in relation]    # 선택한 열로 행 만들기

            if row == len(set(tmp)):   # 유일성 만족한다면
                for candi in make_candi:    # 최소성 만족하는지 보기
                    if set(combi).issuperset(candi):    # 지금 열 조합(combi)이 make_candi에 들어가있는 조합(candi)의 큰 집합인가
                    # if candi.issubset(set(combi)):
                        break                           # -> 최소성 만족하지 못함
                else:
                    make_candi.append(set(combi))   # 최소성 만족

    return result + len(make_candi) # 처음 유일성 만족하는 열 개수 + 2개 이상 열들 조합해서 만든 후보키의 개수


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in li[:]:
    li.remove(n)
print(li)


a = {1, 2}
b = {1, 2, 3, 4, 5}
print(b.issuperset(a))
print(a.issubset(b))