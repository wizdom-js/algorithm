def solution(gems):
    n = len(gems)
    gem_kinds = len(set(gems))

    # 보석의 빈도수 저장
    dic = {gems[0]: 0}
    l, r = 0, 0

    answer = [1, n]
    while n > l:
        # 모든 종류의 보석이 들어오지 않았다면
        if len(dic) != gem_kinds:
            r += 1
            # r이 보석의 끝인경우
            if r >= n:
                break

            # 빈도수 넣어주기
            if gems[r] in dic:
                dic[gems[r]] += 1
            else:
                dic[gems[r]] = 1

        # 모든 종류의 보석이 다 들어온경우
        else:
            # 기존 구간 최단거리보다 현재 구간이 더 짧다면 갱신
            if r - l < answer[1] - answer[0]:
                answer = [l + 1, r + 1]

            # 보석의 빈도수 1 이상인 경우
            if dic[gems[l]] != 1:
                dic[gems[l]] -= 1
            else:
                del dic[gems[l]]

            l += 1

    return answer